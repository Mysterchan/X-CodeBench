import java.util.*;
import java.io.*;

public class Main {
    static final int MOD = 998244353;
    static final int MAXN = 5005;
    static long[] factorial = new long[MAXN];
    static long[] inverseFactorial = new long[MAXN];

    static long qpow(long x, long y) {
        long res = 1;
        while (y > 0) {
            if ((y & 1) == 1) {
                res = res * x % MOD;
            }
            x = x * x % MOD;
            y >>= 1;
        }
        return res;
    }

    static long inv(long x) {
        return qpow(x, MOD - 2);
    }

    static void init() {
        factorial[0] = 1;
        for (int i = 1; i < MAXN; i++) {
            factorial[i] = factorial[i - 1] * i % MOD;
        }
        inverseFactorial[MAXN - 1] = inv(factorial[MAXN - 1]);
        for (int i = MAXN - 2; i >= 0; i--) {
            inverseFactorial[i] = inverseFactorial[i + 1] * (i + 1) % MOD;
        }
    }

    static long binomial(int n, int k) {
        if (k > n || k < 0) return 0;
        return factorial[n] * inverseFactorial[k] % MOD * inverseFactorial[n - k] % MOD;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        init();
        int n = Integer.parseInt(br.readLine());
        String s = br.readLine();
        int count = 0;
        int balance = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '(') {
                balance++;
            } else {
                balance--;
            }
            if (balance == 0) {
                count++;
            }
        }
        long ans = binomial(count, n / 2);
        ans = (ans * qpow(2, count - 1)) % MOD;
        pw.println(ans);
        pw.close();
    }
}