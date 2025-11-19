import java.util.*;
import java.io.*;

public class Main {
    static final int mod = 998244353;
    static final char nl = '\n';
    static Scanner sc;

    static long f(long x) {
        if (x >= 0) return x % mod;
        x = Math.abs(x);
        x %= mod;
        x = (mod - x) % mod;
        return x;
    }

    static void solve(int cas) {
        int n = sc.nextInt();

        List<Integer> arr = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            arr.add(sc.nextInt());
        }

        for (int i = 1; i < n; i += 2) {
            arr.set(i, arr.get(i) * -1);
        }

        List<Long> pref = new ArrayList<>(n + 1);
        pref.add(0L);
        for (int i = 0; i < n; i++) {
            pref.add(pref.get(i) + arr.get(i));
        }

        long ans = 0;
        for (int t = 0; t < 2; t++) {
            int[] l = new int[n + 1];
            int[] r = new int[n + 1];
            Arrays.fill(l, -1);
            Arrays.fill(r, n + 1);

            List<Integer> stk = new ArrayList<>();
            for (int i = 0; i <= n; i++) {
                while (!stk.isEmpty() && pref.get(i) > pref.get(stk.get(stk.size() - 1))) {
                    r[stk.get(stk.size() - 1)] = i;
                    stk.remove(stk.size() - 1);
                }
                if (!stk.isEmpty()) {
                    l[i] = stk.get(stk.size() - 1);
                }
                stk.add(i);
            }

            for (int i = 0; i <= n; i++) {
                ans += f(pref.get(i)) * (r[i] - i) % mod * (i - l[i]) % mod;
                ans %= mod;
            }

            for (int i = 0; i <= n; i++) {
                pref.set(i, -pref.get(i));
            }
        }

        System.out.println(ans);
    }

    public static void main(String[] args) {
        sc = new Scanner(System.in);
        int tt = 1;

        if (sc.hasNextInt()) {
            tt = sc.nextInt();
        }

        for (int t = 1; t <= tt; t++) {
            solve(t);
        }

        sc.close();
    }
}
