import java.util.Scanner;

public class Main {

    static int N;
    static long X;
    static long[] U;
    static long[] D;

    static boolean check(long H) {

        long l = Math.max(0, H - D[0]);
        long r = Math.min(U[0], H);

        if (l > r) {
            return false;
        }

        for (int i = 1; i < N; i++) {

            long L_i = Math.max(0, H - D[i]);
            long R_i = Math.min(U[i], H);

            if (L_i > R_i) {
                return false;
            }

            long L_soft = l - X;
            long R_soft = r + X;

            long l_new = Math.max(L_i, L_soft);
            long r_new = Math.min(R_i, R_soft);

            if (l_new > r_new) {
                return false;
            }

            l = l_new;
            r = r_new;
        }

        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        X = sc.nextLong();

        U = new long[N];
        D = new long[N];

        long totalSum = 0;
        long maxH = Long.MAX_VALUE;

        for (int i = 0; i < N; i++) {
            U[i] = sc.nextLong();
            D[i] = sc.nextLong();
            long s_i = U[i] + D[i];
            totalSum += s_i;
            maxH = Math.min(maxH, s_i);
        }
        sc.close();

        long low = 0;
        long high = maxH;
        long ansH = 0;

        while (low <= high) {
            long midH = low + (high - low) / 2;
            if (check(midH)) {

                ansH = midH;
                low = midH + 1;
            } else {

                high = midH - 1;
            }
        }

        long minCost = totalSum - N * ansH;
        System.out.println(minCost);
    }
}