import java.io.*;
import java.util.*;
import java.util.function.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) throws Exception {
        FastScanner sc = new FastScanner();
        int n = sc.nextInt();
        int[] order = new int[n];
        for (int i = 0; i < n; i++) {
            order[i] = sc.nextInt() - 1;
        }
        SegmentTree st = new SegmentTree(n + 1);
        for (int i = 0; i <= n; i++) {
            st.add(i, 1);
        }
        int[] ans = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            int idx = st.getIdx(order[i]);
            ans[idx] = i + 1;
            st.add(idx, -1);
        }
        System.out.println(Arrays.stream(ans).mapToObj(String::valueOf).collect(Collectors.joining(" ")));
    }

    static class SegmentTree {
        int size;
        int[] values;

        public SegmentTree(int x) {
            size = 2;
            while (size < x) {
                size <<= 1;
            }
            values = new int[size * 2 - 1];
        }

        public void add(int idx, int v) {
            values[idx + size - 1] += v;
            calc((idx + size - 2) / 2);
        }

        private void calc(int idx) {
            values[idx] = values[idx * 2 + 1] + values[idx * 2 + 2];
            if (idx > 0) {
                calc((idx - 1) / 2);
            }
        }

        public int getIdx(int v) {
            int left = 0;
            int right = size;
            while (right - left > 1) {
                int m = (left + right) / 2;
                if (getSum(m) <= v) {
                    left = m;
                } else {
                    right = m;
                }
            }
            return left;
        }

        private int getSum(int right) {
            return getSum(0, 0, size, right);
        }

        private int getSum(int idx, int min, int max, int right) {
            if (right <= min) {
                return 0;
            } else if (max <= right) {
                return values[idx];
            } else {
                return getSum(idx * 2 + 1, min, (min + max) / 2, right)
                    + getSum(idx * 2 + 2, (min + max) / 2, max, right);
            }
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