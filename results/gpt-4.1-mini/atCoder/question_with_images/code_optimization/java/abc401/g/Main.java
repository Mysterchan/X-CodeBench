import java.util.Scanner;

public class Main {
    static int N;
    static long[] sx, sy, gx, gy;
    static double[][] dist;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        sx = new long[N];
        sy = new long[N];
        gx = new long[N];
        gy = new long[N];
        for (int i = 0; i < N; i++) {
            sx[i] = sc.nextLong();
            sy[i] = sc.nextLong();
        }
        for (int i = 0; i < N; i++) {
            gx[i] = sc.nextLong();
            gy[i] = sc.nextLong();
        }
        sc.close();

        dist = new double[N][N];
        double maxDist = 0;
        for (int i = 0; i < N; i++) {
            long sx_i = sx[i];
            long sy_i = sy[i];
            for (int j = 0; j < N; j++) {
                long dx = sx_i - gx[j];
                long dy = sy_i - gy[j];
                dist[i][j] = Math.sqrt((double) dx * dx + (double) dy * dy);
                if (dist[i][j] > maxDist) maxDist = dist[i][j];
            }
        }

        double left = 0, right = maxDist;
        for (int iter = 0; iter < 60; iter++) {
            double mid = (left + right) * 0.5;
            if (canAssign(mid)) {
                right = mid;
            } else {
                left = mid;
            }
        }

        System.out.printf("%.12f\n", right);
    }

    // Check if there exists a perfect matching where dist[i][j] <= time
    static boolean canAssign(double time) {
        // Build graph: edges from person i to button j if dist[i][j] <= time
        // Use Hungarian algorithm for maximum bipartite matching
        int[] matchR = new int[N];
        for (int i = 0; i < N; i++) matchR[i] = -1;

        for (int u = 0; u < N; u++) {
            boolean[] seen = new boolean[N];
            if (!bipartiteMatch(u, seen, matchR, time)) {
                return false;
            }
        }
        return true;
    }

    static boolean bipartiteMatch(int u, boolean[] seen, int[] matchR, double time) {
        for (int v = 0; v < N; v++) {
            if (!seen[v] && dist[u][v] <= time) {
                seen[v] = true;
                if (matchR[v] < 0 || bipartiteMatch(matchR[v], seen, matchR, time)) {
                    matchR[v] = u;
                    return true;
                }
            }
        }
        return false;
    }
}