import java.util.Scanner;

public class Main {
    static long P;
    static long[][] C;

    static long add(long a, long b) { return (a + b) % P; }
    static long sub(long a, long b) { return (a - b + P) % P; }
    static long mul(long a, long b) { return (a * b) % P; }

    static void precomputeCombs(int n) {
        C = new long[n + 1][n + 1];
        for (int i = 0; i <= n; i++) {
            C[i][0] = 1;
            for (int j = 1; j <= i; j++) {
                C[i][j] = add(C[i - 1][j - 1], C[i - 1][j]);
            }
        }
    }

    static long getComb(int n, int k) {
        if (k < 0 || k > n) return 0;
        return C[n][k];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        P = sc.nextLong();

        int n = N / 2;
        int M_max = N * (N - 1) / 2;

        precomputeCombs(M_max);

        long[][][] T = new long[n + 1][n + 1][M_max + 1];

        long[][][] C_dp = new long[n + 1][n + 1][M_max + 1];

        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                long max_kb = (long)i * j;
                long max_ko = (long)j * (j - 1) / 2;

                for (int k = 0; k <= M_max; k++) {
                    long total_k = 0;

                    for (int kb = 0; kb <= k; kb++) {
                        int ko = k - kb;
                        if (kb > max_kb || ko > max_ko) continue;
                        total_k = add(total_k, mul(getComb((int)max_kb, kb), getComb((int)max_ko, ko)));
                    }
                    T[i][j][k] = total_k;
                }
            }
        }

        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0 && j == 0) continue;

                for (int k = 0; k <= M_max; k++) {

                    C_dp[i][j][k] = T[i][j][k];

                    for (int ic = 1; ic <= i; ic++) {
                        for (int jc = 0; jc <= j; jc++) {
                            if (ic == i && jc == j) continue;

                            int ir = i - ic;
                            int jr = j - jc;

                            long coeff = mul(getComb(i - 1, ic - 1), getComb(j, jc));
                            if (coeff == 0) continue;

                            long R_k = 0;
                            for (int kc = 0; kc <= k; kc++) {
                                R_k = add(R_k, mul(C_dp[ic][jc][kc], T[ir][jr][k - kc]));
                            }

                            C_dp[i][j][k] = sub(C_dp[i][j][k], mul(coeff, R_k));
                        }
                    }
                }
            }
        }

        long numPartitions = getComb(N - 1, n - 1);
        StringBuilder sb = new StringBuilder();

        for (int M = N - 1; M <= M_max; M++) {

            long ans = mul(C_dp[n][n][M], numPartitions);
            sb.append(ans);
            if (M < M_max) {
                sb.append(" ");
            }
        }
        System.out.println(sb.toString());
        sc.close();
    }
}