import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br;
    static BufferedWriter bw;
    static StringTokenizer st;
    static int N, K;
    static final int MAXA = 1_000_000;
    static int[] a;
    static int[] freq = new int[MAXA + 1];
    static int[] countDiv = new int[MAXA + 1];

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        a = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            a[i] = Integer.parseInt(st.nextToken());
            freq[a[i]]++;
        }

        // countDiv[d] = number of elements divisible by d
        for (int d = 1; d <= MAXA; d++) {
            int sum = 0;
            for (int multiple = d; multiple <= MAXA; multiple += d) {
                sum += freq[multiple];
            }
            countDiv[d] = sum;
        }

        // For each element, find max divisor d of a[i] with countDiv[d] >= K
        // To do this efficiently, precompute divisors for each a[i] on the fly
        // and pick the max divisor with countDiv[d] >= K

        // Since max a[i] <= 1e6, number of divisors per element is small (~100 max)
        // So this is efficient enough.

        for (int i = 0; i < N; i++) {
            int x = a[i];
            int ans = 1;
            // Enumerate divisors of x
            int limit = (int) Math.sqrt(x);
            for (int d = 1; d <= limit; d++) {
                if (x % d == 0) {
                    int d1 = d;
                    int d2 = x / d;
                    if (countDiv[d1] >= K && d1 > ans) ans = d1;
                    if (countDiv[d2] >= K && d2 > ans) ans = d2;
                }
            }
            bw.write(ans + "\n");
        }
        bw.flush();
    }
}