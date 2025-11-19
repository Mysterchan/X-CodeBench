import java.util.*;

public class Main{
    static long K;
    static int n;
    static long[] p;
    static long[] delay;
    static int[] d;
    static boolean[] exit;
    static boolean[] vis;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int c = scanner.nextInt();
        for (int caseNum = 0; caseNum < c; caseNum++) {
            go(scanner);
        }
        scanner.close();
    }

    static void go(Scanner scanner) {
        n = scanner.nextInt();
        K = scanner.nextLong();
        p = new long[n];
        for (int i = 0; i < n; i++) {
            p[i] = scanner.nextLong();
        }
        delay = new long[n];
        for (int i = 0; i < n; i++) {
            delay[i] = scanner.nextLong();
        }
        int qn = scanner.nextInt();
        long[] q = new long[qn];
        for (int i = 0; i < qn; i++) {
            q[i] = scanner.nextLong();
        }


        d = new int[2 * n];
        Arrays.fill(d, -1);


        long[] a = new long[n];
        for (int i = 0; i < n; i++) {
            a[i] = ((p[i] - delay[i]) % K + K) % K;
        }
        Map<Long, Integer> idx = new HashMap<>();
        for (int i = n - 1; i >= 0; i--) {
            if (idx.containsKey(a[i])) {
                d[i] = idx.get(a[i]) + n;
            }
            idx.put(a[i], i);
        }

        long[] b = new long[n];
        for (int i = 0; i < n; i++) {
            b[i] = (p[i] + delay[i]) % K;
        }
        idx.clear();
        for (int i = 0; i < n; i++) {
            if (idx.containsKey(b[i])) {
                d[i + n] = idx.get(b[i]);
            }
            idx.put(b[i], i);
        }

        exit = new boolean[2 * n];
        vis = new boolean[2 * n];
        for (int i = 0; i < 2 * n; i++) {
            dfs(i);
        }

        Query[] q2 = new Query[qn];
        for (int i = 0; i < qn; i++) {
            q2[i] = new Query(q[i], i);
        }
        Arrays.sort(q2, (x, y) -> Long.compare(y.pos, x.pos));

        boolean[] res = new boolean[qn];
        Arrays.fill(res, true);
        int ai = n - 1;
        idx.clear();
        for (Query t : q2) {
            while (ai >= 0 && p[ai] >= t.pos) {
                idx.put(a[ai], ai);
                ai--;
            }
            if (!idx.containsKey(t.pos % K)) {
                res[t.idx] = true;
            } else {
                res[t.idx] = exit[idx.get(t.pos % K) + n];
            }
        }

        for (boolean x : res) {
            System.out.println(x ? "YES" : "NO");
        }
    }

    static boolean dfs(int x) {
        if (x == -1) return true;
        if (vis[x]) return exit[x];
        vis[x] = true;
        exit[x] = dfs(d[x]);
        return exit[x];
    }

    static class Query {
        long pos;
        int idx;

        Query(long pos, int idx) {
            this.pos = pos;
            this.idx = idx;
        }
    }
}
