import java.io.*;
import java.util.*;

public class Main {
    public static int INF = 0x3f3f3f3f, mod = 1000000007, mod9 = 998244353;
    public static void main(String args[]){
        try {
            PrintWriter o = new PrintWriter(System.out);
            boolean multiTest = true;

            if(multiTest) {
                int t = nextInt(), loop = 0;
                while (loop < t) {loop++;solve(o);}
            } else solve(o);
            o.close();
        } catch (Exception e) {e.printStackTrace();}
    }
    static int n, m, res;
    static void solve(PrintWriter o) {
        try {
            n = nextInt();
            m = nextInt();
            int[][] a = new int[n][m];
            for(int i=0;i<n;i++) {
                String s = nextString();
                for(int j=0;j<m;j++) a[i][j] = s.charAt(j) == '#' ? 1 : 0;
            }
            res = n*m;
            dfs(0, 0, 0, a);
            o.println(res);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    static void dfs(int i, int j, int now, int[][] a) {
        if(j >= m-1) {
            i++;
            j = 0;
        }
        if(i >= n-1) {
            res = Math.min(res, now);
            return;
        }
        if(a[i][j] == 1 && a[i][j+1] == 1 && a[i+1][j] == 1 && a[i+1][j+1] == 1) {
            a[i][j] = 0;
            dfs(i, j+1, now+1, a);
            a[i][j] = 1;
            a[i][j+1] = 0;
            dfs(i, j+1, now+1, a);
            a[i][j+1] = 1;
            a[i+1][j] = 0;
            dfs(i, j+1, now+1, a);
            a[i+1][j] = 1;
            a[i+1][j+1] = 0;
            dfs(i, j+1, now+1, a);
            a[i+1][j+1] = 1;
        }
        else dfs(i, j+1, now, a);
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
    public static int lower_bound(long[] a, int val){
        int l = 0, r = a.length;
        while(l < r){
            int mid = l + (r - l) / 2;
            if(a[mid] < val) l = mid + 1;
            else r = mid;
        }
        return l;
    }
    public static int lower_bound(Integer[] a, int val){
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
        private void clear() {
            a = new long[n+1];
            tree = new long[n+1];
        }
    }
    static class DSU {
        int n;
        int[] parent;
        int[] size;
        public DSU(int n) {
            this.n = n;
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
        public boolean check(int x, int y) {
            int root_x = find(x);
            int root_y = find(y);
            return root_x == root_y;
        }
        public Map<Integer, List<Integer>> groups() {
            Map<Integer, List<Integer>> map = new HashMap<>();
            for(int i=0;i<n;i++) {
                int root = find(i);
                map.computeIfAbsent(root, key->new ArrayList<>()).add(i);
            }
            return map;
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