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

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.close();

        long[] fact = new long[N + 1];
        fact[0] = 1;
        for (int i = 1; i <= N; i++) {
            fact[i] = (fact[i - 1] * i) % MOD;
        }

        long totalSum = 0;
        long multiplier = 1;

        for (int i = 1; i <= N; i++) {
            totalSum = (totalSum + (multiplier * fact[N - 1]) % MOD * i) % MOD;
            multiplier = (multiplier * 10 + 1) % MOD;
        }

        totalSum = (totalSum * fact[N]) % MOD;
        System.out.println(totalSum);
    }
}