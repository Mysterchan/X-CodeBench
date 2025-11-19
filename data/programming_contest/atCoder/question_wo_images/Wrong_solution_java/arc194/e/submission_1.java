import java.io.*;
import java.util.*;

public class Main {
    static final int INF = 0x3f3f3f3f;
    static final int MOD = 1000000007;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());

        String s = br.readLine();
        String t = br.readLine();

        int[] a = new int[n + 1];
        int[] b = new int[n + 1];

        for (int i = 0; i < n; i++) {
            a[i + 1] = a[i] + (s.charAt(i) == '1' ? 1 : 0);
            b[i + 1] = b[i] + (t.charAt(i) == '1' ? 1 : 0);
        }

        int[][] dp = new int[n + 1][2];

        for (int i = 0; i <= n; i++) {
            dp[i][0] = dp[i][1] = -1;
        }

        dp[0][0] = 0;

        for (int i = 0; i < n; i++) {
            if (dp[i][0] != -1) {
                if (i + x + y <= n) {
                    if (a[i + x + y] - a[i] == x + y && b[i + x + y] - b[i] == y) {
                        dp[i + x + y][1] = Math.max(dp[i + x + y][1], dp[i][0] + x);
                    }
                    if (a[i + x + y] - a[i] == y && b[i + x + y] - b[i] == x + y) {
                        dp[i + x + y][0] = Math.max(dp[i + x + y][0], dp[i][0] + y);
                    }
                }
                if (i + y <= n) {
                    if (a[i + y] - a[i] == y && b[i + y] - b[i] == y) {
                        dp[i + y][0] = Math.max(dp[i + y][0], dp[i][0]);
                    }
                }
            }
            if (dp[i][1] != -1) {
                if (i + x + y <= n) {
                    if (a[i + x + y] - a[i] == x && b[i + x + y] - b[i] == x) {
                        dp[i + x + y][1] = Math.max(dp[i + x + y][1], dp[i][1]);
                    }
                    if (a[i + x + y] - a[i] == x + y && b[i + x + y] - b[i] == y) {
                        dp[i + x + y][0] = Math.max(dp[i + x + y][0], dp[i][1] + y);
                    }
                }
                if (i + x <= n) {
                    if (a[i + x] - a[i] == x && b[i + x] - b[i] == x) {
                        dp[i + x][1] = Math.max(dp[i + x][1], dp[i][1]);
                    }
                }
            }
        }

        boolean ok = true;
        for (int i = 0; i <= n; i++) {
            if (a[i] != b[i]) {
                ok = false;
                break;
            }
        }

        if (ok) {
            out.println("Yes");
        } else {
            out.println("No");
        }

        out.close();
    }
}