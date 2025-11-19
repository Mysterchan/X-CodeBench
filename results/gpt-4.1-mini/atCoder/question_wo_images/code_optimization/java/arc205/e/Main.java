import java.util.*;
public class Main {
    static final int MOD = 998244353;
    static final int MAX_BIT = 20;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }

        // freq[mask] = product of all A[i] with value == mask
        // Since A[i] < 2^20, we can use an array of size 2^20
        int size = 1 << MAX_BIT;
        long[] freq = new long[size];
        Arrays.fill(freq, 1L);

        // Count product of all elements with exact value mask
        // If no element with that mask, freq[mask] = 1 (neutral for multiplication)
        // For each A[i], multiply freq[A[i]] by A[i]
        for (int i = 0; i < N; i++) {
            freq[A[i]] = (freq[A[i]] * A[i]) % MOD;
        }

        // We want for each mask, the product of all elements whose value is subset of mask
        // i.e. all x where (x | mask) == mask  <=> x subset of mask
        // Use SOS DP to compute freq2[mask] = product of freq[subsets of mask]
        // Multiplicative SOS DP:
        // For each bit, multiply freq2[mask] by freq2[mask^(1<<bit)] if bit is set in mask

        // Copy freq to freq2
        long[] freq2 = freq.clone();

        for (int bit = 0; bit < MAX_BIT; bit++) {
            for (int mask = 0; mask < size; mask++) {
                if ((mask & (1 << bit)) != 0) {
                    freq2[mask] = (freq2[mask] * freq2[mask ^ (1 << bit)]) % MOD;
                }
            }
        }

        // Now freq2[mask] = product of all A[i] with value subset of mask

        // For each k, output freq2[A[k]]
        StringBuilder sb = new StringBuilder();
        for (int k = 0; k < N; k++) {
            sb.append(freq2[A[k]]).append('\n');
        }
        System.out.print(sb);
    }
}