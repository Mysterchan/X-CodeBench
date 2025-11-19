import java.util.*;

public class Main {
    static Scanner in = new Scanner(System.in);
    static final int N = 10;
    static StringBuilder[] a = new StringBuilder[N + 5];
    static {
        for (int i = 0; i < N; i++) {
            a[i] = new StringBuilder("");
        }
    }
    public static void main(String[] args) {
        int t = 1;
        t = in.nextInt();
        while (t-- > 0) solve();
    }
    private static void solve() {
        int n = in.nextInt(), m = in.nextInt();
        in.nextLine();
        for (int i = 0; i < n; i++) {
            a[i] = new StringBuilder(in.nextLine());
        }
        int[] st = new int[(1 << m) + 5];
        int[][] f = new int[n + 5][(1 << m) + 5];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                char c = a[i].charAt(j);
                if (c == '#') {
                    st[i] += 1 << j;
                }
            }
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < (1 << m); j++) {
                f[i][j] = Integer.MAX_VALUE;
            }
        }
        f[0][0] = 0;
        for (int i = 1; i <= n; i++) {
            int t = st[i - 1];
            for (int s1 = 0; s1 < (1 << m); s1++) {

                for (int s2 = 0; s2 < (1 << m); s2++) {
                    int s = s1 & s2;
                    if ((s & (s >> 1)) >= 1) continue;
                    f[i][s1] = Math.min(f[i][s1], f[i - 1][s2] + Integer.bitCount(t ^ s1));
                }
            }
        }
        int res = Integer.MAX_VALUE;
        for (int s = 0; s < (1 << m); s++) {
            res = Math.min(res, f[n][s]);
        }
        System.out.printf("%d\n", res);
    }
}