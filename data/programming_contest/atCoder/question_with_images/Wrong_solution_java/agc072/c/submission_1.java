import java.util.Scanner;

public class Main {
    static long[][] C;
    static final int MAX = 205;
    static final long INF = (long)1e18 + 1;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        long K = sc.nextLong();

        C = new long[MAX][MAX];
        for (int i = 0; i < MAX; i++) {
            C[i][0] = 1;
            for (int j = 1; j <= i; j++) {
                C[i][j] = Math.min(C[i - 1][j - 1] + C[i - 1][j], INF);
            }
        }

        int d = N - 1;
        int r = N - 1;
        StringBuilder sb = new StringBuilder();

        while (d > 0 || r > 0) {
            if (d == 0) {
                sb.append('R');
                r--;
            } else if (r == 0) {
                sb.append('D');
                d--;
            } else {
                long count = C[d + r - 1][d - 1];
                if (K <= count) {
                    sb.append('D');
                    d--;
                } else {
                    sb.append('R');
                    K -= count;
                    r--;
                }
            }
        }

        System.out.println(sb.toString());
    }
}