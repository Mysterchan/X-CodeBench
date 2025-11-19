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
import java.lang.Throwable;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashSet;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Queue;
import java.util.Random;
import java.util.Set;
import java.util.function.IntUnaryOperator;

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

    public static Graph read(int N, int M) {
        Graph graph = new Graph(N);
        FastScanner sc = FastScanner.getInstance();
        for (int i = 0; i < M; ++i) {
            int a = sc.nextInt() - 1;
            int b = sc.nextInt() - 1;
            graph.adj[a].add(b);
            graph.adj[b].add(a);
        }
        return graph;
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
    }

    @Override
    public void run() {
        FastScanner sc = FastScanner.getInstance();
        MyPrintWriter pw = MyPrintWriter.getInstance();
        int N = sc.nextInt();
        int M = sc.nextInt();
        Graph g = Graph.read(N, M);
        int cnt = 0;
        for (int i = 0; i < N; ++i) {
            if ((((N - 1) - g.adj[i].size()) % 2) == 1) {
                cnt++;
            }
        }
        System.out.println((((1L * N) * (N - 1)) / 2) - (cnt / 2));
        pw.close();
    }
}