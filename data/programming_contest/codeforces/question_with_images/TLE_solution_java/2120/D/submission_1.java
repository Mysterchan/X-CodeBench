import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        final int MOD = 1000000007;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        int tc = Integer.parseInt(br.readLine());
        while(tc-- > 0) {
            long[] inverses = new long[100010];
            inverses[1] = 1;
            for(int i = 2; i < inverses.length; i++) {
                inverses[i] = MOD - (long) (MOD / i) * inverses[MOD % i] % MOD;
            }

            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            long n = ((long) (a - 1) * k + 1);
            long m = 1;
            for(long i = n - a + 1; i <= n; i++) {
                m = ((m * (i % MOD)) % MOD);
            }

            for(int i = a; i >= 2; i--) {
                m = (inverses[i] * m) % MOD;
            }

            m = (m * k) % MOD;
            m = (m * (b - 1)) % MOD;
            int n1 = (int) (n % MOD);
            int m1 = (int) ((m+1) % MOD);

            pw.println(n1 + " " + m1);
        }
        pw.close();
    }
}
