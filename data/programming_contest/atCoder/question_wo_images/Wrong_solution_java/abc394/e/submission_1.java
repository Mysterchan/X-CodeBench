import java.util.*;
import java.io.*;

public class Main {
    static int[][][] dp;
    static int[][][] dp2;
    static char[][] grid;
    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);

        n = Integer.parseInt(br.readLine());
        grid = new char[n][n];
        for (int i = 0; i < n; i++) {
            grid[i] = br.readLine().toCharArray();
        }

        dp = new int[n][n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                Arrays.fill(dp[i][j], -1);
            }
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (i == j) dp[i][j][k] = 0;
                    else if (grid[i][j] != '-') dp[i][j][k] = 1;
                    else if (k != i && k != j && grid[i][k] != '-' && grid[k][j] != '-') {
                        dp[i][j][k] = 2;
                    }
                }
            }
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (dp[i][j][k] == -1) {
                        for (int l = 0; l < n; l++) {
                            if (l != k && grid[i][l] != '-' && dp[l][j][k] != -1) {
                                dp[i][j][k] = dp[l][j][k] + 1;
                                break;
                            }
                        }
                    }
                }
            }
        }

        dp2 = new int[n][n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                Arrays.fill(dp2[i][j], -1);
            }
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (i == j) dp2[i][j][k] = 0;
                    else if (grid[i][j] == grid[j][i] && grid[i][j] != '-') dp2[i][j][k] = 2;
                    else if (k != i && k != j && grid[i][k] != '-' && grid[k][j] != '-' && grid[i][k] == grid[j][k]) {
                        dp2[i][j][k] = 4;
                    }
                }
            }
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (dp2[i][j][k] == -1) {
                        for (int l = 0; l < n; l++) {
                            for (int m = 0; m < n; m++) {
                                if (l != k && m != k && grid[i][l] != '-' && grid[m][j] != '-' && dp[l][m][k] != -1) {
                                    dp2[i][j][k] = dp[l][m][k] + 2;
                                    break;
                                }
                            }
                            if (dp2[i][j][k] != -1) break;
                        }
                    }
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int ans = -1;
                for (int k = 0; k < n; k++) {
                    if (dp[i][j][k] != -1 && (ans == -1 || dp[i][j][k] < ans)) ans = dp[i][j][k];
                    if (dp2[i][j][k] != -1 && (ans == -1 || dp2[i][j][k] < ans)) ans = dp2[i][j][k];
                }
                pw.print(ans + " ");
            }
            pw.println();
        }

        pw.close();
    }
}