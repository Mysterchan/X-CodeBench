import java.util.Scanner;

public class Main {
    static final int MOD = 998244353;
    static final int MAXN = 200005;

    static long[] fact = new long[MAXN];
    static long[] fact_inv = new long[MAXN];
    static long[] pow10 = new long[MAXN];

    static long modPow(long a, long n) {
        long res = 1;
        while (n > 0) {
            if ((n & 1) == 1) {
                res = (res * a) % MOD;
            }
            a = (a * a) % MOD;
            n >>= 1;
        }
        return res;
    }

    static void init() {
        fact[0] = 1;
        fact_inv[0] = 1;
        pow10[0] = 1;
        for (int i = 1; i < MAXN; i++) {
            fact[i] = (fact[i - 1] * i) % MOD;
            fact_inv[i] = modPow(fact[i], MOD - 2);
            pow10[i] = (pow10[i - 1] * 10) % MOD;
        }
    }

    static long getLen(int x) {
        long res = 0;
        while (x > 0) {
            res++;
            x /= 10;
        }
        return res;
    }

    public static void main(String[] args) {
        init();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        long ans = 0;
        for (int i = 1; i <= n; i++) {
            long cnt = fact[n - 1];
            long cur = (cnt * i) % MOD;
            long len = getLen(i);
            for (int j = 1; j <= n; j++) {
                if (j != i) {
                    cur = (cur + (cnt * j) % MOD * pow10[(int) (len + getLen(j))] % MOD) % MOD;
                }
            }
            ans = (ans + cur) % MOD;
        }
        System.out.println(ans);
    }
}