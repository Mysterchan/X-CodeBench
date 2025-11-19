import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        new Main().solve();
    }

    private void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());

        // Separate foods by vitamin type
        int[][] foods = new int[3][n * 2]; // store as pairs (A_i, C_i)
        int[] counts = new int[3];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int v = Integer.parseInt(st.nextToken()) - 1;
            int a = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            foods[v][counts[v] * 2] = a;
            foods[v][counts[v] * 2 + 1] = c;
            counts[v]++;
        }

        // dp arrays: dp[v][cal] = max vitamin amount for vitamin v with cal calories
        // Initialize with -1 (impossible)
        int[][] dp = new int[3][X + 1];
        for (int v = 0; v < 3; v++) {
            for (int cal = 0; cal <= X; cal++) {
                dp[v][cal] = -1;
            }
            dp[v][0] = 0;
            for (int i = 0; i < counts[v]; i++) {
                int a = foods[v][i * 2];
                int c = foods[v][i * 2 + 1];
                for (int cal = X; cal >= c; cal--) {
                    if (dp[v][cal - c] != -1) {
                        int val = dp[v][cal - c] + a;
                        if (val > dp[v][cal]) {
                            dp[v][cal] = val;
                        }
                    }
                }
            }
        }

        // For each vitamin, create an array minCaloriesForAmount[v][amount] = minimal calories to get at least amount
        // We only need to consider amounts up to max possible for each vitamin
        int[] maxAmount = new int[3];
        for (int v = 0; v < 3; v++) {
            for (int cal = 0; cal <= X; cal++) {
                if (dp[v][cal] > maxAmount[v]) {
                    maxAmount[v] = dp[v][cal];
                }
            }
        }

        // For each vitamin, build minCaloriesForAmount array
        // Initialize with large value (X+1)
        int[][] minCaloriesForAmount = new int[3][];
        for (int v = 0; v < 3; v++) {
            int maxA = maxAmount[v];
            minCaloriesForAmount[v] = new int[maxA + 1];
            for (int i = 0; i <= maxA; i++) {
                minCaloriesForAmount[v][i] = X + 1;
            }
            // For each calorie, update minimal calories for dp[v][cal] amount
            for (int cal = 0; cal <= X; cal++) {
                int amt = dp[v][cal];
                if (amt >= 0) {
                    if (cal < minCaloriesForAmount[v][amt]) {
                        minCaloriesForAmount[v][amt] = cal;
                    }
                }
            }
            // Make minCaloriesForAmount non-increasing for easier binary search
            for (int i = maxA - 1; i >= 0; i--) {
                if (minCaloriesForAmount[v][i] > minCaloriesForAmount[v][i + 1]) {
                    minCaloriesForAmount[v][i] = minCaloriesForAmount[v][i + 1];
                }
            }
        }

        // Binary search on answer (minimum vitamin intake)
        int left = 0;
        int right = Math.min(Math.min(maxAmount[0], maxAmount[1]), maxAmount[2]);
        int ans = 0;

        while (left <= right) {
            int mid = (left + right) >>> 1;
            // Check if possible to get at least mid units of each vitamin within X calories
            int cal1 = minCaloriesForAmount[0][mid];
            int cal2 = minCaloriesForAmount[1][mid];
            int cal3 = minCaloriesForAmount[2][mid];
            if ((long) cal1 + cal2 + cal3 <= X) {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        System.out.println(ans);
    }
}