import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static long[] sx, sy, gx, gy;
    static List<Integer>[] adj;
    static int[] matchR;
    static boolean[] seen;

    static boolean bpm(int u) {
        for (int v : adj[u]) {
            if (!seen[v]) {
                seen[v] = true;
                if (matchR[v] < 0 || bpm(matchR[v])) {
                    matchR[v] = u;
                    return true;
                }
            }
        }
        return false;
    }

    static boolean can(double t) {
        adj = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            adj[i] = new ArrayList<>();
            for (int j = 0; j < N; j++) {
                double dx = sx[i] - gx[j];
                double dy = sy[i] - gy[j];
                if (dx*dx + dy*dy <= t*t + 1e-12) {
                    adj[i].add(j);
                }
            }
        }
        matchR = new int[N];
        Arrays.fill(matchR, -1);
        int result = 0;
        for (int u = 0; u < N; u++) {
            seen = new boolean[N];
            if (bpm(u)) result++;
            else break;
        }
        return result == N;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        sx = new long[N]; sy = new long[N];
        gx = new long[N]; gy = new long[N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            sx[i] = Long.parseLong(st.nextToken());
            sy[i] = Long.parseLong(st.nextToken());
        }
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            gx[i] = Long.parseLong(st.nextToken());
            gy[i] = Long.parseLong(st.nextToken());
        }

        double lo = 0, hi = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                double dx = sx[i] - gx[j];
                double dy = sy[i] - gy[j];
                hi = Math.max(hi, Math.hypot(dx, dy));
            }
        }
        for (int iter = 0; iter < 60; iter++) {
            double mid = (lo + hi) / 2;
            if (can(mid)) hi = mid;
            else lo = mid;
        }
        System.out.printf("%.10f\n", hi);
    }
}