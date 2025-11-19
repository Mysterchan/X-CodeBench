import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintStream;
import java.io.PrintWriter;
import java.lang.AssertionError;
import java.lang.Integer;
import java.lang.Long;
import java.lang.Object;
import java.lang.Override;
import java.lang.Runnable;
import java.lang.String;
import java.lang.StringBuilder;
import java.lang.System;
import java.lang.Thread;
import java.lang.ThreadGroup;
import java.lang.Throwable;
import java.lang.reflect.Array;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Queue;
import java.util.Random;
import java.util.Set;
import java.util.function.IntFunction;
import java.util.function.IntToLongFunction;
import java.util.function.IntUnaryOperator;
import java.util.random.RandomGenerator;
import java.util.stream.IntStream;

class FastScanner {
    private static FastScanner instance = null;

    private final InputStream in = System.in;

    private final byte[] buffer = new byte[1024];

    private int ptr = 0;

    private int buflen = 0;

    private FastScanner() {
    }

    public static FastScanner getInstance() {
        if (instance == null) {
            instance = new FastScanner();
        }
        return instance;
    }

    private boolean hasNextByte() {
        if (ptr < buflen) {
            return true;
        }
        ptr = 0;
        try {
            buflen = in.read(buffer);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return buflen > 0;
    }

    private int readByte() {
        if (hasNextByte()) {
            return buffer[ptr++];
        } else {
            return -1;
        }
    }

    private boolean isPrintableChar(int c) {
        return (33 <= c) && (c <= 126);
    }

    public boolean hasNext() {
        while (hasNextByte() && (!isPrintableChar(buffer[ptr]))) {
            ptr++;
        }
        return hasNextByte();
    }

    public long nextLong() {
        if (!hasNext()) {
            throw new NoSuchElementException();
        }
        long n = 0;
        boolean minus = false;
        int b = readByte();
        if (b == '-') {
            minus = true;
            b = readByte();
        }
        while ((b >= '0') && (b <= '9')) {
            n = (n * 10) + (b - '0');
            b = readByte();
        }
        return minus ? -n : n;
    }

    public int nextInt() {
        return ((int) (nextLong()));
    }
}

class Graph {
    public int N;

    public int M;

    public ArrayList<Integer>[] adj;

    public Graph(int N) {
        this.N = N;
        adj = new ArrayList[N];
        for (int i = 0; i < N; ++i) {
            adj[i] = new ArrayList<>();
        }
    }

    public void addEdge(int from, int to) {
        adj[from].add(to);
        ++M;
    }

    public void addUnorientedEdge(int a, int b) {
        addEdge(a, b);
        if (b != a) {
            addEdge(b, a);
        }
    }
}

class ArrayUtils {
    public static void swap(int i, int j, int[] A) {
        if (i == j) {
            return;
        }
        int tmp = A[i];
        A[i] = A[j];
        A[j] = tmp;
    }

    public static void reverse(int[] a) {
        int s = 0;
        int t = a.length - 1;
        while (s < t) {
            swap(s, t, a);
            ++s;
            --t;
        }
    }
}

class Forest extends Graph {
    public int N;

    public int[] parent;

    public int[] depth;

    public Forest(int N) {
        super(N);
        this.N = N;
    }

    public int[] rooted(int root) {
        if (parent == null) {
            parent = new int[N + 1];
            depth = new int[N + 1];
            Arrays.fill(parent, N);
            depth[N] = -1;
        }
        parent[root] = N;
        depth[root] = 0;
        Queue<Integer> que = new ArrayDeque<>();
        que.add(root);
        ArrayList<Integer> bfsOrder = new ArrayList<>();
        while (!que.isEmpty()) {
            int v = que.poll();
            bfsOrder.add(v);
            for (int next : adj[v]) {
                if (next == parent[v]) {
                    continue;
                }
                que.add(next);
                parent[next] = v;
                depth[next] = depth[v] + 1;
            }
        }
        int[] ret = new int[bfsOrder.size()];
        for (int i = 0; i < bfsOrder.size(); ++i) {
            ret[i] = bfsOrder.get(i);
        }
        return ret;
    }
}

class MyPrintWriter extends PrintWriter {
    private static MyPrintWriter instance = null;

    private MyPrintWriter() {
        super(System.out);
    }

    public static MyPrintWriter getInstance() {
        if (instance == null) {
            instance = new MyPrintWriter();
        }
        return instance;
    }

    public MyPrintWriter(PrintStream out) {
        super(out);
    }
}

public class Main implements Runnable {
    public static void main(String[] args) throws IOException {
        new Thread(null, new Main(), "", (1024 * 1024) * 1024).start();

    }

    long solve(int N, int[] p) {
        for (int i = 0; i < p.length; ++i) {
            p[i] -= 1;
        }
        Forest g = new Forest(N);
        for (int i = 1; i < N; ++i) {
            g.addUnorientedEdge(i, p[i]);
        }
        var bfsOrder = g.rooted(0);
        ArrayUtils.reverse(bfsOrder);
        int[] dp = new int[N];
        for (int v : bfsOrder) {
            ArrayList<Integer> list = new ArrayList<>();
            for (int u : g.adj[v]) {
                if (u == g.parent[v]) {
                    continue;
                }
                list.add(dp[u]);
            }
            Collections.sort(list);
            int sum = 0;
            for (int i = 0; i < (list.size() - 1); ++i) {
                sum += list.get(i);
            }
            if (list.size() <= 1) {
                for (int val : list) {
                    dp[v] += val;
                }
            } else if (sum >= list.get(list.size() - 1)) {
                dp[v] = (sum + list.get(list.size() - 1)) % 2;
            } else {
                dp[v] = list.get(list.size() - 1) - sum;
            }
            dp[v]++;
        }
        return (N - dp[0]) / 2;
    }

    @Override
    public void run() {
        FastScanner sc = FastScanner.getInstance();
        MyPrintWriter pw = MyPrintWriter.getInstance();
        int T = sc.nextInt();
        for (int t = 0; t < T; ++t) {
            int N = sc.nextInt();
            int[] p = new int[N];
            p[0] = -1;
            for (int i = 1; i < N; ++i) {
                p[i] = sc.nextInt();
            }
            pw.println(solve(N, p));
        }
        pw.close();
    }
}