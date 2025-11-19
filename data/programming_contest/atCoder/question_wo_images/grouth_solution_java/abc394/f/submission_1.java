import java.util.*;

public class Main {
    static List<List<Integer>> e = new ArrayList<>();
    static int ans = -1;
    static int[] dp;

    static void DFS(int now, int fa) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i : e.get(now)) {
            if (i == fa) continue;
            DFS(i, now);
            pq.add(Math.max(1, dp[i]));
            if (pq.size() > 4) pq.poll();
        }
        int[] tmp = new int[4];
        int cnt = 0;
        while (!pq.isEmpty())
            tmp[cnt++] = pq.poll();
        if (cnt == 4) {
            ans = Math.max(ans, tmp[0] + tmp[1] + tmp[2] + tmp[3] + 1);
            dp[now] = tmp[1] + tmp[2] + tmp[3] + 1;
            if (tmp[3] > 1)
                ans = Math.max(ans, tmp[3] + 1);
        }
        if (cnt == 3) {
            dp[now] = tmp[0] + tmp[1] + tmp[2] + 1;
            if (tmp[2] > 1)
                ans = Math.max(ans, tmp[2] + 1);
        }
        if (cnt == 2 && tmp[1] > 1)
            ans = Math.max(ans, tmp[1] + 1);
        if (cnt == 1 && tmp[0] > 1)
            ans = Math.max(ans, tmp[0] + 1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        dp = new int[n + 10];
        e.add(new ArrayList<>());
        for (int i = 1; i <= n; i++)
            e.add(new ArrayList<>());
        for (int i = 1; i < n; ++i) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            e.get(a).add(b);
            e.get(b).add(a);
        }
        DFS(1, 0);
        System.out.println(ans);
    }
}