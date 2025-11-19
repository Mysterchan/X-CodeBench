import java.util.Scanner;

public class Main {
    static final long MOD = 998244353;

    static long pow(long base, long exp) {
        long res = 1;
        base %= MOD;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * base) % MOD;
            base = (base * base) % MOD;
            exp /= 2;
        }
        return res;
    }

    static long modInverse(long n) {
        return pow(n, MOD - 2);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.close();

        long[] fact = new long[N + 1];
        fact[0] = 1;
        for (int i = 1; i <= N; i++) {
            fact[i] = (fact[i - 1] * i) % MOD;
        }

        long[] L = new long[N + 1];
        long[] W = new long[N + 1];
        long[] invW = new long[N + 1];

        for (int k = 1; k <= N; k++) {
            L[k] = String.valueOf(k).length();
            W[k] = pow(10, L[k]);
            invW[k] = modInverse(W[k]);
        }

        long[] c = new long[N + 1];
        c[0] = 1;
        for (int i = 1; i <= N; i++) {

            for (int j = i; j >= 1; j--) {

                c[j] = (c[j - 1] + c[j] * W[i]) % MOD;
            }
            c[0] = (c[0] * W[i]) % MOD;
        }

        long totalSum = 0;

        for (int k = 1; k <= N; k++) {

            long[] d = new long[N];
            long d_prev = 0;

            for (int i = 0; i < N; i++) {
                d[i] = (c[i] - d_prev + MOD) % MOD;
                d[i] = (d[i] * invW[k]) % MOD;
                d_prev = d[i];
            }

            for (int j = 1; j <= N; j++) {

                long E_m = d[j - 1];

                long term = (k * fact[j - 1]) % MOD;
                term = (term * fact[N - j]) % MOD;
                term = (term * E_m) % MOD;

                totalSum = (totalSum + term) % MOD;
            }
        }

        System.out.println(totalSum);
    }
}