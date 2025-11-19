import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        FastScanner sc = new FastScanner();
        int n = sc.nextInt();
        int m = sc.nextInt();
        long[] weights = new long[n];
        for (int i = 0; i < n; i++) {
            weights[i] = sc.nextLong();
        }

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt() - 1;
            int v = sc.nextInt() - 1;
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        long[] minFuel = new long[n];
        Arrays.fill(minFuel, Long.MAX_VALUE);
        minFuel[0] = 0;

        PriorityQueue<Triplet> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a.fuel));
        pq.add(new Triplet(0, 0)); // (current vertex, fuel consumed)

        while (!pq.isEmpty()) {
            Triplet current = pq.poll();
            int u = current.vertex;

            if (current.fuel > minFuel[u]) continue;

            long currentWeight = current.fuel;
            for (int v : graph.get(u)) {
                long newFuel = currentWeight + (currentWeight + weights[v]);
                if (newFuel < minFuel[v]) {
                    minFuel[v] = newFuel;
                    pq.add(new Triplet(v, newFuel));
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (long fuel : minFuel) {
            sb.append(fuel).append("\n");
        }
        System.out.print(sb);
    }

    static class Triplet {
        int vertex;
        long fuel;

        public Triplet(int vertex, long fuel) {
            this.vertex = vertex;
            this.fuel = fuel;
        }
    }

    static class FastScanner {
        private DataInputStream din;
        private byte[] buffer;
        private int bufferPointer, bytesRead;
        private static final int BUFFER_SIZE = 1 << 16;

        public FastScanner() {
            din = new DataInputStream(System.in);
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        private byte read() {
            try {
                if (bufferPointer == bytesRead) {
                    bytesRead = din.read(buffer, 0, BUFFER_SIZE);
                    if (bytesRead == -1) return -1;
                    bufferPointer = 0;
                }
                return buffer[bufferPointer++];
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }

        public long nextLong() {
            long ret = 0;
            byte c = read();
            while (isSpaceChar(c)) c = read();
            boolean neg = (c == '-');
            if (neg) c = read();
            do {
                ret = ret * 10 + c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return neg ? -ret : ret;
        }

        private boolean isSpaceChar(byte c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }
    }
}