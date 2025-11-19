import java.util.*;

public class Main {
    static final int MOD = 998244353;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String s = sc.next();

        if (!isValid(s, n)) {
            System.out.println(0);
            return;
        }

        long[] fact = new long[2 * n + 1];
        long[] inv = new long[2 * n + 1];
        fact[0] = inv[0] = 1;
        for (int i = 1; i <= 2 * n; i++) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        inv[2 * n] = modInverse(fact[2 * n]);
        for (int i = 2 * n - 1; i >= 1; i--) {
            inv[i] = inv[i + 1] * (i + 1) % MOD;
        }

        int open = 0;
        long res = 1;
        for (char c : s.toCharArray()) {
            if (c == 'W') {
                open++;
            } else {
                res = res * open % MOD;
                open--;
            }
        }

        System.out.println(res);
    }

    private static boolean isValid(String s, int n) {
        int w = 0, b = 0;
        for (char c : s.toCharArray()) {
            if (c == 'W') w++;
            else b++;
        }
        return w == n && b == n;
    }

    private static long modInverse(long x) {
        return power(x, MOD - 2);
    }

    private static long power(long x, long y) {
        long res = 1;
        x %= MOD;
        while (y > 0) {
            if ((y & 1) == 1) res = res * x % MOD;
            x = x * x % MOD;
            y >>= 1;
        }
        return res;
    }
}