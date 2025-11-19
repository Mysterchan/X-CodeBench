import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tt = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        while (tt-- > 0) {
            String[] parts = br.readLine().split(" ");
            int n = Integer.parseInt(parts[0]);
            int m = Integer.parseInt(parts[1]);
            int k = Integer.parseInt(parts[2]);

            char[][] arr = new char[n][];
            for (int i = 0; i < n; i++) {
                arr[i] = br.readLine().toCharArray();
            }

            int totalGold = 0;
            boolean hasEmpty = false;

            // Count total gold and check for empty cells
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (arr[i][j] == 'g') totalGold++;
                    else if (arr[i][j] == '.') hasEmpty = true;
                }
            }

            if (!hasEmpty) {
                sb.append("0\n");
                continue;
            }

            // If k == 1, boundary is just the cell itself, so all gold inside disappears, none collected
            // So max gold collected = totalGold - 0 = totalGold
            if (k == 1) {
                sb.append(totalGold).append('\n');
                continue;
            }

            // Precompute prefix sums of gold for O(1) queries
            int[][] prefix = new int[n + 1][m + 1];
            for (int i = 0; i < n; i++) {
                int rowSum = 0;
                for (int j = 0; j < m; j++) {
                    rowSum += (arr[i][j] == 'g' ? 1 : 0);
                    prefix[i + 1][j + 1] = prefix[i][j + 1] + rowSum;
                }
            }

            // Function to get sum of gold in rectangle (r1,c1) to (r2,c2) inclusive
            // Handles out of bounds by clamping
            // Using 1-based indexing for prefix sums
            // Returns 0 if invalid rectangle
            // r1, c1, r2, c2 are zero-based indices
            // So prefix indices are +1
            // sum = prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]
            // Clamp indices to [0,n] and [0,m]
            // If r1 > r2 or c1 > c2 return 0
            // We'll inline this logic in code for speed

            int maxCollected = 0;

            // For each empty cell, calculate gold on boundary of explosion square
            // Boundary is the square of side 2k+1 centered at (x,y)
            // Boundary cells are those on the edges of the square
            // We can get total gold in the big square and total gold in the inner square (side 2k-1)
            // Boundary gold = total big square gold - inner square gold

            int sideBig = 2 * k + 1;
            int sideInner = sideBig - 2; // 2k-1

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (arr[i][j] != '.') continue;

                    // Big square boundaries
                    int r1b = i - k;
                    int c1b = j - k;
                    int r2b = i + k;
                    int c2b = j + k;

                    // Inner square boundaries
                    int r1i = i - k + 1;
                    int c1i = j - k + 1;
                    int r2i = i + k - 1;
                    int c2i = j + k - 1;

                    int bigSum = getSum(prefix, r1b, c1b, r2b, c2b, n, m);
                    int innerSum = getSum(prefix, r1i, c1i, r2i, c2i, n, m);

                    int boundaryGold = bigSum - innerSum;
                    if (boundaryGold > maxCollected) maxCollected = boundaryGold;
                }
            }

            sb.append(maxCollected).append('\n');
        }

        System.out.print(sb);
    }

    static int getSum(int[][] prefix, int r1, int c1, int r2, int c2, int n, int m) {
        // Clamp to valid range
        r1 = Math.max(r1, 0);
        c1 = Math.max(c1, 0);
        r2 = Math.min(r2, n - 1);
        c2 = Math.min(c2, m - 1);

        if (r1 > r2 || c1 > c2) return 0;

        // prefix is 1-based
        int sum = prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1] - prefix[r2 + 1][c1] + prefix[r1][c1];
        return sum;
    }
}