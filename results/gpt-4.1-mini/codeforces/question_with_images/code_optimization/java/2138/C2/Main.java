import java.util.*;

public class Main {
    static List<List<Integer>> al;
    static int[] lvlCnt;
    static int h;

    static int f(int u) {
        if (al.get(u).isEmpty()) return 1;
        int mn = Integer.MAX_VALUE;
        for (int v : al.get(u)) mn = Math.min(mn, f(v));
        return mn + 1;
    }

    static void dfs(int u, int d) {
        lvlCnt[d]++;
        for (int v : al.get(u)) dfs(v, d + 1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        StringBuilder sb = new StringBuilder();
        while (T-- > 0) {
            int n = sc.nextInt(), k = sc.nextInt();
            al = new ArrayList<>();
            for (int i = 0; i <= n; i++) al.add(new ArrayList<>());
            for (int i = 2; i <= n; i++) {
                int p = sc.nextInt();
                al.get(p).add(i);
            }

            lvlCnt = new int[n + 1];
            dfs(1, 0);

            h = f(1);

            int z = k, o = n - k;
            int ans = 0;

            // Greedy approach:
            // For each level i, we can assign either all zeros or all ones to the nodes at that level.
            // We want to maximize the length of the longest common subsequence of all leaves,
            // which is the maximum number of levels we can assign a label to, such that
            // the total zeros assigned <= z and total ones assigned <= o.
            //
            // At each level, we try to assign zeros if possible (if z >= lvlCnt[i]),
            // else assign ones if possible (if o >= lvlCnt[i]),
            // else stop because we cannot assign that level.
            //
            // The answer is the number of levels assigned.

            for (int i = 0; i < h; i++) {
                int c = lvlCnt[i];
                if (z >= c) {
                    z -= c;
                    ans++;
                } else if (o >= c) {
                    o -= c;
                    ans++;
                } else {
                    break;
                }
            }

            sb.append(ans).append('\n');
        }
        System.out.print(sb);
    }
}