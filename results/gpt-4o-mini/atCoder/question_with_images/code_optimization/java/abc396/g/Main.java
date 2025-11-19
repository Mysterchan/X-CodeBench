import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int H = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());

        int[][] A = new int[H][W];
        for (int i = 0; i < H; i++) {
            String s = br.readLine();
            for (int j = 0; j < W; j++) {
                A[i][j] = s.charAt(j) - '0';
            }
        }

        int[] colSum = new int[W];
        for (int j = 0; j < W; j++) {
            for (int i = 0; i < H; i++) {
                colSum[j] += A[i][j];
            }
        }

        int min = H * W;
        for (int i = 0; i < (1 << W); i++) {
            int total = 0;
            for (int j = 0; j < W; j++) {
                int countOnes = colSum[j];
                if ((i & (1 << j)) != 0) {
                    countOnes = H - countOnes; // Flip the column
                }
                total += Math.min(countOnes, H - countOnes);
            }
            min = Math.min(min, total);
        }

        System.out.println(min);
    }
}