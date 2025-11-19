import java.io.*;
import java.util.*;

public class Main {
    static final int INF = 0x3f3f3f3f;
    static final int MOD = 1000000007;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        int t = 1;
        while (t-- > 0) {
            solve(br, out);
        }
        out.close();
    }

    static void solve(BufferedReader br, PrintWriter out) throws IOException {
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        long[] p = new long[n];
        for (int i = 0; i < n; i++) {
            p[i] = Long.parseLong(st.nextToken()) - 1;
        }
        long ans = 0;
        for (int i = 0; i < n; i++) {
            if (p[i] != i) {
                ans += i + 1;
                for (int j = i; j > 0; j--) {
                    long temp = p[j];
                    p[j] = p[j - 1];
                    p[j - 1] = temp;
                }
                i--;
            }
        }
        out.println(ans);
    }
}