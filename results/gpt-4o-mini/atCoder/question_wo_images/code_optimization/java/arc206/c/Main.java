import java.util.*;

public class Main {
    static final int MOD = 998244353;
    static int N;
    static int[] A;
    static boolean[] isSet;
    static int[] counts;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        A = new int[N];
        isSet = new boolean[N + 1];
        counts = new int[N + 1];

        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
            if (A[i] > 0) {
                isSet[A[i]] = true; // Mark this number as used
            }
        }

        // Count how many numbers are not initially set
        for (int i = 1; i <= N; i++) {
            if (!isSet[i]) {
                counts[i]++;
            }
        }

        long result = 1;
        for (int i = 1; i <= N; i++) {
            if (!isSet[i]) {
                result = (result * (counts[i] + 1)) % MOD; // options: not set or set
            }
        }

        // Calculate ways to assign values for '-1' without breaking the good sequence property
        result = (result * countValidConfig()) % MOD;
        System.out.println(result);
    }

    static long countValidConfig() {
        long result = 1; // Start with 1 valid configuration
        int unknowns = 0;
        for (int i = 0; i < N; i++) {
            if (A[i] == -1) {
                unknowns++;
            }
        }

        // Each -1 can be filled with a valid number from 1 to N
        result = (result * modPow(N, unknowns)) % MOD;
        return result;
    }

    static long modPow(long base, long exp) {
        long res = 1;
        while (exp > 0) {
            if (exp % 2 == 1) {
                res = (res * base) % MOD;
            }
            base = (base * base) % MOD;
            exp /= 2;
        }
        return res;
    }
}