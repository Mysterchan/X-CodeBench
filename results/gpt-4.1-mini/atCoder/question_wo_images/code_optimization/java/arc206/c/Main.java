import java.util.*;

public class Main {
    static final int MOD = 998244353;
    static int N;
    static int[] A;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }

        // dp[i][0]: number of ways for prefix i where A[i] is fixed (no choice)
        // dp[i][1]: number of ways for prefix i where A[i] is -1 (choice)
        // Actually, we only need dp[i]: number of ways for prefix i
        // The problem reduces to counting sequences where for each i:
        // A[i] in [1,N], and for all i, A[i] in [i, N] (due to the problem's condition)
        // But from the editorial and problem analysis:
        // The condition implies A[i] >= i for all i.
        // For fixed A[i] != -1, if A[i] < i, answer is 0.
        // For A[i] == -1, number of choices = N - i + 1 (values from i to N)
        // Total ways = product over i of (1 if fixed else N - i + 1)

        long result = 1;
        for (int i = 0; i < N; i++) {
            if (A[i] != -1) {
                if (A[i] < i + 1) {
                    // No valid sequences if A[i] < i+1
                    System.out.println(0);
                    return;
                }
            } else {
                // choices from i+1 to N inclusive
                result = (result * (N - i)) % MOD;
            }
        }

        System.out.println(result);
    }
}