import java.io.*;
import java.util.*;

class MaxSegmentTree {
    private final int n;
    private final long[] tree;
    private long mergeVal(long a, long b) {
        return Math.max(a, b);
    }
    public MaxSegmentTree(int n, long initVal) {
        this.n = n;
        long[] a = new long[n];
        Arrays.fill(a, initVal);
        tree = new long[2 << (32 - Integer.numberOfLeadingZeros(n - 1))];
        build(a, 1, 0, n - 1);
    }
    public MaxSegmentTree(long[] a) {
        n = a.length;
        tree = new long[2 << (32 - Integer.numberOfLeadingZeros(n - 1))];
        build(a, 1, 0, n - 1);
    }
    public void update(int i, long val) {
        update(1, 0, n - 1, i, val);
    }
    public long query(int ql, int qr) {
        return query(1, 0, n - 1, ql, qr);
    }
    public long get(int i) {
        return query(1, 0, n - 1, i, i);
    }
    private void maintain(int node) {
        tree[node] = mergeVal(tree[node * 2], tree[node * 2 + 1]);
    }
    private void build(long[] a, int node, int l, int r) {
        if (l == r) {
            tree[node] = a[l];
            return;
        }
        int m = (l + r) / 2;
        build(a, node * 2, l, m);
        build(a, node * 2 + 1, m + 1, r);
        maintain(node);
    }
    private void update(int node, int l, int r, int i, long val) {
        if (l == r) {
            tree[node] = mergeVal(tree[node], val);
            return;
        }
        int m = (l + r) / 2;
        if (i <= m) {
            update(node * 2, l, m, i, val);
        } else {
            update(node * 2 + 1, m + 1, r, i, val);
        }
        maintain(node);
    }
    private long query(int node, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr) {
            return tree[node];
        }
        int m = (l + r) / 2;
        if (qr <= m) {
            return query(node * 2, l, m, ql, qr);
        }
        if (ql > m) {
            return query(node * 2 + 1, m + 1, r, ql, qr);
        }
        long lRes = query(node * 2, l, m, ql, qr);
        long rRes = query(node * 2 + 1, m + 1, r, ql, qr);
        return mergeVal(lRes, rRes);
    }
}

class MinSegmentTree {
    private final int n;
    private final long[] tree;
    private long mergeVal(long a, long b) {
        return Math.min(a, b);
    }
    public MinSegmentTree(int n, long initVal) {
        this.n = n;
        long[] a = new long[n];
        Arrays.fill(a, initVal);
        tree = new long[2 << (32 - Integer.numberOfLeadingZeros(n - 1))];
        build(a, 1, 0, n - 1);
    }
    public MinSegmentTree(long[] a) {
        n = a.length;
        tree = new long[2 << (32 - Integer.numberOfLeadingZeros(n - 1))];
        build(a, 1, 0, n - 1);
    }
    public void update(int i, long val) {
        update(1, 0, n - 1, i, val);
    }
    public long query(int ql, int qr) {
        return query(1, 0, n - 1, ql, qr);
    }
    public long get(int i) {
        return query(1, 0, n - 1, i, i);
    }
    private void maintain(int node) {
        tree[node] = mergeVal(tree[node * 2], tree[node * 2 + 1]);
    }
    private void build(long[] a, int node, int l, int r) {
        if (l == r) {
            tree[node] = a[l];
            return;
        }
        int m = (l + r) / 2;
        build(a, node * 2, l, m);
        build(a, node * 2 + 1, m + 1, r);
        maintain(node);
    }
    private void update(int node, int l, int r, int i, long val) {
        if (l == r) {
            tree[node] = mergeVal(tree[node], val);
            return;
        }
        int m = (l + r) / 2;
        if (i <= m) {
            update(node * 2, l, m, i, val);
        } else {
            update(node * 2 + 1, m + 1, r, i, val);
        }
        maintain(node);
    }
    private long query(int node, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr) {
            return tree[node];
        }
        int m = (l + r) / 2;
        if (qr <= m) {
            return query(node * 2, l, m, ql, qr);
        }
        if (ql > m) {
            return query(node * 2 + 1, m + 1, r, ql, qr);
        }
        long lRes = query(node * 2, l, m, ql, qr);
        long rRes = query(node * 2 + 1, m + 1, r, ql, qr);
        return mergeVal(lRes, rRes);
    }
}

public class Main {
    boolean MULTI_CASE = false;
    boolean ALWAYS_FLUSH = false;
    void go() {
        int n = nextInt();
        int q = nextInt();
        MaxSegmentTree L = new MaxSegmentTree(n + 5, -1);
        MinSegmentTree R = new MinSegmentTree(n + 5, Integer.MAX_VALUE);
        while (q-- > 0) {
            int l = nextInt();
            int r = nextInt();
            l--; r--;
            long minv = R.query(l, r);
            long maxv = L.query(l, r);
            if (minv < l || maxv > r) {
                sl("No");
            } else {
                sl("Yes");
                L.update(l, r);
                R.update(r, l);
            }
        }
    }

    InputStream inStream;
    byte[] inBuff = new byte[1024];
    int inBuffCursor = 0, inBuffLen = 0;

    boolean isVisibleChar(int c) {
        return 33 <= c && c <= 126;
    }

    boolean hasNextByte() {
        if (inBuffCursor < inBuffLen) return true;
        inBuffCursor = 0;
        try {
            inBuffLen = inStream.read(inBuff);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return inBuffLen > 0;
    }

    boolean hasNext() {
        while (hasNextByte() && !isVisibleChar(inBuff[inBuffCursor])) inBuffCursor++;
        return hasNextByte();
    }

    int nextByte() {
        return hasNextByte() ? inBuff[inBuffCursor++] : -1;
    }

    String next() {
        if (!hasNext()) throw new RuntimeException("no next.");
        StringBuilder sb = new StringBuilder();
        int b = nextByte();
        while (isVisibleChar(b)) {
            sb.appendCodePoint(b);
            b = nextByte();
        }
        return sb.toString();
    }

    long nextLong() {
        if (!hasNext()) throw new RuntimeException("no next.");
        long result = 0;
        boolean negative = false;
        int b = nextByte();
        if (b < '0') {
            if (b == '-') negative = true;
            else if (b != '+') throw new RuntimeException("long number must start with +/-.");
            b = nextByte();
        }
        while (isVisibleChar(b)) {
            if (b < '0' || b > '9') throw new RuntimeException("wrong digit in long:" + (char) b);

            result = result * 10 + (b - '0');
            b = nextByte();
        }
        return negative ? -result : result;
    }

    int nextInt() {
        long x = nextLong();
        if (x < Integer.MIN_VALUE || x > Integer.MAX_VALUE)
            throw new RuntimeException("int overflow:" + x);
        return (int) x;
    }

    double nextDouble() {
        return Double.parseDouble(next());
    }

    PrintWriter printOut = new PrintWriter(System.out);

    void so(Object obj, boolean newLine) {
        if (newLine) printOut.println(obj);
        else printOut.print(obj);
        if (ALWAYS_FLUSH) printOut.flush();
    }

    void so(Object obj) {
        so(obj, false);
    }

    void sl(Object obj) {
        so(obj, true);
    }

    void sl() {
        sl("");
    }

    void mainGo() {
        try {
            inStream = new FileInputStream("src/main.in");
            ALWAYS_FLUSH = true;
        } catch (Exception e) {
            inStream = System.in;
        }
        while (hasNext()) {
            if (MULTI_CASE) {
                int T = nextInt();
                if (T == 0) break;
                for (int i = 0; i < T; ++i) {
                    go();
                }
            } else {
                go();
            }
        }
        printOut.flush();
    }

    public static void main(String[] args) {
        new Main().mainGo();
    }
}