import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        String s = scanner.next();

        List<Integer> ones = new ArrayList<>();

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                ones.add(i);
            }
        }

        int k = ones.size();
        
        if (k <= 1) {
            System.out.println(0);
            return;
        }

        long minCost = Long.MAX_VALUE;
        
        // Precompute prefix sums
        long[] prefixSum = new long[k + 1];
        for (int i = 0; i < k; i++) {
            prefixSum[i + 1] = prefixSum[i] + ones.get(i);
        }
        
        // Try each position as the median
        for (int mid = 0; mid < k; mid++) {
            int mVal = ones.get(mid);
            
            // Cost for left side
            long leftCost = (long) mid * mVal - prefixSum[mid] - (long) mid * (mid - 1) / 2;
            
            // Cost for right side
            long rightCost = (prefixSum[k] - prefixSum[mid + 1]) - (long) (k - mid - 1) * mVal - (long) (k - mid - 1) * (k - mid) / 2;
            
            minCost = Math.min(minCost, leftCost + rightCost);
        }

        System.out.println(minCost);
    }
}