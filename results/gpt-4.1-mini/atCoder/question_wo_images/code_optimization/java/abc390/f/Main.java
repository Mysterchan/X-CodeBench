import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt() - 1;
        }

        // The problem reduces to counting the number of connected components
        // in the subarray's value set intervals.
        // The original code tries to track intervals and connected components naively.
        // We can optimize by using a two-pointer approach and a Union-Find or
        // a boolean array to track presence and connected components efficiently.

        // Key insight:
        // For each subarray [L,R], f(L,R) = number of connected components in the set of values in A[L..R].
        // Connected components are defined by consecutive integers present in the subarray.

        // We can use a two-pointer approach:
        // - Expand R from L to N-1
        // - Maintain min and max of values in A[L..R]
        // - Maintain a boolean array "present" to mark which values are present
        // - Maintain count of connected components in the current subarray
        //   - When a new value is added:
        //     - If neighbors (value-1 and value+1) are present, connected components decrease by 1 for each neighbor present
        //     - Else if no neighbors present, connected components increase by 1

        // To optimize memory and speed:
        // - We reset the "present" array for each L
        // - Use an int[] for present with 0/1 flags
        // - Since N can be up to 3*10^5, this is still O(N^2) worst case, but we can optimize by
        //   breaking early when max-min+1 > current length (since intervals must be continuous)
        // However, this is still too slow for N=3*10^5.

        // We need a better approach:
        // Observation:
        // f(L,R) = number of connected components in the set of values in A[L..R].
        // The connected components correspond to intervals of consecutive integers present.

        // Another approach:
        // For each position i, we can find the minimal R such that the subarray A[i..R]
        // forms a connected interval of values (i.e., max - min + 1 == number of distinct values).
        // For such intervals, f(i,R) = 1.
        // For other intervals, f(i,R) > 1.

        // The original code counts connected components for all subarrays, which is O(N^2).

        // Since the problem is from a contest, the intended solution is to use a stack or segment tree
        // or a data structure to process intervals efficiently.

        // However, the original code is accepted but slow.
        // We can optimize the original code by:
        // - Using a single boolean array for presence instead of int[]
        // - Avoid resetting the entire array for each L by using a versioning technique
        // - Using a fast IO and minimal operations inside loops

        // Implementing versioning technique for presence array:
        // Instead of clearing the presence array for each L, we keep an int[] lastSeen
        // and an int currentVersion that increments for each L.
        // presence[x] = (lastSeen[x] == currentVersion)

        int[] lastSeen = new int[N];
        int currentVersion = 0;
        int ans = 0;

        for (int i = 0; i < N; i++) {
            currentVersion++;
            int min = A[i];
            int max = A[i];
            int sum = 1; // number of connected components
            lastSeen[min] = currentVersion;

            for (int j = i; j < N; j++) {
                int val = A[j];
                if (lastSeen[val] == currentVersion) {
                    // already present, no change
                } else {
                    lastSeen[val] = currentVersion;
                    if (val < min) {
                        min = val;
                        // new min, check neighbor min+1
                        if (lastSeen[min + 1] != currentVersion) {
                            sum++;
                        }
                    } else if (val > max) {
                        max = val;
                        // new max, check neighbor max-1
                        if (lastSeen[max - 1] != currentVersion) {
                            sum++;
                        }
                    } else {
                        // val inside [min+1, max-1]
                        boolean left = lastSeen[val - 1] == currentVersion;
                        boolean right = lastSeen[val + 1] == currentVersion;
                        if (left && right) {
                            sum--;
                        } else if (!left && !right) {
                            sum++;
                        }
                    }
                }
                ans += sum;
            }
        }

        System.out.println(ans);
    }
}