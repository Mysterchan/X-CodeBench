import java.util.*;

public class Main {

    static final int S = 100005;
    static long[] a = new long[S];
    static long[] d = new long[S];
    static long n;

    static boolean check(long ans) {
        Arrays.fill(d, 0, (int)n, 0);
        long acc = 0;

        for (long i = 0; i < n; ++i) {
            acc -= d[(int)i];

            long need = Math.max(0L, i - (n - ans));
            if (acc < need) return false;

            long end = i + a[(int)i] + (acc++) - need + 1;
            if (end < n) ++d[(int)end];
        }

        return true;
    }

    static void solve(Scanner sc) {
        n = sc.nextLong();
        for (int i = 0; i < n; ++i) a[i] = sc.nextLong();

        long le = 1, ri = n + 1, mid;
        while (ri - le > 1) {
            mid = (le + ri) / 2;
            if (check(mid)) le = mid;
            else ri = mid;
        }

        System.out.println(le);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long tc = sc.nextLong();
        while (tc-- > 0) solve(sc);
    }
}
