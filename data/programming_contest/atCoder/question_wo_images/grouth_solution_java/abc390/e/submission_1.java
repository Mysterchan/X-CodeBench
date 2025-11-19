import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class Main {

    static class Food {
        int A;
        int C;

        Food(int A, int C) {
            this.A = A;
            this.C = C;
        }
    }

    static long[] runKnapsack(int X, List<Food> foods) {

        long[] dp = new long[X + 1];

        for (Food food : foods) {
            for (int c = X; c >= food.C; c--) {
                dp[c] = Math.max(dp[c], dp[c - food.C] + food.A);
            }
        }

        for (int c = 1; c <= X; c++) {
            dp[c] = Math.max(dp[c], dp[c - 1]);
        }
        return dp;
    }

    static int findMinCost(long[] dp, long K, int X) {
        for (int c = 0; c <= X; c++) {
            if (dp[c] >= K) {
                return c;
            }
        }
        return X + 1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int X = sc.nextInt();

        List<Food> vit1Foods = new ArrayList<>();
        List<Food> vit2Foods = new ArrayList<>();
        List<Food> vit3Foods = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            int V = sc.nextInt();
            int A = sc.nextInt();
            int C = sc.nextInt();
            if (V == 1) {
                vit1Foods.add(new Food(A, C));
            } else if (V == 2) {
                vit2Foods.add(new Food(A, C));
            } else {
                vit3Foods.add(new Food(A, C));
            }
        }

        long[] dp1 = runKnapsack(X, vit1Foods);
        long[] dp2 = runKnapsack(X, vit2Foods);
        long[] dp3 = runKnapsack(X, vit3Foods);

        long low = 0;

        long high = 1_000_000_001L;
        long ans = 0;

        while (low <= high) {
            long midK = low + (high - low) / 2;

            if (midK == 0) {
                ans = 0;
                low = midK + 1;
                continue;
            }

            int cost1 = findMinCost(dp1, midK, X);
            int cost2 = findMinCost(dp2, midK, X);
            int cost3 = findMinCost(dp3, midK, X);

            if ((long)cost1 + cost2 + cost3 <= X) {

                ans = midK;
                low = midK + 1;
            } else {

                high = midK - 1;
            }
        }

        System.out.println(ans);
        sc.close();
    }
}