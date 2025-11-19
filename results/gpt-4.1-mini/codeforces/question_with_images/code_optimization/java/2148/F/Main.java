import java.util.*;
import java.io.*;

public class Main {
    static FastScanner fs = null;

    public static void main(String[] args) {
        fs = new FastScanner();
        PrintWriter out = new PrintWriter(System.out);
        int t = fs.nextInt();
        while (t-- > 0) {
            int n = fs.nextInt();
            int maxLen = 0;
            int[][] arrays = new int[n][];
            for (int i = 0; i < n; i++) {
                int k = fs.nextInt();
                arrays[i] = new int[k];
                maxLen = Math.max(maxLen, k);
                for (int j = 0; j < k; j++) {
                    arrays[i][j] = fs.nextInt();
                }
            }

            // The key insight:
            // After gravity, the bottom row is formed by taking the bottom-most element
            // in each column from the stacked arrays.
            // We can reorder arrays arbitrarily.
            // To get lex min bottom row, for each column, pick the minimal element possible
            // from the arrays that have that column.
            // Since gravity stacks elements down, the bottom row at column c is the minimal
            // element among all arrays that have length > c, at position c.

            // So for each column c (0-based), find the minimal element among arrays[i][c] for all i with length > c.

            // We only need to find minimal elements per column.

            int[] bottomRow = new int[maxLen];
            Arrays.fill(bottomRow, Integer.MAX_VALUE);

            for (int i = 0; i < n; i++) {
                int[] arr = arrays[i];
                for (int c = 0; c < arr.length; c++) {
                    if (arr[c] < bottomRow[c]) {
                        bottomRow[c] = arr[c];
                    }
                }
            }

            // Output the bottom row
            for (int i = 0; i < maxLen; i++) {
                out.print(bottomRow[i] + " ");
            }
            out.println();
        }
        out.close();
    }

    static class FastScanner {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer("");

        String next() {
            while (!st.hasMoreTokens())
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }
    }
}