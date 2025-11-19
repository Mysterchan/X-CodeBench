import java.io.*;
import java.util.*;

public class Main {
    private static int MDC = (int) 998244353;
    static long[] P = new long[501];
    static long[] INV_P = new long[501];

    static {
        P[0] = 1;
        for (int i = 1; i < 501; i++) {
            P[i] = (P[i - 1] * i) % MDC;
        }
        INV_P[500] = pow(P[500], MDC - 2);
        for (int i = 499; i >= 0; i--) {
            INV_P[i] = (INV_P[i + 1] * (i + 1)) % MDC;
        }
    }

    public static void main(String[] args) throws IOException {
        sc = new MScanner(System.in);
        pw = new PrintWriter(System.out);
        int t = sc.nextInt();

        for (int i = 0; i < t; i++) {
            solver();
        }
    }

    public static void solver() throws IOException {
        int n = sc.nextInt();
        int m = sc.nextInt();
        int x = sc.nextInt();
        int y = sc.nextInt();
        List<Integer>[] graph = new List[n + 1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int i = 0; i < m; i++) {
            int f = sc.nextInt();
            int e = sc.nextInt();
            graph[f].add(e);
            graph[e].add(f);
        }
        for (int i = 1; i <= n; i++) {
            graph[i].sort(Integer::compareTo);
        }
        List<Integer> list = new ArrayList<>();
        dfs(x, list, graph, y);
        pw.flush();
    }

    public static int dfs(int x, List<Integer> list, List<Integer>[] graph, int y) {
        list.add(x);
        if (x == y) {
            for (int i = 0; i < list.size(); i++) {
                pw.print(list.get(i) + " ");
            }
            pw.println();
            pw.flush();
            return -1;
        }
        for (int o : graph[x]) {
            if(list.contains(o)) {
                continue;
            }
            int ans = dfs(o, list, graph, y);
            if (ans < 0) return -1;
        }
        list.remove(list.size() - 1);
        return 1;
    }

    public static int[] calculateZ(int[] nums) {
        int n = nums.length;
        int[] z = new int[n];
        z[0] = n;

        int l = 0, r = 0;
        for (int i = 1; i < n; i++) {
            if (i <= r) {
                z[i] = Math.min(r - i + 1, z[i - l]);
            }
            while (i + z[i] < n && nums[z[i]] == nums[i + z[i]]) {
                z[i]++;
            }
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }
        return z;
    }

    public static long gcd(long a, long b) {
        if (a < b) return gcd(b, a);
        if (b == 0)
            return a;
        else
            return gcd(b, a % b);
    }

    private static long pow(long n, long m) {
        long res = 1;
        long base = n;
        while (m != 0) {
            if ((m & 1) == 1) {
                res = res * base;
                res %= MDC;
            }
            base = base * base;
            base %= MDC;
            m = m >> 1;
        }
        return res;
    }

    static int curt;
    static PrintWriter pw;
    static MScanner sc;

    static class MScanner {
        StringTokenizer st;
        BufferedReader br;

        public MScanner(InputStream system) {
            br = new BufferedReader(new InputStreamReader(system));
        }

        public MScanner(String file) throws Exception {
            br = new BufferedReader(new FileReader(file));
        }

        public String next() throws IOException {
            while (st == null || !st.hasMoreTokens())
                st = new StringTokenizer(br.readLine());
            return st.nextToken();
        }

        public String nextLine() throws IOException {
            return br.readLine();
        }

        public int nextInt() throws IOException {
            return Integer.parseInt(next());
        }

        public double nextDouble() throws IOException {
            return Double.parseDouble(next());
        }

        public char nextChar() throws IOException {
            return next().charAt(0);
        }

        public long nextLong() throws IOException {
            return Long.parseLong(next());
        }

        public boolean ready() throws IOException {
            return br.ready();
        }

        public void waitForInput() throws InterruptedException {
            Thread.sleep(3000);
        }

    }

    static void dbg(int[] in) {
        System.out.println(Arrays.toString(in));
    }

    static void dbg(long[] in) {
        System.out.println(Arrays.toString(in));
    }

    static void sort(int[] in) {
        shuffle(in);
        Arrays.sort(in);
    }

    static void sort(long[] in) {
        shuffle(in);
        Arrays.sort(in);
    }

    static void shuffle(int[] in) {
        for (int i = 0; i < in.length; i++) {
            int idx = (int) (Math.random() * in.length);
            int tmp = in[i];
            in[i] = in[idx];
            in[idx] = tmp;
        }
    }

    static void shuffle(long[] in) {
        for (int i = 0; i < in.length; i++) {
            int idx = (int) (Math.random() * in.length);
            long tmp = in[i];
            in[i] = in[idx];
            in[idx] = tmp;
        }
    }
}

class XorBasis {
    private final int[] b;

    public XorBasis(int n) {
        b = new int[n];
    }

    public void insert(int x) {
        while (x > 0) {
            int i = 31 - Integer.numberOfLeadingZeros(x);
            if (b[i] == 0) {
                b[i] = x;
                return;
            }
            x ^= b[i];
        }

    }

    public int maxXor() {
        int res = 0;

        for (int i = b.length - 1; i >= 0; i--) {
            res = Math.max(res, res ^ b[i]);
        }
        return res;
    }
}

class FenwickTree {
    private final long[] tree;

    public FenwickTree(int n) {
        tree = new long[n + 1];
    }

    public void update(int i, long val) {
        for (; i < tree.length; i += i & -i) {
            tree[i] += val;
        }
    }

    public long pre(int i) {
        long res = 0;
        for (; i > 0; i &= i - 1) {
            res += tree[i];
        }
        return res;
    }
}