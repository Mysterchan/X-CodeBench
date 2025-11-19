import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter writer = new PrintWriter(System.out);
        int T = Integer.parseInt(reader.readLine());

        for (int t = 0; t < T; t++) {
            String[] sizes = reader.readLine().split(" ");
            int H = Integer.parseInt(sizes[0]);
            int W = Integer.parseInt(sizes[1]);
            char[][] grid = new char[H][W];

            for (int i = 0; i < H; i++) {
                grid[i] = reader.readLine().toCharArray();
            }

            int minRepaints = 0;

            for (int i = 0; i < H - 1; i++) {
                for (int j = 0; j < W - 1; j++) {
                    if (grid[i][j] == '#' && grid[i][j + 1] == '#' && grid[i + 1][j] == '#' && grid[i + 1][j + 1] == '#') {
                        minRepaints += 1;  // Repaint one cell in this 2x2 block
                        grid[i][j] = '.';  // Change any cell to white, we can choose any
                    }
                }
            }

            writer.println(minRepaints);
        }

        writer.close();
    }
}