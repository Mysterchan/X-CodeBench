import java.util.Scanner;

public class Main {
    static final long MOD = 998244353;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        String S = sc.next();
        sc.close();

        int numStates = 1 << N;
        long[][] dp = new long[M + 1][numStates];
        dp[0][0] = 1;

        int[][] lcsCols = new int[numStates][N + 1];
        for (int mask = 0; mask < numStates; mask++) {
            for (int i = 1; i <= N; i++) {
                lcsCols[mask][i] = lcsCols[mask][i - 1] + ((mask >> (i - 1)) & 1);
            }
        }

        int[][] transition = new int[numStates][26];
        for (int mask = 0; mask < numStates; mask++) {
            int[] L_old = lcsCols[mask];

            for (int c_code = 0; c_code < 26; c_code++) {
                char c = (char) ('a' + c_code);
                int[] L_new = new int[N + 1];

                for (int i = 1; i <= N; i++) {
                    if (S.charAt(i - 1) == c) {
                        L_new[i] = L_old[i - 1] + 1;
                    } else {
                        L_new[i] = Math.max(L_new[i - 1], L_old[i]);
                    }
                }

                int new_mask = 0;
                for (int i = 1; i <= N; i++) {
                    if (L_new[i] > L_new[i - 1]) {
                        new_mask |= (1 << (i - 1));
                    }
                }
                transition[mask][c_code] = new_mask;
            }
        }

        for (int m = 0; m < M; m++) {
            for (int mask = 0; mask < numStates; mask++) {
                if (dp[m][mask] == 0) continue;

                for (int c_code = 0; c_code < 26; c_code++) {
                    int new_mask = transition[mask][c_code];
                    dp[m + 1][new_mask] = (dp[m + 1][new_mask] + dp[m][mask]) % MOD;
                }
            }
        }

        long[] ans = new long[N + 1];
        for (int mask = 0; mask < numStates; mask++) {

            int k = lcsCols[mask][N];
            ans[k] = (ans[k] + dp[M][mask]) % MOD;
        }

        StringBuilder sb = new StringBuilder();
        for (int k = 0; k <= N; k++) {
            sb.append(ans[k]);
            if (k < N) {
                sb.append(" ");
            }
        }
        System.out.println(sb.toString());
    }
}