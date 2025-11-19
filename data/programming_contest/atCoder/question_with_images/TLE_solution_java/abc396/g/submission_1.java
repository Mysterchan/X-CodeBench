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

        int[] rowSum = new int[H];
        int[] colSum = new int[W];
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                rowSum[i] += A[i][j];
                colSum[j] += A[i][j];
            }
        }

        int min = H * W;
        for (int i = 0; i < (1 << W); i++) {
            int tmp = 0;
            for (int j = 0; j < H; j++) {
                int cnt = 0;
                for (int k = 0; k < W; k++) {
                    if (((i >> k) & 1) == 1) {
                        cnt += (1 - A[j][k]);
                    } else {
                        cnt += A[j][k];
                    }
                }
                tmp += Math.min(cnt, W - cnt);
            }
            min = Math.min(min, tmp);
        }

        System.out.println(min);
    }
}