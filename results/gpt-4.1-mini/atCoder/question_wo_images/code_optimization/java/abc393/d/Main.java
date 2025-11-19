import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        String s = scanner.next();

        List<Integer> ones = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            if (s.charAt(i) == '1') {
                ones.add(i);
            }
        }

        int m = ones.size();
        if (m < 2) {
            System.out.println(0);
            return;
        }

        // Precompute prefix sums of ones' positions
        long[] prefix = new long[m + 1];
        for (int i = 0; i < m; i++) {
            prefix[i + 1] = prefix[i] + ones.get(i);
        }

        long ans = Long.MAX_VALUE;

        // For each possible median index, calculate cost in O(1)
        for (int mid = 0; mid < m; mid++) {
            int medianPos = ones.get(mid);

            // Number of ones to the left and right of median
            int leftCount = mid;
            int rightCount = m - mid - 1;

            // Sum of positions on left and right
            long leftSum = prefix[mid];
            long rightSum = prefix[m] - prefix[mid + 1];

            // Calculate cost for left side
            // Target positions for left side: medianPos - 1, medianPos - 2, ..., medianPos - leftCount
            // Sum of target positions on left side:
            // = leftCount * medianPos - (leftCount * (leftCount + 1)) / 2
            long leftTargetSum = (long) leftCount * medianPos - (long) leftCount * (leftCount + 1) / 2;
            long leftCost = leftTargetSum - leftSum;

            // Calculate cost for right side
            // Target positions for right side: medianPos + 1, medianPos + 2, ..., medianPos + rightCount
            // Sum of target positions on right side:
            // = rightCount * medianPos + (rightCount * (rightCount + 1)) / 2
            long rightTargetSum = (long) rightCount * medianPos + (long) rightCount * (rightCount + 1) / 2;
            long rightCost = rightSum - rightTargetSum;

            long totalCost = leftCost + rightCost;
            if (totalCost < ans) {
                ans = totalCost;
            }
        }

        System.out.println(ans);
    }
}