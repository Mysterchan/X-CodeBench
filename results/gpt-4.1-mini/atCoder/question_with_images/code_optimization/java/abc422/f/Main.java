import java.io.*;
import java.util.*;

public class Main {
    static class State implements Comparable<State> {
        int node;
        long weight;
        long fuel;

        State(int node, long weight, long fuel) {
            this.node = node;
            this.weight = weight;
            this.fuel = fuel;
        }

        public int compareTo(State o) {
            return Long.compare(this.fuel, o.fuel);
        }
    }

    public static void main(String[] args) throws Exception {
        FastScanner sc = new FastScanner();
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] W = new int[n];
        for (int i = 0; i < n; i++) {
            W[i] = sc.nextInt();
        }
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt() - 1;
            int v = sc.nextInt() - 1;
            graph[u].add(v);
            graph[v].add(u);
        }

        // dist[i] = minimal fuel to reach node i
        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[0] = 0;

        // weight[i] = minimal weight upon arrival at node i for the minimal fuel path
        long[] weight = new long[n];
        Arrays.fill(weight, Long.MAX_VALUE);
        weight[0] = W[0];

        PriorityQueue<State> pq = new PriorityQueue<>();
        pq.add(new State(0, W[0], 0));

        while (!pq.isEmpty()) {
            State cur = pq.poll();
            int u = cur.node;
            long w = cur.weight;
            long f = cur.fuel;

            if (dist[u] < f) continue;
            if (dist[u] == f && weight[u] < w) continue;

            for (int nxt : graph[u]) {
                long newFuel = f + w;
                long newWeight = w + W[nxt];
                if (newFuel < dist[nxt] || (newFuel == dist[nxt] && newWeight < weight[nxt])) {
                    dist[nxt] = newFuel;
                    weight[nxt] = newWeight;
                    pq.add(new State(nxt, newWeight, newFuel));
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(dist[i]).append('\n');
        }
        System.out.print(sb);
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

        public String next() {
            byte b = read();

            while (isSpaceChar(b)) {
                b = read();
            }
            StringBuilder sb = new StringBuilder();
            while (!isSpaceChar(b)) {
                sb.append((char) b);
                b = read();
            }
            return sb.toString();
        }

        public int nextInt() {
            int ret = 0;
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

        public long nextLong() {
            long ret = 0;
            byte c = read();
            while (isSpaceChar(c)) c = read();
            boolean neg = (c == '-');
            if (neg) c = read();
            do {
                ret = ret * 10L + c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return neg ? -ret : ret;
        }

        private boolean isSpaceChar(byte c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }
    }
}