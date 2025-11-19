import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);

        StringTokenizer st = new StringTokenizer(br.readLine());
        int H = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());

        int[][] A = new int[H][W];
        for (int i = 0; i < H; i++) {
            String line = br.readLine();
            for (int j = 0; j < W; j++) {
                A[i][j] = line.charAt(j) - '0';
            }
        }

        int[] col_sum = new int[W];
        for (int j = 0; j < W; j++) {
            for (int i = 0; i < H; i++) {
                col_sum[j] += A[i][j];
            }
        }

        int[] dp = new int[1 << W];
        Arrays.fill(dp, Integer.MAX_VALUE / 2);
        dp[0] = 0;
        for (int i = 0; i < H; i++) {
            int[] next_dp = new int[1 << W];
            Arrays.fill(next_dp, Integer.MAX_VALUE / 2);
            for (int bit = 0; bit < (1 << W); bit++) {
                int sum = 0;
                for (int j = 0; j < W; j++) {
                    if ((bit & (1 << j)) == 0) {
                        sum += A[i][j];
                    } else {
                        sum += 1 - A[i][j];
                    }
                }
                sum = Math.min(sum, H - sum);
                for (int bit2 = 0; bit2 < (1 << W); bit2++) {
                    int new_bit = 0;
                    for (int j = 0; j < W; j++) {
                        if ((bit & (1 << j)) == 0 && (bit2 & (1 << j)) == 0) {
                            new_bit |= (1 << j);
                        }
                    }
                    next_dp[new_bit] = Math.min(next_dp[new_bit], dp[bit2] + sum);
                }
            }
            dp = next_dp;
        }

        int ans = Integer.MAX_VALUE / 2;
        for (int bit = 0; bit < (1 << W); bit++) {
            int sum = 0;
            for (int j = 0; j < W; j++) {
                if ((bit & (1 << j)) == 0) {
                    sum += col_sum[j];
                } else {
                    sum += H - col_sum[j];
                }
            }
            sum = Math.min(sum, H * W - sum);
            ans = Math.min(ans, dp[bit] + sum);
        }

        pw.println(ans);

        pw.close();
    }
}