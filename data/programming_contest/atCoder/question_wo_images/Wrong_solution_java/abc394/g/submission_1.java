import java.io.*;
import java.util.*;

public class Main {
    public static int INF = 0x3f3f3f3f, mod = 1000000007, mod9 = 998244353;
    public static void main(String args[]){
        try {
            PrintWriter o = new PrintWriter(System.out);
            boolean multiTest = false;

            if(multiTest) {
                int t = nextInt(), loop = 0;
                while (loop < t) {loop++;solve(o);}
            } else solve(o);
            o.close();
        } catch (Exception e) {e.printStackTrace();}
    }
    static void solve(PrintWriter o) {
        try {
            int H = nextInt(), W = nextInt();
            int[][] F = new int[H][W];
            int MAX = 0;
            for(int i=0;i<H;i++) for(int j=0;j<W;j++) {
                F[i][j] = nextInt();
                MAX = Math.max(MAX, F[i][j]);
            }
            int Q = nextInt();
            int[] A = new int[Q];
            int[] B = new int[Q];
            int[] Y = new int[Q];
            int[] C = new int[Q];
            int[] D = new int[Q];
            int[] Z = new int[Q];
            for(int i=0;i<Q;i++) {
                A[i] = nextInt()-1;
                B[i] = nextInt()-1;
                Y[i] = nextInt();
                C[i] = nextInt()-1;
                D[i] = nextInt()-1;
                Z[i] = nextInt();
            }
            int[] l = new int[Q];
            int[] r = new int[Q];
            Arrays.fill(l, 1);
            Arrays.fill(r, MAX);
            List<int[]>[] E = new ArrayList[MAX+1];
            Arrays.setAll(E, key->new ArrayList<>());
            for(int i=0;i<H-1;i++) for(int j=0;j<W;j++) E[Math.min(F[i][j], F[i+1][j])].add(new int[]{i*W+j, (i+1)*W+j});
            for(int i=0;i<H;i++) for(int j=0;j<W-1;j++) E[Math.min(F[i][j], F[i][j+1])].add(new int[]{i*W+j, i*W+j+1});
            List<Integer>[] check = new ArrayList[MAX+1];
            Arrays.setAll(check, key->new ArrayList<>());
            while(true) {
                for(int i=1;i<=MAX;i++) check[i].clear();
                boolean goOn = false;
                for(int i=0;i<Q;i++) {
                    if(l[i] < r[i]) {
                        int m = (l[i]+r[i])/2;
                        check[m].add(i);
                        goOn = true;
                    }
                }
                if(!goOn) break;
                DSU dsu = new DSU(H*W);
                for(int f=MAX;f>=1;f--) {
                    for(int[] it: E[f]) dsu.union(it[0], it[1]);
                    for(int i: check[f]) {
                        int u = A[i]*W+B[i];
                        int v = C[i]*W+D[i];
                        if(dsu.find(u) == dsu.find(v)) l[i] = f+1;
                        else r[i] = f;
                    }
                }
            }
            for(int i=0;i<Q;i++) {
                int lower = Math.min(l[i]-1, Math.min(Y[i], Z[i]));
                o.println(Y[i] + Z[i] - 2*lower);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    public static int lower_bound(List<Integer> li, long val){
        int l = 0, r = li.size();
        while(l < r){
            int mid = l + (r - l) / 2;
            if(li.get(mid) < val) l = mid + 1;
            else r = mid;
        }
        return l;
    }
    public static int upper_bound(List<Integer> li, int val){
        int l = 0, r = li.size();
        while(l < r){
            int mid = l + (r - l) / 2;
            if(li.get(mid) <= val) l = mid + 1;
            else r = mid;
        }
        return l;
    }
    public static int upper_bound(int[] a, long val){
        int l = 0, r = a.length;
        while(l < r){
            int mid = l + (r - l) / 2;
            if(a[mid] <= val) l = mid + 1;
            else r = mid;
        }
        return l;
    }
    public static int lower_bound(int[] a, int val){
        int l = 0, r = a.length;
        while(l < r){
            int mid = l + (r - l) / 2;
            if(a[mid] < val) l = mid + 1;
            else r = mid;
        }
        return l;
    }
    public static long gcd(long a, long b) {
        return b == 0 ? a : gcd(b, a%b);
    }
    public static long[] extgcd(long a, long b) {
        if(b == 0) return new long[]{1, 0};
        long[] it = extgcd(b, a%b);
        long x = it[1], y = it[0];
        y -= a/b*x;
        return new long[]{x, y};
    }
    public static long lcm(long a, long b){
        return a / gcd(a,b)*b;
    }
    public static long qpow(long a, long n){
        long ret = 1l;
        while(n > 0){
            if((n & 1) == 1) ret = ret * a;
            n >>= 1;
            a = a * a;
        }
        return ret;
    }
    public static long qpow(long a, long n, int md){
        a %= md;
        long ret = 1l;
        while(n > 0){
            if((n & 1) == 1) ret = ret * a % md;
            n >>= 1;
            a = a * a % md;
        }
        return ret;
    }
    public static class FenWick {
        int n;
        long[] a;
        long[] tree;
        public FenWick(int n){
            this.n = n;
            a = new long[n+1];
            tree = new long[n+1];
        }
        private void add(int x, long val){
            while(x <= n){
                tree[x] += val;
                x += x&-x;
            }
        }
        private void addMx(int x, long val) {
            a[x] += val;
            tree[x] = a[x];
            while(x <= n) {
                for(int i=1;i<(x&-x);i<<=1) tree[x] = Math.max(tree[x], tree[x-i]);
                x += x&-x;
            }
        }
        private void addMn(int x, long val) {
            a[x] += val;
            tree[x] = a[x];
            while(x <= n) {
                for(int i=1;i<(x&-x);i<<=1) tree[x] = Math.min(tree[x], tree[x-i]);
                x += x&-x;
            }
        }
        private long query(int x){
            long ret = 0l;
            while(x > 0){
                ret += tree[x];
                x -= x&-x;
            }
            return ret;
        }
        private long queryMx(int l, int r) {
            long res = 0l;
            while(l <= r) {
                if(r-(r&-r) >= l) {
                    res = Math.max(res, tree[r]);
                    r -= r&-r;
                }
                else {
                    res = Math.max(res, a[r]);
                    r--;
                }
            }
            return res;
        }
        private long queryMn(int l, int r) {
            long res = 1l<<55;
            while(l <= r) {
                if(r-(r&-r) >= l) {
                    res = Math.min(res, tree[r]);
                    r -= r&-r;
                }
                else {
                    res = Math.min(res, a[r]);
                    r--;
                }
            }
            return res;
        }
    }
    static class Pair {
        Integer p1, p2;
        public Pair(Integer p1, Integer p2) {
            this.p1 = p1;
            this.p2 = p2;
        }
        @Override
        public int hashCode() {
            int prime = 31, ret = 0;
            ret = ret*prime+p1.hashCode();
            ret = ret*prime+p2.hashCode();
            return ret;
        }
        @Override
        public boolean equals(Object o) {
            if(o instanceof Pair pair) {
                return p1.equals(pair.p1) && p2.equals(pair.p2);
            }
            return false;
        }
    }
    static class DSU {
        int[] parent;
        int[] size;
        public DSU(int n) {
            parent = new int[n];
            size = new int[n];
            for(int i=0;i<n;i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }
        public int find(int x) {
            if(parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }
        public void union(int x, int y) {
            int root_x = find(x);
            int root_y = find(y);
            if(root_x == root_y) return;
            parent[root_y] = root_x;
            size[root_x] += size[root_y];
            size[root_y] = 0;
        }
    }
    private static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer tokenizer = new StringTokenizer("");
    private static String next() throws IOException{
        while(!tokenizer.hasMoreTokens()){tokenizer = new StringTokenizer(reader.readLine());}
        return tokenizer.nextToken();
    }
    public static int nextInt() throws IOException {return Integer.parseInt(next());}
    public static Long nextLong() throws IOException {return Long.parseLong(next());}
    public static double nextDouble() throws IOException {return Double.parseDouble(next());}
    public static char nextChar() throws IOException {return next().toCharArray()[0];}
    public static String nextString() throws IOException {return next();}
    public static String nextLine() throws IOException {return reader.readLine();}
}