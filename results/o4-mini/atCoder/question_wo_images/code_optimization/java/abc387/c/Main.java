import java.util.*;
import java.io.*;

public class Main {
    static int[] digits;
    static int n;
    static long[][][] dp; // pos, started(0/1), topDigit 0..9

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long L = Long.parseLong(st.nextToken());
        long R = Long.parseLong(st.nextToken());
        long ans = countSnake(R) - countSnake(L - 1);
        System.out.println(ans);
    }

    static long countSnake(long x) {
        if (x < 10) return 0;
        String s = Long.toString(x);
        n = s.length();
        digits = new int[n];
        for (int i = 0; i < n; i++) {
            digits[i] = s.charAt(i) - '0';
        }
        dp = new long[n][2][10];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 2; j++) {
                for (int k = 0; k < 10; k++) {
                    dp[i][j][k] = -1;
                }
            }
        }
        long total = dfs(0, true, false, 0);
        // subtract one-digit numbers 1..9
        total -= 9;
        return total;
    }

    static long dfs(int pos, boolean tight, boolean started, int top) {
        if (pos == n) {
            return started ? 1 : 0;
        }
        if (!tight) {
            int si = started ? 1 : 0;
            if (dp[pos][si][top] != -1) {
                return dp[pos][si][top];
            }
        }
        int limit = tight ? digits[pos] : 9;
        long res = 0;
        for (int d = 0; d <= limit; d++) {
            boolean nt = tight && (d == limit);
            if (!started) {
                if (d == 0) {
                    res += dfs(pos + 1, nt, false, 0);
                } else {
                    // first non-zero digit becomes top
                    res += dfs(pos + 1, nt, true, d);
                }
            } else {
                // already started, d must be < top
                if (d >= top) continue;
                res += dfs(pos + 1, nt, true, top);
            }
        }
        if (!tight) {
            int si = started ? 1 : 0;
            dp[pos][si][top] = res;
        }
        return res;
    }
}