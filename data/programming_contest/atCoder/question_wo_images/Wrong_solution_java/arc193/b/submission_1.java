import java.util.*;
import java.io.*;

public class Main {
    static final int MOD = 998244353;
    static final int MAXN = 1000005;

    static int[] fact = new int[MAXN];
    static int[] inv = new int[MAXN];

    static int add(int x, int y) {
        x += y;
        if (x >= MOD) x -= MOD;
        return x;
    }

    static int sub(int x, int y) {
        x -= y;
        if (x < 0) x += MOD;
        return x;
    }

    static int mul(int x, int y) {
        return (int)((long)x * y % MOD);
    }

    static int binpow(int x, int y) {
        int z = 1;
        while (y > 0) {
            if (y % 2 == 1) z = mul(z, x);
            x = mul(x, x);
            y /= 2;
        }
        return z;
    }

    static int inv(int x) {
        return binpow(x, MOD - 2);
    }

    static void precalc() {
        fact[0] = 1;
        for (int i = 1; i < MAXN; i++) {
            fact[i] = mul(fact[i - 1], i);
        }
        inv[MAXN - 1] = inv(fact[MAXN - 1]);
        for (int i = MAXN - 2; i >= 0; i--) {
            inv[i] = mul(inv[i + 1], i + 1);
        }
    }

    static int C(int n, int k) {
        if (k < 0 || k > n) return 0;
        return mul(fact[n], mul(inv[k], inv[n - k]));
    }

    public static void main(String[] args) throws IOException {
        precalc();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        int n = Integer.parseInt(br.readLine());
        String s = br.readLine();
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '1') cnt++;
        }
        if (cnt == 0) {
            pw.println(mul(fact[n - 1], 2));
            pw.close();
            return;
        }
        if (cnt == 1) {
            pw.println(add(mul(fact[n - 1], 2), mul(sub(fact[n - 2], 1), n - 1)));
            pw.close();
            return;
        }
        if (cnt == n) {
            pw.println(add(mul(fact[n - 1], 2), sub(mul(fact[n - 2], n - 1), 1)));
            pw.close();
            return;
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int cur = mul(mul(mul(fact[n - cnt - 1], C(n - 2, i - 1)), C(cnt - 1, i - 1)), binpow(2, n - 1 - i));
            ans = add(ans, cur);
        }
        pw.println(ans);
        pw.close();
    }
}