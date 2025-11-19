import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main {
    static final int MOD = 1000000007;
    static long[] inv;

    // Precompute inverses up to max needed (100000)
    static void precomputeInverses(int max) {
        inv = new long[max + 1];
        inv[1] = 1;
        for (int i = 2; i <= max; i++) {
            inv[i] = MOD - (MOD / i) * inv[MOD % i] % MOD;
        }
    }

    // Compute nCr modulo MOD using precomputed inverses
    static long nCrMod(long n, int r) {
        // nCr = n*(n-1)*...*(n-r+1) / r!
        long res = 1;
        for (long i = n - r + 1; i <= n; i++) {
            res = (res * (i % MOD)) % MOD;
        }
        for (int i = 2; i <= r; i++) {
            res = (res * inv[i]) % MOD;
        }
        return res;
    }

    public static void main(String[] args) throws IOException {
        // Precompute inverses once
        precomputeInverses(100000);

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            // n = (a-1)*k + 1
            long n = ((long)(a - 1) * k + 1) % MOD;

            // m = C(n, a) * k * (b-1) + 1
            // Compute C(n, a) modulo MOD
            long comb = nCrMod(((long)(a - 1) * k + 1), a);
            long m = (comb * k) % MOD;
            m = (m * (b - 1)) % MOD;
            m = (m + 1) % MOD;

            pw.println(n + " " + m);
        }
        pw.close();
    }
}