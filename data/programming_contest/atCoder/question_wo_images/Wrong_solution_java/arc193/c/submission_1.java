import java.util.Scanner;

public class Main {
    static final int MOD = 998244353;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int h = scanner.nextInt();
        int w = scanner.nextInt();
        int c = scanner.nextInt();

        if (h == 1 && w == 1) {
            System.out.println(c % MOD);
        } else if (h == 1 || w == 1) {
            System.out.println((long) c * (c - 1) % MOD);
        } else {
            long ans = powMod(c, h + w - 2, MOD) * (c - 1) % MOD * (c - 1) % MOD;
            ans = (ans + powMod(c, h - 1, MOD) * (c - 1)) % MOD;
            ans = (ans + powMod(c, w - 1, MOD) * (c - 1)) % MOD;
            ans = (ans + 1) % MOD;
            System.out.println(ans);
        }
    }

    public static long powMod(long a, long b, int mod) {
        long res = 1;
        while (b > 0) {
            if ((b & 1) == 1) {
                res = res * a % mod;
            }
            a = a * a % mod;
            b >>= 1;
        }
        return res;
    }
}