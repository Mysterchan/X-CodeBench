import java.util.Scanner;

public class Main {
    static long[] A;
    static int N;

    static boolean check(int K) {

        if (K == 0) {
            return true;
        }

        for (int i = 0; i < K; i++) {
            long topSize = A[i];
            long bottomSize = A[N - K + i];

            if (2L * topSize > bottomSize) {

                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        A = new long[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextLong();
        }

        int low = 0;
        int high = N / 2;
        int ans = 0;

        while (low <= high) {
            int midK = low + (high - low) / 2;

            if (check(midK)) {

                ans = midK;
                low = midK + 1;
            } else {

                high = midK - 1;
            }
        }

        System.out.println(ans);
        sc.close();
    }
}