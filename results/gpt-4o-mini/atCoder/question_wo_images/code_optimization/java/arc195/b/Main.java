import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        FastReader sc = new FastReader();
        int n = sc.nextInt();
        long[] a = new long[n], b = new long[n];
        long sumA = 0, sumB = 0;
        int sA = 0, sB = 0;

        for (int i = 0; i < n; i++) {
            a[i] = sc.nextLong();
            if (a[i] == -1) sA++;
            else sumA += a[i];
        }
        for (int i = 0; i < n; i++) {
            b[i] = sc.nextLong();
            if (b[i] == -1) sB++;
            else sumB += b[i];
        }

        long totalRequired = sumA + sumB + sA + sB;
        if (totalRequired % n != 0) {
            System.out.println("No");
            return;
        }

        long target = totalRequired / n;

        // Check if we can adjust A and B to match the target
        long needA = 0, needB = 0;
        for (int i = 0; i < n; i++) {
            if (a[i] != -1) needA += target - a[i];
            if (b[i] != -1) needB += target - b[i];
        }

        if (needA <= sA && needB <= sB) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }
    }
}