import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        long k = Long.parseLong(input[1]);

        StringBuilder path = new StringBuilder();
        int[] down = new int[n];
        int[] right = new int[n];

        long totalPaths = 1; // To count total unique paths possibilities
        for (int i = 1; i < n; i++) {
            totalPaths *= 2; // Each step can go either right or down
        }

        // Calculate the path for K-th exercise
        for (int step = 0; step < 2 * (n - 1); step++) {
            // How many total paths can be made from the current position (down & right remaining)
            long downCount = Math.min(n - 1, step + 1) - down[step % 2];
            long rightCount = Math.min(n - 1, step + 1) - right[step % 2];

            if (downCount > 0) {
                long leftPaths = totalPaths / (downCount + 1);
                if (k <= leftPaths) {
                    path.append('D');
                    down[step % 2]++;
                } else {
                    path.append('R');
                    k -= leftPaths;
                    right[step % 2]++;
                }
            } else {
                path.append('R');
                right[step % 2]++;
            }
        }

        System.out.println(path.toString());
    }
}