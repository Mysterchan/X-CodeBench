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

        // dist[i][j] = shortest palindrome path length from i to j
        int[][] dist = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dist[i], -1);
            dist[i][i] = 0; // empty path is palindrome of length 0
        }

        // We'll do a BFS on pairs (i,j) representing the start and end of the palindrome path
        // The BFS state is (i,j), and the distance is the length of the palindrome path from i to j
        // Initially, for all edges i->j with label c, dist[i][j] = 1 (single edge palindrome)
        // Then we try to extend palindrome by matching edges from i and j with same label

        // Queue for BFS states (i,j)
        ArrayDeque<int[]> queue = new ArrayDeque<>();

        // Initialize dist for edges of length 1 (single edge palindrome)
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] != '-') {
                    dist[i][j] = 1;
                    queue.add(new int[]{i, j});
                }
            }
        }

        // For quick access to edges by label
        // For each vertex, store outgoing edges by label
        // edgesOut[v][c] = list of vertices w where edge v->w has label c
        ArrayList<Integer>[][] edgesOut = new ArrayList[n][26];
        for (int i = 0; i < n; i++) {
            for (int c = 0; c < 26; c++) {
                edgesOut[i][c] = new ArrayList<>();
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                char ch = matrix[i][j];
                if (ch != '-') {
                    edgesOut[i][ch - 'a'].add(j);
                }
            }
        }

        // BFS to find shortest palindrome paths
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int i = cur[0], j = cur[1];
            int curDist = dist[i][j];

            // If i == j, we can try to extend palindrome by adding edges from i and j with same label
            // But also if i != j, we try to extend palindrome by adding edges from i and j with same label
            // The palindrome grows by 2 edges (one from i side and one from j side)
            for (int c = 0; c < 26; c++) {
                for (int ni : edgesOut[i][c]) {
                    for (int nj : edgesOut[j][c]) {
                        if (dist[ni][nj] == -1 || dist[ni][nj] > curDist + 2) {
                            dist[ni][nj] = curDist + 2;
                            queue.add(new int[]{ni, nj});
                        }
                    }
                }
            }
        }

        // Output results
        PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                out.print(dist[i][j]);
                if (j < n - 1) out.print(' ');
            }
            out.println();
        }
        out.flush();
    }
}