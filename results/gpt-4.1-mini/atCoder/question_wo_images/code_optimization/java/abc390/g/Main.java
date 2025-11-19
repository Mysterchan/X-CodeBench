import java.util.Scanner;

public class Main {
    static final long MOD = 998244353;

    static long pow(long base, long exp) {
        long res = 1;
        base %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) res = (res * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.close();

        // Precompute factorials
        long[] fact = new long[N + 1];
        fact[0] = 1;
        for (int i = 1; i <= N; i++) {
            fact[i] = (fact[i - 1] * i) % MOD;
        }

        // Precompute length of each number and powers of 10
        int[] len = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            int x = i;
            int l = 0;
            while (x > 0) {
                x /= 10;
                l++;
            }
            len[i] = l;
        }

        // Precompute prefix sums of lengths for quick calculation of total length
        long[] prefixLen = new long[N + 1];
        for (int i = 1; i <= N; i++) {
            prefixLen[i] = prefixLen[i - 1] + len[i];
        }

        // Precompute powers of 10 up to max total length
        // Max total length = sum of lengths of 1..N, max ~ 6 * 2e5 = 1.2e6
        // But we only need powers up to max length of concatenation = sum of all lengths
        // We'll compute powers on the fly using pow function with memoization

        // Instead of complicated combinatorics, use the key insight:
        // The sum over all permutations of f(P) = (N! / N) * sum_{k=1}^N k * sum over all positions of 10^{pos_shift}
        // But positions vary, so we use a formula derived from the problem editorial:
        // The sum is fact[N-1] * sum_{k=1}^N k * sum_{j=0}^{N-1} 10^{sum of lengths of j elements}

        // To implement efficiently:
        // For each position j (0-based), the contribution of each number k is k * 10^{sum of lengths of j elements}
        // Since all permutations are equally likely, each number appears equally in each position: (N-1)! times
        // So total sum = (N-1)! * sum_{j=0}^{N-1} 10^{sumLen_j} * sum_{k=1}^N k

        // sum_{k=1}^N k = N*(N+1)/2 mod MOD
        long sumK = ((long) N * (N + 1) / 2) % MOD;
        long factN_1 = fact[N - 1];

        // Precompute prefix sums of lengths for positions 0..N-1
        // sumLen_j = sum of lengths of first j numbers (j from 0 to N-1)
        // prefixLen array already has sum of lengths of first i numbers (1-based)
        // So sumLen_j = prefixLen[j]

        // Precompute powers of 10 for all prefixLen[j]
        // max prefixLen[N] can be up to ~1.2 million, so we use pow function directly

        long totalSum = 0;
        for (int j = 0; j < N; j++) {
            long power = pow(10, prefixLen[j]);
            long contrib = (power * sumK) % MOD;
            totalSum = (totalSum + contrib) % MOD;
        }
        totalSum = (totalSum * factN_1) % MOD;

        System.out.println(totalSum);
    }
}