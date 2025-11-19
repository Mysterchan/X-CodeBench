import java.util.*;

public class Main {
    static final int MOD = 998244353;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(), M = sc.nextInt();

        int[][] perms = new int[M][N];
        for (int i = 0; i < M; i++)
            for (int j = 0; j < N; j++)
                perms[i][j] = sc.nextInt() - 1;

        boolean[][] ok = new boolean[N][N];
        for (int i = 0; i < N; i++)
            Arrays.fill(ok[i], true);

        for (int p = 0; p < M; p++) {
            int[] pos = new int[N];
            for (int i = 0; i < N; i++)
                pos[perms[p][i]] = i;

            for (int u = 0; u < N; u++) {
                for (int v = u + 1; v < N; v++) {
                    for (int x = 0; x < N; x++) {
                        for (int y = x + 1; y < N; y++) {
                            if (u == x || u == y || v == x || v == y) continue;
                            int a = pos[u], b = pos[v];
                            int c = pos[x], d = pos[y];
                            if (intersect(a, b, c, d, N)) {
                                ok[u][v] = ok[v][u] = false;
                            }
                        }
                    }
                }
            }
        }

        long[][] lap = new long[N][N];
        for (int u = 0; u < N; u++) {
            for (int v = u + 1; v < N; v++) {
                if (ok[u][v]) {
                    lap[u][u]++;
                    lap[v][v]++;
                    lap[u][v]--;
                    lap[v][u]--;
                }
            }
        }

        long[][] mat = new long[N - 1][N - 1];
        for (int i = 0; i < N - 1; i++)
            for (int j = 0; j < N - 1; j++)
                mat[i][j] = (lap[i][j] + MOD) % MOD;

        System.out.println(determinant(mat, MOD));
    }

    static boolean intersect(int a, int b, int c, int d, int N) {
        if (a > b) { int t = a; a = b; b = t; }
        if (c > d) { int t = c; c = d; d = t; }
        return (a < c && c < b && b < d) || (c < a && a < d && d < b);
    }

    static long determinant(long[][] a, int mod) {
        int n = a.length;
        long det = 1;
        for (int i = 0; i < n; i++) {
            int pivot = i;
            for (int j = i + 1; j < n; j++) {
                if (a[j][i] != 0) {
                    pivot = j;
                    break;
                }
            }
            if (a[pivot][i] == 0) return 0;
            if (i != pivot) {
                long[] temp = a[i]; a[i] = a[pivot]; a[pivot] = temp;
                det = (mod - det) % mod;
            }
            det = det * a[i][i] % mod;
            long inv = modInverse(a[i][i], mod);
            for (int j = i + 1; j < n; j++) {
                long factor = a[j][i] * inv % mod;
                for (int k = i; k < n; k++) {
                    a[j][k] = (a[j][k] - factor * a[i][k]) % mod;
                    if (a[j][k] < 0) a[j][k] += mod;
                }
            }
        }
        return det;
    }

    static long modInverse(long a, int mod) {
        return pow(a, mod - 2, mod);
    }

    static long pow(long a, long b, int mod) {
        long res = 1;
        a %= mod;
        while (b > 0) {
            if ((b & 1) == 1) res = res * a % mod;
            a = a * a % mod;
            b >>= 1;
        }
        return res;
    }
}