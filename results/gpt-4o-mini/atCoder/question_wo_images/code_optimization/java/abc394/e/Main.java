import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        char[][] matrix = new char[n][n];
        for (int i = 0; i < n; i++) {
            matrix[i] = br.readLine().toCharArray();
        }

        int[][] dist = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dist[i], Integer.MAX_VALUE);
            dist[i][i] = 0; // Distance to self is 0
        }

        for (char c = 'a'; c <= 'z'; c++) {
            List<int[]> edges = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (matrix[i][j] == c) {
                        edges.add(new int[]{i, j});
                    }
                }
            }
            for (int[] edge1 : edges) {
                for (int[] edge2 : edges) {
                    if (edge1[0] != edge2[0] && edge1[1] != edge2[1]) {
                        int newDist = dist[edge1[0]][edge1[1]] + 2;
                        dist[edge1[0]][edge2[1]] = Math.min(dist[edge1[0]][edge2[1]], newDist);
                    }
                }
            }
        }

        PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dist[i][j] == Integer.MAX_VALUE) {
                    out.print(-1 + " ");
                } else {
                    out.print(dist[i][j] + " ");
                }
            }
            out.println();
        }
        out.flush();
    }
}