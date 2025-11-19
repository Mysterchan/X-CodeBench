import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] aStr = br.readLine().split(" ");
        String[] bStr = br.readLine().split(" ");

        int[] a = new int[n];
        int[] b = new int[n];
        int unknownCount = 0;
        long sumKnown = -1;
        boolean possible = true;

        // We'll track the sums for known pairs and check feasibility
        // Also track min and max possible sums from known pairs
        // Since we can rearrange A arbitrarily, the order doesn't matter.

        // Count how many pairs have both known values
        // For pairs with one or both unknowns, we can assign values to achieve the target sum if possible.

        // First, collect all known sums and check if they are consistent
        // If inconsistent, answer is No immediately.

        // Also, check if any known sum is negative or impossible to achieve with non-negative assignments.

        // We'll store all known sums in a set to check consistency
        Set<Long> knownSums = new HashSet<>();
        int knownPairs = 0;

        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(aStr[i]);
            b[i] = Integer.parseInt(bStr[i]);
            if (a[i] == -1 && b[i] == -1) {
                unknownCount++;
            } else if (a[i] == -1) {
                // b[i] known
                if (b[i] < 0) {
                    possible = false;
                    break;
                }
                knownPairs++;
                knownSums.add((long) b[i]); // sum = A_i + B_i, A_i unknown, so sum >= b[i]
            } else if (b[i] == -1) {
                // a[i] known
                if (a[i] < 0) {
                    possible = false;
                    break;
                }
                knownPairs++;
                knownSums.add((long) a[i]); // sum = A_i + B_i, B_i unknown, so sum >= a[i]
            } else {
                // both known
                if (a[i] < 0 || b[i] < 0) {
                    possible = false;
                    break;
                }
                long s = (long) a[i] + b[i];
                knownPairs++;
                knownSums.add(s);
            }
        }

        if (!possible) {
            System.out.println("No");
            return;
        }

        // If there are multiple known sums, they must all be equal
        if (knownSums.size() > 1) {
            System.out.println("No");
            return;
        }

        // Determine the target sum
        long targetSum;
        if (knownSums.isEmpty()) {
            // No known sums, so we can pick any sum >= 0
            // For example, 0
            targetSum = 0;
        } else {
            targetSum = knownSums.iterator().next();
        }

        // Now check feasibility for each pair:
        // For pairs with both known, sum must equal targetSum
        // For pairs with one known, the unknown must be assigned targetSum - known value >= 0
        // For pairs with both unknown, assign any non-negative values summing to targetSum

        for (int i = 0; i < n; i++) {
            if (a[i] != -1 && b[i] != -1) {
                if ((long) a[i] + b[i] != targetSum) {
                    System.out.println("No");
                    return;
                }
            } else if (a[i] == -1 && b[i] != -1) {
                if (targetSum < b[i]) {
                    System.out.println("No");
                    return;
                }
            } else if (a[i] != -1 && b[i] == -1) {
                if (targetSum < a[i]) {
                    System.out.println("No");
                    return;
                }
            }
            // if both unknown, always possible
        }

        System.out.println("Yes");
    }
}