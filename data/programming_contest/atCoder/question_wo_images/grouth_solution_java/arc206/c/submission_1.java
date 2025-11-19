import java.util.*;

import java.io.*;

public class Main {
    static class Data implements Comparable<Data>{
        long ai;
        long bi;
        long ci;
        public Data(long ai, long bi, long ci){
            this.ai = ai;
            this.bi = bi;
            this.ci = ci;
        }
        @Override
        public int compareTo(Data p1){
            return (int)(this.bi-p1.bi);
        }
    }
    static class Node{
        int a;
        int b;
        public Node(int a, int b){
            this.a = a;
            this.b = b;
        }
    }

    public static PP.Reader cs = new PP.Reader(System.in);

    public static void main(String[] args) throws IOException{
        int tests = 1;
        while(tests>0){
            tests--;
            solve();
        }

    }
    public static long mod = 998244353;
    public static long MOD = 998244353;

    public static void solve() throws IOException{
        int n = cs.nextInt();
        long ln = (long)n;
        int[] arr = new int[n];
        for(int i=0;i<n;i++) arr[i] = cs.nextInt();
        long[][] dp = new long[n][3];
        if(n==1){
            System.out.println("1");
            return;
        }

        if(arr[0] == -1){
            dp[0][0] = 0;
            dp[0][1] = 1;
            dp[0][2] = n-1;
        }
        else{
            if(arr[0] ==2) dp[0][1] = 1;
            else dp[0][2] =  1;
        }
        for(int i=1;i<n-1;i++){
            if(arr[i] == -1){
                dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2])%mod;
                dp[i][1] = dp[i-1][1];
                dp[i][2] = (ln-2)*dp[i-1][1]%mod;
            }
            else{
                if(arr[i] == i)  dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2])%mod;
                else if(arr[i] == i+2) dp[i][1] = dp[i-1][1];
                else dp[i][2] = dp[i-1][1];
            }
        }
        if(arr[n-1]!=-1){
            if(arr[n-1] == n-1)  dp[n-1][0] = (dp[n-2][0] + dp[n-2][1] + dp[n-2][2])%mod;
            else dp[n-1][2] = dp[n-2][1];
        }
        else{
           dp[n-1][0] = (dp[n-2][0] + dp[n-2][1] + dp[n-2][2])%mod;
            dp[n-1][2] = (ln-1)*dp[n-2][1]%mod;
        }
        long ans = (dp[n-1][0]+dp[n-1][1]+dp[n-1][2])%mod;
        System.out.println(ans);

    }

    public static int getlis(ArrayList<Integer> arr){
        ArrayList<Integer> seq = new ArrayList<>();
        seq.add(arr.get(0));
        for(int i=1;i<arr.size();i++) {
            int idx = Collections.binarySearch(seq,arr.get(i));
            if(idx>=0) continue;
            idx = -idx-1;
            if(idx==seq.size()) seq.add(arr.get(i));
            else seq.set(idx,arr.get(i));
        }

        return seq.size();

    }

    public static int kth_ancestor(int[][] binpar,int node,int k){
        for(int i=0;i<21;i++){
            int bitset = (k>>i)&1;
            if(bitset ==1){
                node = binpar[i][node];
            }
            if(node == -1) return -2;
        }
        return node;
    }

    public static long gcd(long a,long b){

        long c = Math.min(a,b);
        long d = Math.max(a,b);
        if(d%c==0) return c;
        return gcd(c,d%c);
    }
    public static long divmod(long a,long b,long m){
        a = a%m;b = b%m;
        long inv =  powermod(b, m-2, m);
        return (inv*a)%m;
    }
    static long powermod(long x, long y, long p)
    {
        long res = 1;
        x = x % p;
        while (y > 0) {
            if ((y & 1) > 0)
                res = (res * x) % p;
            y = y >> 1;
            x = (x * x) % p;
        }
        return res;
    }
}

class Fenwick{

    public static long mod = 1000000000 + 7;
    long fenarr[];
    public Fenwick(int size){
        fenarr = new long[size+1];
    }
    public Fenwick(long arr[]){
        fenarr = new long[arr.length+1];
        for(int i=1;i<=arr.length;i++) update(i, arr[i-1]);
    }
    public void update(int idx,long change){
        while(idx<fenarr.length){
            fenarr[idx] = (fenarr[idx] + change)%mod;
            idx += (idx&-idx);
        }
    }

    public long prefixSum(int idx) {
        long ans = 0;
        while (idx > 0) {
            ans = (ans + fenarr[idx]) % mod;
            idx -= (idx & -idx);
        }
        return ans;
    }

    public long rangeSum(int l, int r) {
        if (l > r) return 0;
        return (prefixSum(r) - prefixSum(l - 1) + mod) % mod;
    }
}

class PP {
    static String IN = "%s";
    static String OUT = "%s";

    static class Reader {
        BufferedReader br;
        StringTokenizer st;

        Reader(InputStream is) {
            br = new BufferedReader(new InputStreamReader(is));
        }

        String next() {
            try {
                while (st == null || !st.hasMoreTokens())
                    st = new StringTokenizer(br.readLine());
                return st.nextToken();
            } catch (Exception ignored) {
            }
            return null;
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }
    }
}
class SegmentTree {
    private final int n;
    private final long[] tree;
    private final long[] arr;

    public SegmentTree(long[] input) {
        this.n = input.length;
        this.arr = new long[n];
        System.arraycopy(input, 0, this.arr, 0, n);
        this.tree = new long[4 * Math.max(1, n)];
        if (n > 0) build(1, 0, n - 1);
    }

    private void build(int node, int l, int r) {
        if (l == r) {
            tree[node] = arr[l];
            return;
        }
        int mid = l + (r - l) / 2;
        build(node << 1, l, mid);
        build(node << 1 | 1, mid + 1, r);
        tree[node] = Math.max(tree[node << 1], tree[node << 1 | 1]);
    }

    public long rangeMax(int l, int r) {

        if (l < 0 || r >= n || l > r) throw new IllegalArgumentException("Invalid query range");
        return query(1, 0, n - 1, l, r);
    }

    private long query(int node, int nl, int nr, int ql, int qr) {
        if (ql > nr || qr < nl) return Long.MIN_VALUE;
        if (ql <= nl && nr <= qr) return tree[node];
        int mid = nl + (nr - nl) / 2;
        long left = query(node << 1, nl, mid, ql, qr);
        long right = query(node << 1 | 1, mid + 1, nr, ql, qr);
        return Math.max(left, right);
    }

    public void update(int idx, long newVal) {
        if (idx < 0 || idx >= n) throw new IllegalArgumentException("Index out of bounds");
        updateNode(1, 0, n - 1, idx, newVal);
        arr[idx] = newVal;
    }

    private void updateNode(int node, int nl, int nr, int pos, long newVal) {
        if (nl == nr) {
            tree[node] = newVal;
            return;
        }
        int mid = nl + (nr - nl) / 2;
        if (pos <= mid) updateNode(node << 1, nl, mid, pos, newVal);
        else updateNode(node << 1 | 1, mid + 1, nr, pos, newVal);
        tree[node] = Math.max(tree[node << 1], tree[node << 1 | 1]);
    }

    public long get(int idx) {
        if (idx < 0 || idx >= n) throw new IllegalArgumentException("Index out of bounds");
        return arr[idx];
    }
}