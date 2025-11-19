import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // Use BufferedReader and BufferedWriter for faster IO
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int H = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        // Store obstacles in a HashSet for O(1) lookup
        // Encode position as (row * W + col)
        HashSet<Integer> obstacles = new HashSet<>(K);
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken()) - 1;
            obstacles.add(r * W + c);
        }
        br.close();

        // If start or goal is blocked (problem states they are not, but just in case)
        if (obstacles.contains(0) || obstacles.contains((H - 1) * W + (W - 1))) {
            System.out.println("No");
            return;
        }

        // BFS using primitive arrays and a boolean visited array
        boolean[] visited = new boolean[H * W];
        int[] dh = {-1, 1, 0, 0};
        int[] dw = {0, 0, -1, 1};

        ArrayDeque<Integer> queue = new ArrayDeque<>();
        queue.add(0);
        visited[0] = true;

        while (!queue.isEmpty()) {
            int pos = queue.pollFirst();
            int r = pos / W;
            int c = pos % W;

            if (r == H - 1 && c == W - 1) {
                System.out.println("Yes");
                return;
            }

            for (int i = 0; i < 4; i++) {
                int nr = r + dh[i];
                int nc = c + dw[i];
                if (nr >= 0 && nr < H && nc >= 0 && nc < W) {
                    int npos = nr * W + nc;
                    if (!visited[npos] && !obstacles.contains(npos)) {
                        visited[npos] = true;
                        queue.add(npos);
                    }
                }
            }
        }

        System.out.println("No");
    }
}