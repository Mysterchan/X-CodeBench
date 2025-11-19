import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    private class Intakes {
        private int quantity;
        private int calories;
        public Intakes(int quantity, int calories) {
            this.quantity = quantity;
            this.calories = calories;
        }

        public int getQuantity() {
            return quantity;
        }

        public int getCalories() {
            return calories;
        }
    }
    public static void main(String[] args) throws IOException {
        Main vitaminsIntake = new Main();
        vitaminsIntake.solve();
    }

    private void solve() throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(bufferedReader.readLine());

        int n = Integer.parseInt(tokenizer.nextToken());
        int x = Integer.parseInt(tokenizer.nextToken());

        List<Intakes>[] vitamins = new ArrayList[3];
        for(int i = 0; i < 3; ++i) {
            vitamins[i] = new ArrayList<>();
        }

        for(int i = 0; i < n; ++i) {
            tokenizer = new StringTokenizer(bufferedReader.readLine());
            int v = Integer.parseInt(tokenizer.nextToken());
            int a = Integer.parseInt(tokenizer.nextToken());
            int c = Integer.parseInt(tokenizer.nextToken());

            vitamins[v - 1].add(new Intakes(a, c));
        }

        int [][]dp = new int[3][x + 10];
        for(int []data: dp) {
            Arrays.fill(data, -1);
        }
        for(int i = 0; i < 3; ++i) {
            dp[i][0] = 0;
            for(Intakes intake: vitamins[i]) {
                for(int j = x; j >= intake.calories ; --j) {
                    if (dp[i][j - intake.calories] == -1) {
                        continue;
                    }

                    dp[i][j] = Math.max(dp[i][j], dp[i][j - intake.calories] + intake.getQuantity());
                }
            }
        }

        ArrayList<Intakes> []finalData = new ArrayList[3];
        for(int j = 0; j < 3; ++j) {
            finalData[j] = new ArrayList<>();
            for(int i = 1; i <= x; ++i) {
                if (dp[j][i] > 0) {
                    finalData[j].add(new Intakes(dp[j][i], i));
                }
            }
        }

        int max = 0;
        for(Intakes a: finalData[0]) {
            if (x < a.getCalories())break;
            for(Intakes b: finalData[1]) {
                if (x < (a.getCalories() + b.getCalories()))break;
                for(Intakes c: finalData[2]) {
                    if (x < (a.getCalories() + b.getCalories() + c.getCalories()))break;
                    max = Math.max(max, Math.min(a.getQuantity(), Math.min(b.getQuantity(), c.getQuantity())));
                }
            }
        }

        System.out.println(max);

    }

    private static void displayData(int[][] dp) {
        for (int i = 0; i < 3; ++i) {
            for(int j: dp[i]) {
                if (j > 0)
                    System.out.print(j + " ");
            }
            System.out.println();
        }
    }

}