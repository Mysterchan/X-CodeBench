import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int N, X;
    private static long[] U, D;

    public static void main(String[] args) throws Exception {
        setInput();
        System.out.print(solve());
    }

    private static void setInput() throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());
        U = new long[N];
        D = new long[N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            U[i] = Long.parseLong(st.nextToken());
            D[i] = Long.parseLong(st.nextToken());
        }
    }

    private static long solve() {
        long totalSum = 0;
        long minH = Long.MAX_VALUE;

        for (int i = 0; i < N; i++) {
            totalSum += U[i] + D[i];
            minH = Math.min(minH, U[i] + D[i]);
        }

        long left = 0, right = minH + 1;
        while (left < right) {
            long mid = (left + right) / 2;
            if (!canFit(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return totalSum - (long) (right - 1) * N;
    }

    private static boolean canFit(long h) {
        long upper = U[0];
        long lower = Math.max(h - D[0], 0);

        for (int i = 1; i < N; i++) {
            upper = Math.min(U[i], upper + X);
            lower = Math.max(h - D[i], lower - X);
            lower = Math.max(lower, 0);
            if (lower > upper) {
                return false;
            }
        }
        return true;
    }
}