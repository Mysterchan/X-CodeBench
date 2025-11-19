import java.io.*;
import java.util.*;
import java.util.function.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) throws Exception {
        FastScanner sc = new FastScanner();
        int n = sc.nextInt();
        int q = sc.nextInt();
        SegmentTree st = new SegmentTree(n + 1);
        StringBuilder sb = new StringBuilder();
        while (q-- > 0) {
            int a = sc.nextInt() - 1;
            int b = sc.nextInt() - 1;
            if (st.same(a, b)) {
                sb.append("Yes\n");
                st.add(a, b + 1, q);
            } else {
                sb.append("No\n");
            }
        }
        System.out.print(sb);
    }

    static class SegmentTree {
        static final int COUNT = 20;
        static int[] mods = new int[COUNT];
        static {
            int v = 1000000000;
            for (int i = 0; i < COUNT; i++) {
                while (!isPrime(v)) {
                    v++;
                }
                mods[i] = v++;
            }
        }
        int size;
        long[][] values;

        public SegmentTree(int x) {
            size = 2;
            while (size < x) {
                size <<= 1;
            }
            values = new long[size * 2 - 1][COUNT];
        }

        public void add(int left, int right, long v) {
            add(0, 0, size, left, right, v);
        }

        private void add(int idx, int min, int max, int left, int right, long v) {
            if (max <= left || right <= min) {
                return;
            } else if (left <= min && max <= right) {
                for (int i = 0; i < COUNT; i++) {
                    long current = pow(v + 17, mods[i] - 2, mods[i]);
                    values[idx][i] += v;
                    values[idx][i] %= mods[i];
                }
            } else {
                add(idx * 2 + 1, min, (min + max) / 2, left, right, v);
                add(idx * 2 + 2, (min + max) / 2, max, left, right, v);
            }
        }

        public boolean same(int a, int b) {
            for (int i = 0; i < COUNT; i++) {
                if (getValue(a + size - 1, i) != getValue(b + size - 1, i)) {
                    return false;
                }
            }
            return true;
        }

        public long getValue(int idx, int c) {
            return (values[idx][c] + (idx == 0 ? 0 : getValue((idx - 1) / 2, c))) % mods[c];
        }

        static boolean isPrime(int x) {
            for (int i = 2; i <= Math.sqrt(x); i++) {
                if (x % i == 0) {
                    return false;
                }
            }
            return true;
        }

        static long pow(long x, int p, int m) {
            if (p == 0) {
                return 1;
            } else if (p % 2 == 0) {
                return pow(x * x % m, p / 2, m);
            } else {
                return pow(x, p - 1, m) * x % m;
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