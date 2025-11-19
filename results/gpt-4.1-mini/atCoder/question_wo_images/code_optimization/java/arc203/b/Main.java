import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        // Since sum of N over all test cases is at most 2*10^5,
        // we can process each test case efficiently.

        for (int t = 0; t < T; t++) {
            int n = sc.nextInt();
            int[] a = new int[n];
            int[] b = new int[n];
            int sumA = 0, sumB = 0;
            for (int i = 0; i < n; i++) {
                a[i] = sc.nextInt();
                sumA += a[i];
            }
            for (int i = 0; i < n; i++) {
                b[i] = sc.nextInt();
                sumB += b[i];
            }

            // Key insight:
            // The operation allows swapping two subarrays with equal sums.
            // Since elements are 0 or 1, sum of subarray = number of ones in it.
            // The operation can rearrange the array in a way that preserves the multiset of sub-subarrays sums.
            //
            // But more simply:
            // The total number of ones in A and B must be equal for A to be transformable into B.
            // Also, if sumA == 0 (all zeros), then A == B only if B is also all zeros.
            // If sumA == n (all ones), then A == B only if B is also all ones.
            //
            // Otherwise, since we can swap subarrays with equal sums, we can rearrange the array to any sequence with the same number of ones.
            //
            // So the answer is "Yes" if sumA == sumB, else "No".

            System.out.println(sumA == sumB ? "Yes" : "No");
        }
    }
}