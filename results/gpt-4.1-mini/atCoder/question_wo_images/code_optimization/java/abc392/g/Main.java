import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int[] S = new int[N];
        int maxVal = 0;
        for (int i = 0; i < N; i++) {
            S[i] = sc.nextInt();
            if (S[i] > maxVal) maxVal = S[i];
        }
        sc.close();

        boolean[] exists = new boolean[maxVal + 1];
        for (int val : S) {
            exists[val] = true;
        }

        // Sort the array to process in ascending order
        java.util.Arrays.sort(S);

        long count = 0;

        // For each B in S, check for fine triplets (A, B, C)
        // where A = B - d and C = B + d, d > 0
        // Both A and C must be in S.
        for (int bIdx = 0; bIdx < N; bIdx++) {
            int B = S[bIdx];
            // d can be at most min(B - 1, maxVal - B)
            int maxD = Math.min(B - 1, maxVal - B);
            for (int d = 1; d <= maxD; d++) {
                int A = B - d;
                int C = B + d;
                if (exists[A] && exists[C]) {
                    count++;
                }
            }
        }

        System.out.println(count);
    }
}