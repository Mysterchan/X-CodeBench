import java.util.Scanner;

public class Main {
    static final int MOD = 998244353;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        StringBuilder sb = new StringBuilder();

        while (T-- > 0) {
            int N = sc.nextInt();
            int[][] A = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    A[i][j] = sc.nextInt();
                }
            }
            sb.append(calc(N, A)).append("\n");
        }
        System.out.print(sb);
        sc.close();
    }

    private static int calc(int n, int[][] A) {
        int size = 0;
        int[] degree = new int[n];
        boolean[] visited = new boolean[n];
        boolean isConnected = true;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (A[i][j] == 1) {
                    degree[i]++;
                }
            }
            if (degree[i] == 0) {
                isConnected = false;
            }
        }

        if (!isConnected || degree[0] != n - 1) {
            return 0;
        }

        for (int i = 1; i < n; i++) {
            visited[i] = true;
            size++;
        }

        int result = 1;
        for (int i = 1; i < size; i++) {
            result = result * (i + 1) % MOD;
        }

        return result;
    }
}