import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;
import java.util.Stack;
import java.util.HashMap;

public class Main {
    final static int mod = 998244353;
    static int[] fc;
    static int[] ifc;
    static int qpow(int a, int b) {
        int ret = 1;
        for (; b > 0; a = (int)(1l * a * a % mod), b >>= 1) if (b % 2 != 0) {
            ret = (int)(1l * ret * a % mod);
        }
        return ret;
    }
    static ArrayList<Integer>[] adj;
    static int[] dp;
    static long[] h;
    static long mask;
    static long shift(long x) {
        x ^= mask;
        x ^= x << 13;
        x ^= x >> 7;
        x ^= x << 17;
        x ^= mask;
        return x;
    }
    static void dfs(int u) {
        h[u] = 1;
        dp[u] = fc[adj[u].size()];
        HashMap<Long, Integer> mp = new HashMap();
        for (var v : adj[u]) {
            dfs(v);
            h[u] += shift(h[v]);
            dp[u] = (int)(1l * dp[u] * dp[v] % mod);
            if (mp.containsKey(h[v])) {
                mp.compute(h[v], (key, value) -> value + 1);
            } else {
                mp.put(h[v], 1);
            }
        }
        int sum = 0;
        for (int cnt : mp.values()) sum += cnt;
        if (sum != adj[u].size()){
            System.out.println(-1);
        }
        for (var t : mp.values()) {
            dp[u] = (int)(1l * dp[u] * ifc[t] % mod);
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String s = sc.next();
        ArrayList<Integer> fa = new ArrayList();
        Stack<Integer> stk = new Stack();
        fa.add(-1);
        stk.push(0);
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '(') {
                fa.add(stk.peek());
                stk.push(fa.size() - 1);
            } else stk.pop();
        }
        int tot = fa.size() - 1;
        adj = new ArrayList[tot + 1];
        for (int u = 0; u <= tot; u++) adj[u] = new ArrayList();
        dp = new int[tot + 1];
        h = new long[tot + 1];
        for (int u = 1; u <= tot; u++) {
            int p = fa.get(u);
            adj[p].add(u);
        }
        Random random = new Random();
        mask = random.nextLong();
        fc = new int[tot + 1];
        ifc = new int[tot + 1];
        fc[0] = ifc[0] = 1;
        for (int i = 1; i <= tot; i++) {
            fc[i] = (int)(1l * i * fc[i - 1] % mod);
            ifc[i] = qpow(fc[i], mod - 2);
        }
        dfs(0);
        System.out.println(dp[0]);
    }
}