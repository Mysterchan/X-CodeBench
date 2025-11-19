import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int q = sc.nextInt();
        char[][] matrix = new char[n][n];

        // Read the matrix
        for (int i = 0; i < n; i++) {
            matrix[i] = sc.next().toCharArray();
        }

        // Preprocess the matrix to create a count of white cells that form 2x2 squares
        int[][] count = new int[n - 1][n - 1];
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 1; j++) {
                if (matrix[i][j] == '.' && matrix[i][j + 1] == '.' && 
                    matrix[i + 1][j] == '.' && matrix[i + 1][j + 1] == '.') {
                    count[i][j] = 1;
                }
            }
        }

        // Compute a prefix sum array for 2x2 white cells
        int[][] prefix = new int[n][n];
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < n; j++) {
                prefix[i][j] = count[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1];
            }
        }

        for (int i = 0; i < q; i++) {
            int u = sc.nextInt() - 1;
            int d = sc.nextInt() - 1;
            int l = sc.nextInt() - 1;
            int r = sc.nextInt() - 1;

            // Check the limits of the prefix sums
            int total = prefix[d - 1][r - 1];
            if (u > 0) {
                total -= prefix[u - 1][r - 1];
            }
            if (l > 0) {
                total -= prefix[d - 1][l - 1];
            }
            if (u > 0 && l > 0) {
                total += prefix[u - 1][l - 1];
            }

            System.out.println(total);
        }
    }
}