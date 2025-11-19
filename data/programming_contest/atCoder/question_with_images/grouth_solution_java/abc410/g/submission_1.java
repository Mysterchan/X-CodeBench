import java.io.*;
import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public class FenwickTree {
        private int[] tree;
        private int size;

        public FenwickTree(int size) {
            this.size = size;
            this.tree = new int[size + 1];
        }

        private int lowbit(int x) {
            return x & (-x);
        }
        public void update(int i, int val) {
            while (i <= size) {
                tree[i] = Math.max(tree[i], val);
                i += lowbit(i);
            }
        }
        public int query(int i) {
            int res = 0;
            while (i > 0) {
                res = Math.max(res,tree[i]);
                i -= lowbit(i);
            }
            return res;
        }
    }

    static int[][] edges;

    public static void main(String[] args) {
        Main main = new Main();
        main.solve();
        out.flush();
    }

    public void solve(){
        int n = in.nextInt();
        edges = new int[n][2];
        for (int i = 0; i < n; i++) {
            edges[i][0] = in.nextInt();
            edges[i][1] = in.nextInt();
            if(edges[i][0]>edges[i][1]) {
                int tmp = edges[i][0];
                edges[i][0] = edges[i][1];
                edges[i][1] = tmp;
            }
        }
        Arrays.sort(edges,(a,b)->a[1]-b[1]);
        FenwickTree tree = new FenwickTree(2*n+5);
        int[] dp = new int[n];
        for (int i = 0; i < n; i++) {
            int l = edges[i][0];
            int len = tree.query(2*n-l+1);
            dp[i] = len+1;
            tree.update(2*n-l+1, dp[i]);
        }

        int ans  = 1;
        FenwickTree ansTree = new FenwickTree(2*n+5);
        for (int i = 0; i < n; i++) {
            int r = edges[i][1];
            int l = edges[i][0];
            ans = Math.max(ans,dp[i]+ansTree.query(l));
            ansTree.update(r,dp[i]);
        }
        out.println(ans);
    }

    static FastReader in = new FastReader();
    static PrintWriter out=new PrintWriter(System.out);
    static class FastReader{
        static BufferedReader  br;
        static StringTokenizer st;
        FastReader(){
            br=new BufferedReader(new InputStreamReader(System.in));
        }
        String next(){
            String str="";
            while(st==null||!st.hasMoreElements()){
                try {
                    str=br.readLine();
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
                st=new StringTokenizer(str);
            }
            return st.nextToken();
        }
        int nextInt(){
            return Integer.parseInt(next());
        }
    }
}