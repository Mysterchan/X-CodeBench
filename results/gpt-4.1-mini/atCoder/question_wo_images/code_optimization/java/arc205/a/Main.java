import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        char[][] matrix = new char[n][n];
        for (int i = 0; i < n; i++) {
            matrix[i] = br.readLine().toCharArray();
        }

        // Precompute a 2D prefix sum array for 2x2 white squares
        // whiteSquare[i][j] = 1 if cells (i,j),(i,j+1),(i+1,j),(i+1,j+1) are all white, else 0
        int[][] whiteSquare = new int[n - 1][n - 1];
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 1; j++) {
                if (matrix[i][j] == '.' && matrix[i][j + 1] == '.' &&
                    matrix[i + 1][j] == '.' && matrix[i + 1][j + 1] == '.') {
                    whiteSquare[i][j] = 1;
                }
            }
        }

        // Build prefix sums for whiteSquare
        int[][] prefix = new int[n][n];
        // prefix[i][j] = sum of whiteSquare[0..i-1][0..j-1]
        for (int i = 1; i < n; i++) {
            int rowSum = 0;
            for (int j = 1; j < n; j++) {
                rowSum += whiteSquare[i - 1][j - 1];
                prefix[i][j] = prefix[i - 1][j] + rowSum;
            }
        }

        // For each query, answer by counting how many 2x2 white squares lie fully inside the subgrid
        // The subgrid is from rows U to D and columns L to R (1-based)
        // The 2x2 squares must be fully inside, so top-left corner ranges:
        // rows: U to D-1, columns: L to R-1
        for (int _ = 0; _ < q; _++) {
            st = new StringTokenizer(br.readLine());
            int U = Integer.parseInt(st.nextToken());
            int D = Integer.parseInt(st.nextToken());
            int L = Integer.parseInt(st.nextToken());
            int R = Integer.parseInt(st.nextToken());

            // Calculate sum of whiteSquare in rectangle [U, D-1] x [L, R-1]
            // Using prefix sums:
            // sum = prefix[D-1][R-1] - prefix[U-1][R-1] - prefix[D-1][L-1] + prefix[U-1][L-1]
            int res = prefix[D - 1][R - 1] - prefix[U - 1][R - 1] - prefix[D - 1][L - 1] + prefix[U - 1][L - 1];
            out.println(res);
        }

        out.flush();
    }
}