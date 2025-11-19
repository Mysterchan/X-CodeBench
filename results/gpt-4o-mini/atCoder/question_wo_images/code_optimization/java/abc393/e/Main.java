import java.io.*;
import java.util.*;

public class Main {
    static class MyScanner {
        static BufferedReader r;
        static StringTokenizer st;
        
        public MyScanner() {
            r = new BufferedReader(new InputStreamReader(System.in));
        }
        
        public String next() {
            try {
                while (st == null || !st.hasMoreTokens()) {
                    st = new StringTokenizer(r.readLine());
                }
                return st.nextToken();
            } catch (Exception e) {
                return null;
            }
        }
        
        public int nextInt() {
            return Integer.parseInt(next());
        }
    }

    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static MyScanner sc = new MyScanner();
    static int N, K;
    static final int MAXN = 1000001;  // Maximum value of A_i
    static int[] countDivisors = new int[MAXN];

    public static void main(String[] args) throws IOException {
        N = sc.nextInt();
        K = sc.nextInt();
        int[] a = new int[N];

        // Read the input array A
        for (int i = 0; i < N; i++) {
            a[i] = sc.nextInt();
        }

        // Count occurrences of each number in A
        for (int num : a) {
            countDivisors[num]++;
        }

        // Process each number in A to find the maximum GCD for each A[i]
        for (int i = 0; i < N; i++) {
            int maxGCD = 1;  // At least 1 can be a GCD
            
            // Check all divisors from the current A[i] down to 1
            for (int d = a[i]; d > 0; d--) {
                if (countDivisors[d] >= K) {
                    maxGCD = d;
                    break;  // Found the maximum GCD for A[i]
                }
            }
            bw.write(maxGCD + "\n");
        }
        bw.flush();
    }
}