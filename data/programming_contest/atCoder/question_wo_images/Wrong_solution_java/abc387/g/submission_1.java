import java.util.Scanner;

public class Main {
    static final int N = 250000;
    static final int MD = 998244353;

    static int[] vv = new int[N + 1];
    static int[] ff = new int[N + 1];
    static int[] gg = new int[N + 1];
    static int[] hh = new int[N + 1];

    public static void init() {
        ff[0] = gg[0] = 1;
        hh[0] = 0;
        for (int i = 1; i <= N; i++) {
            vv[i] = i == 1 ? 1 : (int) ((long) vv[i - MD % i] * (MD / i + 1) % MD);
            ff[i] = (int) ((long) ff[i - 1] * i % MD);
            gg[i] = (int) ((long) gg[i - 1] * vv[i] % MD);
            hh[i] = (hh[i - 1] + vv[i]) % MD;
        }
    }

    public static int choose(int n, int k) {
        return k < 0 || k > n ? 0 : (int) ((long) ff[n] * gg[k] % MD * gg[n - k] % MD);
    }

    public static int match(int n) {
        return n == 0 ? 1 : (int) ((long) ff[n] * ff[n - 1] % MD);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        init();

        int ans = 0;
        for (int k = 1; k <= n; k++)
            ans = (ans + (int) ((long) (k % 2 == 0 ? -1 : 1) * choose(n, k) * match(k) % MD * ff[n - k] % MD)) % MD;
        if (ans < 0)
            ans += MD;
        System.out.println(ans);
    }
}