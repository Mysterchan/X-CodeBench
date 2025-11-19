import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        char[][] grid = new char[n][n];

        // Initialize grid with '#'
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = '#';
            }
        }

        // Fill in the appropriate pattern
        for (int i = 1; i <= n; i++) {
            int j = n + 1 - i;
            if (i > j) continue;
            
            char fillChar = (i % 2 == 0) ? '.' : '#';
            for (int row = i - 1; row <= j - 1; row++) {
                for (int col = i - 1; col <= j - 1; col++) {
                    if (row == i - 1 || row == j - 1 || col == i - 1 || col == j - 1) {
                        grid[row][col] = fillChar;
                    } else if ((row - (i - 1)) % 2 == 0 && (col - (i - 1)) % 2 == 0) {
                        grid[row][col] = fillChar;
                    }
                }
            }
        }

        // Print the result
        for (int i = 0; i < n; i++) {
            System.out.println(new String(grid[i]));
        }
    }
}