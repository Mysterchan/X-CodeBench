import java.io.*;
import java.util.*;
import java.util.function.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) throws Exception {
        FastScanner sc = new FastScanner();
        int n = sc.nextInt();
        Deque<Unit> current = new ArrayDeque<>();
        for (char c : sc.next().toCharArray()) {
            current.add(new Unit(c - '0', 1));
        }
        Deque<Unit> next = new ArrayDeque<>();
        while (current.size() > 1) {
            next.add(getNext(current.poll(), current.poll(), current.poll()));
            Deque<Unit> tmp = next;
            next = current;
            current = tmp;
        }
        System.out.println(current.poll().count);
    }

    static Unit getNext(Unit a, Unit b, Unit c) {
        Unit ans;
        if (a.type == 1) {
            if (b.type == 1) {
                if (c.type == 1) {
                    if (a.count >= b.count && a.count >= c.count) {
                        ans = new Unit(1, b.count + c.count);
                    } else if (b.count >= a.count && b.count >= c.count) {
                        ans = new Unit(1, a.count + c.count);
                    } else {
                        ans = new Unit(1, a.count + b.count);
                    }
                } else {
                    ans = new Unit(1, Math.min(a.count, b.count));
                }
            } else {
                if (c.type == 1) {
                    ans = new Unit(1, Math.min(a.count, c.count));
                } else {
                    ans = new Unit(0, Math.min(b.count, c.count));
                }
            }
        } else {
            if (b.type == 1) {
                if (c.type == 1) {
                    ans = new Unit(1, Math.min(b.count, c.count));
                } else {
                    ans = new Unit(0, Math.min(a.count, c.count));
                }
            } else {
                if (c.type == 1) {
                    ans = new Unit(0, Math.min(a.count, b.count));
                } else {
                    if (a.count >= b.count && a.count >= c.count) {
                        ans = new Unit(0, b.count + c.count);
                    } else if (b.count >= a.count && b.count >= c.count) {
                        ans = new Unit(0, a.count + c.count);
                    } else {
                        ans = new Unit(0, a.count + b.count);
                    }
                }
            }
        }
        return ans;
    }

    static class Unit {
        int type;
        int count;

        public Unit(int type, int count) {
            this.type = type;
            this.count = count;
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