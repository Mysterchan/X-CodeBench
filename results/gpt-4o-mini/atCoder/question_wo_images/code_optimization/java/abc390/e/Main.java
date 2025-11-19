import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        new Main().solve();
    }

    private void solve() throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(bufferedReader.readLine());

        int n = Integer.parseInt(tokenizer.nextToken());
        int x = Integer.parseInt(tokenizer.nextToken());

        int[][] dp = new int[4][x + 1]; // dp[v][c] = max vitamin v intake with c calories
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j <= x; j++) {
                dp[i][j] = 0; // Initialize dp array
            }
        }

        for (int i = 0; i < n; i++) {
            tokenizer = new StringTokenizer(bufferedReader.readLine());
            int v = Integer.parseInt(tokenizer.nextToken());
            int a = Integer.parseInt(tokenizer.nextToken());
            int c = Integer.parseInt(tokenizer.nextToken());

            // Update dp array in reverse order to avoid overwriting
            for (int j = x; j >= c; j--) {
                dp[v][j] = Math.max(dp[v][j], dp[v][j - c] + a);
            }
        }

        // Binary search for the maximum minimum intake
        int low = 0, high = Integer.MAX_VALUE;
        while (low < high) {
            int mid = (low + high + 1) / 2;
            if (canAchieveMinimumIntake(dp, mid, x)) {
                low = mid; // mid is achievable, try for a higher value
            } else {
                high = mid - 1; // mid is not achievable, try lower
            }
        }

        System.out.println(low);
    }

    private boolean canAchieveMinimumIntake(int[][] dp, int minIntake, int maxCalories) {
        int[] requiredCalories = new int[4]; // requiredCalories[v] = min calories needed to achieve at least minIntake of vitamin v
        for (int v = 1; v <= 3; v++) {
            for (int c = 0; c <= maxCalories; c++) {
                if (dp[v][c] >= minIntake) {
                    requiredCalories[v] = Math.min(requiredCalories[v] == 0 ? Integer.MAX_VALUE : requiredCalories[v], c);
                }
            }
        }

        // Check if we can consume the required calories for all three vitamins without exceeding maxCalories
        return requiredCalories[1] + requiredCalories[2] + requiredCalories[3] <= maxCalories;
    }
}