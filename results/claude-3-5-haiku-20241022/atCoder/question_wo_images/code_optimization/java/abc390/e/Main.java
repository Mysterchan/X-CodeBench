import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    private static class Food {
        int quantity;
        int calories;
        
        Food(int quantity, int calories) {
            this.quantity = quantity;
            this.calories = calories;
        }
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());
        
        List<Food>[] vitamins = new ArrayList[3];
        for (int i = 0; i < 3; i++) {
            vitamins[i] = new ArrayList<>();
        }
        
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int v = Integer.parseInt(st.nextToken()) - 1;
            int a = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            vitamins[v].add(new Food(a, c));
        }
        
        int[][] dp = new int[3][x + 1];
        for (int i = 0; i < 3; i++) {
            Arrays.fill(dp[i], -1);
            dp[i][0] = 0;
            
            for (Food food : vitamins[i]) {
                for (int j = x; j >= food.calories; j--) {
                    if (dp[i][j - food.calories] != -1) {
                        dp[i][j] = Math.max(dp[i][j], dp[i][j - food.calories] + food.quantity);
                    }
                }
            }
        }
        
        int maxMin = 0;
        for (int c1 = 0; c1 <= x; c1++) {
            if (dp[0][c1] <= 0) continue;
            for (int c2 = 0; c2 <= x - c1; c2++) {
                if (dp[1][c2] <= 0) continue;
                int c3 = x - c1 - c2;
                if (c3 >= 0 && dp[2][c3] > 0) {
                    int minVitamin = Math.min(dp[0][c1], Math.min(dp[1][c2], dp[2][c3]));
                    maxMin = Math.max(maxMin, minVitamin);
                }
            }
        }
        
        System.out.println(maxMin);
    }
}