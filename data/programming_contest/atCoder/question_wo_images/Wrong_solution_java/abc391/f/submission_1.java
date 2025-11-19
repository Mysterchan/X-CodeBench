import java.util.*;

public class Main {
    static Scanner in = new Scanner(System.in);
    static int n, K;
    private static long cal(int i, int j, int k) {
        return (long) i * n * n + j * n + k;
    }
    private static void solve() {
        n = in.nextInt(); K = in.nextInt();
        Integer[] a = new Integer[n], b = new Integer[n], c = new Integer[n];
        for (int i = 0; i < n; i++) {
            a[i] = in.nextInt();
        }
        for (int i = 0; i < n; i++) {
            b[i] = in.nextInt();
        }
        for (int i = 0; i < n; i++) {
            c[i] = in.nextInt();
        }
        Arrays.sort(a, 0, n, (e1, e2)-> e2 - e1);
        Arrays.sort(b, 0, n, (e1, e2)-> e2 - e1);
        Arrays.sort(c, 0, n, (e1, e2)-> e2 - e1);
        PriorityQueue<long[]> hq = new PriorityQueue<>((e1, e2) -> Long.compare(e2[0], e1[0]));
        HashSet<Long> S = new HashSet<>();
        long val = (long) a[0] * b[0] +  b[0] * c[0] +  c[0] * a[0];
        hq.add(new long[]{val, 0, 0, 0});
        long res = val;
        S.add(0L);

        while (K-- > 0 && !hq.isEmpty()) {
            long[] e = hq.poll();
            int i = (int) e[1],  j = (int) e[2], k = (int) e[3];
            res = e[0];
            if (i + 1 < n) {
                int ii = i+1, jj = j, kk = k;
                long v = (long) a[ii] * b[jj] +  b[jj] * c[kk] +  c[kk] * a[ii];
                long idx = cal(ii, jj, kk);
                if (S.add(idx)) {
                    hq.add(new long[]{v, ii, jj, kk});
                }
            }
            if (j + 1 < n) {
                int ii = i, jj = j+1, kk = k;
                long v = (long) a[ii] * b[jj] +  b[jj] * c[kk] +  c[kk] * a[ii];
                long idx = cal(ii, jj, kk);
                if (S.add(idx)) {
                    hq.add(new long[]{v, ii, jj, kk});
                }
            }
            if (k + 1 < n) {
                int ii = i, jj = j, kk = k+1;
                long v = (long) a[ii] * b[jj] +  b[jj] * c[kk] +  c[kk] * a[ii];
                long idx = cal(ii, jj, kk);
                if (S.add(idx)) {
                    hq.add(new long[]{v, ii, jj, kk});
                }
            }
        }
        System.out.printf("%d\n", res);

    }

    public static void main(String[] args) {

        int t = 1;
        while (t-- != 0) {
            solve();
        }
    }
}