import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        StringBuilder sb = new StringBuilder();

        while (T-- > 0) {
            int N = sc.nextInt();
            long[] A = new long[N];
            long[] B = new long[N];
            long[] C = new long[N];
            long[] D = new long[N];
            long[] E = new long[N];

            for (int i = 0; i < N; i++) {
                A[i] = sc.nextLong();
                B[i] = sc.nextLong();
                C[i] = sc.nextLong();
                D[i] = sc.nextLong();
                E[i] = sc.nextLong();
            }

            long sumA = 0, sumB = 0, sumC = 0, sumD = 0, sumE = 0;

            for (int i = 0; i < N; i++) {
                sumA += A[i];
                sumB += B[i];
                sumC += C[i];
                sumD += D[i];
                sumE += E[i];

                long lo = 0, hi = (long) 1e10, ans = 0;
                while (lo <= hi) {
                    long mid = (lo + hi) / 2;

                    if (sumA >= mid &&
                        sumB >= 2 * mid &&
                        sumC >= 3 * mid &&
                        sumD >= 2 * mid &&
                        sumE >= mid) {
                        ans = mid;
                        lo = mid + 1;
                    } else {
                        hi = mid - 1;
                    }
                }

                sb.append(ans).append(" ");
            }
            sb.append("\n");
        }

        System.out.print(sb);
    }
}