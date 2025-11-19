import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] A = new int[n];
        for (int i = 0; i < n; i++) {
            A[i] = sc.nextInt();
        }

        // The key insight:
        // The number of distinct sequences after the operation equals:
        // 1 (original sequence) + sum over all pairs of consecutive positions (i, i+1)
        // where A[i] != A[i+1], of (n - i)
        // Because each such pair corresponds to intervals starting at i+1 that can create new sequences.

        long ans = 1; // original sequence
        for (int i = 0; i < n - 1; i++) {
            if (A[i] != A[i + 1]) {
                ans += (n - (i + 1));
            }
        }

        System.out.println(ans);
    }
}