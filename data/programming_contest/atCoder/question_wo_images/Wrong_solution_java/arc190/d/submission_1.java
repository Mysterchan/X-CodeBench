import java.io.*;
import java.util.*;

public class Main {
    static final int N = 105;
    static long[][] a = new long[N][N], b = new long[N][N], c = new long[N][N];
    static long n, p, k, t;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Long.parseLong(st.nextToken());
        p = Long.parseLong(st.nextToken());

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                a[i][j] = Long.parseLong(st.nextToken());
                if (a[i][j] == 0) k++;
            }
        }

        if (k == 0) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    pw.print(qpow(a[i][j], p, p) + " ");
                }
                pw.println();
            }
            pw.close();
            return;
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                b[i][j] = a[i][j];
                c[i][j] = a[i][j];
            }
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (a[i][j] == 0) {
                    b[i][j] = 1;
                    c[i][j] = p - 1;
                    break;
                }
            }
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                t = 0;
                if (a[i][j] != 0) {
                    t = qpow(a[i][j], p, p);
                } else {
                    t = (qpow(b[i][j], p, p) + qpow(c[i][j], p, p)) % p;
                }
                pw.print(t + " ");
            }
            pw.println();
        }
        pw.close();
    }

    static long qpow(long a, long b, long mod) {
        long res = 1;
        while (b > 0) {
            if ((b & 1) == 1) res = res * a % mod;
            a = a * a % mod;
            b >>= 1;
        }
        return res;
    }
}