import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        char[][] res = new char[n][n];

        // Initialize all cells to black ('#')
        for (int i = 0; i < n; i++) {
            Arrays.fill(res[i], '#');
        }

        // For each i from 1 to n (1-based indexing)
        // i <= j = n+1 - i  => i <= n+1 - i => 2i <= n+1 => i <= (n+1)/2
        // So only for i in [1, (n+1)/2]
        // Fill the square from (i,i) to (j,j) with white '.' if i even, black '#' if i odd
        // Using 0-based indexing: (i-1, i-1) to (j-1, j-1)
        int half = (n + 1) / 2;
        for (int i = 1; i <= half; i++) {
            int j = n + 1 - i;
            char color = (i % 2 == 1) ? '#' : '.';
            for (int r = i - 1; r <= j - 1; r++) {
                for (int c = i - 1; c <= j - 1; c++) {
                    res[r][c] = color;
                }
            }
        }

        // Print the result
        for (int i = 0; i < n; i++) {
            System.out.println(new String(res[i]));
        }
    }
}