import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int Q = Integer.parseInt(st.nextToken());

        char[][] grid = new char[N + 2][N + 2];
        for (int i = 1; i <= N; i++) {
            String line = br.readLine();
            for (int j = 1; j <= N; j++) {
                grid[i][j] = line.charAt(j - 1);
            }
        }

        // a[i][j] = 1 if 2x2 white square with top-left at (i,j)
        int[][] ps = new int[N + 1][N + 1];
        for (int i = 1; i < N; i++) {
            int rowSum = 0;
            for (int j = 1; j < N; j++) {
                int val = 0;
                if (grid[i][j] == '.' && grid[i+1][j] == '.' &&
                    grid[i][j+1] == '.' && grid[i+1][j+1] == '.') {
                    val = 1;
                }
                rowSum += val;
                ps[i][j] = ps[i-1][j] + rowSum;
            }
        }

        PrintWriter out = new PrintWriter(System.out);
        StringBuilder sb = new StringBuilder();
        for (int qi = 0; qi < Q; qi++) {
            st = new StringTokenizer(br.readLine());
            int U = Integer.parseInt(st.nextToken());
            int D = Integer.parseInt(st.nextToken());
            int L = Integer.parseInt(st.nextToken());
            int R = Integer.parseInt(st.nextToken());
            int i1 = U, i2 = D - 1;
            int j1 = L, j2 = R - 1;
            if (i1 > i2 || j1 > j2) {
                sb.append(0).append('\n');
            } else {
                int res = ps[i2][j2] - ps[i1 - 1][j2] - ps[i2][j1 - 1] + ps[i1 - 1][j1 - 1];
                sb.append(res).append('\n');
            }
        }
        out.print(sb.toString());
        out.flush();
    }
}