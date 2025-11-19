import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws java.lang.Exception {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        StringBuilder result = new StringBuilder();
        
        for (int test = 0; test < t; test++) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int k = sc.nextInt();
            char[][] arr = new char[n][m];
            int totalGold = 0;
            int[][] goldCount = new int[n + 2 * k][m + 2 * k];

            // Read the mine grid and calculate total gold
            for (int i = 0; i < n; i++) {
                arr[i] = sc.next().toCharArray();
                for (int j = 0; j < m; j++) {
                    if (arr[i][j] == 'g') {
                        totalGold++;
                        // Increment goldCount for ranges influenced by this gold
                        int startX = Math.max(0, i - k);
                        int endX = Math.min(n - 1, i + k);
                        int startY = Math.max(0, j - k);
                        int endY = Math.min(m - 1, j + k);
                        
                        for (int x = startX; x <= endX; x++) {
                            for (int y = startY; y <= endY; y++) {
                                if (x >= 0 && x < n && y >= 0 && y < m) {
                                    goldCount[x][y]++;
                                }
                            }
                        }
                    }
                }
            }

            // Calculate maximum collectible gold in empty spaces
            int maxGoldCollectible = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (arr[i][j] == '.') { // Only check empty cells
                        int startX = Math.max(0, i - k);
                        int endX = Math.min(n - 1, i + k);
                        int startY = Math.max(0, j - k);
                        int endY = Math.min(m - 1, j + k);

                        int goldAtThisCell = 0;
                        // Count gold on the boundary
                        for (int x = startX; x <= endX; x++) {
                            for (int y = startY; y <= endY; y++) {
                                if (arr[x][y] == 'g') {
                                    if (x == startX || x == endX || y == startY || y == endY) {
                                        goldAtThisCell++;
                                    }
                                }
                            }
                        }
                        maxGoldCollectible = Math.max(maxGoldCollectible, goldAtThisCell);
                    }
                }
            }
            result.append(totalGold - maxGoldCollectible).append("\n");
        }
        System.out.print(result);
    }
}