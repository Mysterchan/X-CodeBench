import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringBuilder ret = new StringBuilder();

    static int N, X;
    static int[] U, D;
    static long sum;
    static int minSum;

    public static void main(String[] args) throws Exception {
        input();
        solve();
        System.out.print(ret);
    }

    private static void input() throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());
        U = new int[N];
        D = new int[N];
        sum = 0;
        minSum = Integer.MAX_VALUE;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            U[i] = Integer.parseInt(st.nextToken());
            D[i] = Integer.parseInt(st.nextToken());
            int s = U[i] + D[i];
            sum += s;
            if (s < minSum) minSum = s;
        }
    }

    private static void solve() {
        // Binary search for maximum H such that conditions hold
        int left = 0, right = minSum + 1;
        while (left < right) {
            int mid = (left + right) >>> 1;
            if (canFit(mid)) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        // left is the first invalid H, so answer uses left-1
        long answer = sum - (long)(left - 1) * N;
        ret.append(answer).append('\n');
    }

    private static boolean canFit(int H) {
        // We want to check if there exists a sequence U' such that:
        // U'[i] + D[i] = H
        // |U'[i] - U'[i+1]| <= X
        // and U'[i] <= U[i] (since we can only reduce lengths)
        // Also U'[i] >= 0

        // We maintain feasible range of U'[i] for each i
        // For i=0:
        int low = Math.max(H - D[0], 0);
        int high = Math.min(U[0], H);

        if (low > high) return false;

        for (int i = 1; i < N; i++) {
            // For next tooth, feasible range is intersection of:
            // [max(H - D[i], 0), min(U[i], H)] and [low - X, high + X]
            int newLow = Math.max(Math.max(H - D[i], 0), low - X);
            int newHigh = Math.min(Math.min(U[i], H), high + X);

            if (newLow > newHigh) return false;

            low = newLow;
            high = newHigh;
        }
        return true;
    }
}