import java.io.*;
import java.util.*;
import java.util.function.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) throws Exception {
        FastScanner sc = new FastScanner();
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] values = new int[n];
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextInt();
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            int a = sc.nextInt() - 1;
            int b = sc.nextInt() - 1;
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        PriorityQueue<Path> queue = new PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            queue.add(new Path(0, i, 0));
        }
        long[][] costs = new long[n][n];
        for (long[] arr : costs) {
            Arrays.fill(arr, Long.MAX_VALUE);
        }
        while (queue.size() > 0) {
            Path p = queue.poll();
            if (costs[p.count][p.idx] <= p.value) {
                continue;
            }
            costs[p.count][p.idx] = p.value;
            if (p.count == 0) {
                continue;
            }
            for (int x : graph.get(p.idx)) {
                queue.add(new Path(x, p.count - 1, p.value + (long)values[p.idx] * p.count));
            }
        }
        System.out.println(Arrays.stream(costs[0]).mapToObj(String::valueOf).collect(Collectors.joining("\n")));
    }

    static class Path implements Comparable<Path> {
        int idx;
        int count;
        long value;

        public Path(int idx, int count, long value) {
            this.idx = idx;
            this.count = count;
            this.value = value;
        }

        public int compareTo(Path another) {
            return Long.compare(value, another.value);
        }
    }
}

class FastScanner {
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

    public double nextDouble() {
        double ret = 0, div = 1;
        byte c = read();
        while (isSpaceChar(c)) c = read();
        boolean neg = (c == '-');
        if (neg) c = read();
        do {
            ret = ret * 10 + c - '0';
            c = read();
        } while (!isSpaceChar(c) && c != '.');
        if (c == '.') {
            while (!isSpaceChar(c = read())) {
                ret += (c - '0') / (div *= 10);
            }
        }
        return neg ? -ret : ret;
    }

    private boolean isSpaceChar(byte c) {
        return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
    }

    public void close() {
        try {
            if (din != null) din.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}