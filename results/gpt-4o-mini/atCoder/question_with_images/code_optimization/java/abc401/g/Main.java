import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long[] sx = new long[n];
        long[] sy = new long[n];
        long[] gx = new long[n];
        long[] gy = new long[n];

        for (int i = 0; i < n; i++) {
            sx[i] = sc.nextLong();
            sy[i] = sc.nextLong();
        }
        for (int i = 0; i < n; i++) {
            gx[i] = sc.nextLong();
            gy[i] = sc.nextLong();
        }
        sc.close();

        double left = 0, right = 1e18;
        while (right - left > 1e-7) {
            double mid = (left + right) / 2;
            if (canPressAllButtons(n, sx, sy, gx, gy, mid)) {
                right = mid;
            } else {
                left = mid;
            }
        }
        System.out.printf("%.12f\n", right);
    }

    private static boolean canPressAllButtons(int n, long[] sx, long[] sy, long[] gx, long[] gy, double time) {
        boolean[][] reachable = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                double distance = Math.sqrt(Math.pow(sx[i] - gx[j], 2) + Math.pow(sy[i] - gy[j], 2));
                reachable[i][j] = distance <= time;
            }
        }
        return maxBipartiteMatching(n, reachable) == n;
    }

    private static int maxBipartiteMatching(int n, boolean[][] graph) {
        int[] matchR = new int[n];
        boolean[] seen = new boolean[n];
        int result = 0;

        for (int u = 0; u < n; u++) {
            seen = new boolean[n];
            if (bipartiteMatch(u, seen, matchR, graph)) {
                result++;
            }
        }
        return result;
    }

    private static boolean bipartiteMatch(int u, boolean[] seen, int[] matchR, boolean[][] graph) {
        for (int v = 0; v < graph[0].length; v++) {
            if (graph[u][v] && !seen[v]) {
                seen[v] = true;
                if (matchR[v] < 0 || bipartiteMatch(matchR[v], seen, matchR, graph)) {
                    matchR[v] = u;
                    return true;
                }
            }
        }
        return false;
    }
}