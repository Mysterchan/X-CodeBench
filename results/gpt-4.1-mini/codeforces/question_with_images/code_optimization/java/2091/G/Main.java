import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            long s = sc.nextLong();
            int k = sc.nextInt();

            if (s % k == 0) {
                // If s is divisible by k, no turns needed, power remains k
                System.out.println(k);
                continue;
            }

            if (s >= (long) k * k) {
                // If s is large enough, we can afford at least two turns,
                // so power reduces by at least 2 (but not below 1)
                System.out.println(Math.max(1, k - 2));
                continue;
            }

            // Otherwise, simulate the minimal number of turns needed to reach s
            // Turns reduce power by 1 each (except power never below 1)
            // We find minimal turns t such that s can be reached with power k - t

            // The minimal number of turns needed can be found by checking
            // if s can be represented as a sum of moves with decreasing power
            // but since k and s are small here (k <= 1000, s < k*k),
            // we can do a simple binary search on turns

            int left = 0, right = k - 1;
            int ans = 1;

            while (left <= right) {
                int mid = (left + right) / 2;
                int powerAfterTurns = Math.max(1, k - mid);

                // Maximum distance reachable with mid turns:
                // Each turn reduces power by 1 (except power never below 1)
                // The maximum distance is sum of moves with powers:
                // k, k-1, k-2, ..., powerAfterTurns
                // But turns alternate directions, so max distance is:
                // (mid + 1) * powerAfterTurns

                // Actually, from problem and examples, the max distance reachable with mid turns is:
                // (mid + 1) * powerAfterTurns

                // Check if s <= (mid + 1) * powerAfterTurns
                // If yes, we can reach s with mid turns

                long maxDist = (long) (mid + 1) * powerAfterTurns;

                if (maxDist >= s) {
                    ans = powerAfterTurns;
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }

            System.out.println(ans);
        }
    }
}