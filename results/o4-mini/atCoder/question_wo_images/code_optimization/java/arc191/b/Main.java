import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter    pw = new PrintWriter(System.out);
        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            long N = Long.parseLong(st.nextToken());
            long K = Long.parseLong(st.nextToken());
            // Find the highest set bit position of N
            int msb = 63 - Long.numberOfLeadingZeros(N);
            // Collect positions below msb where N has a zero bit
            int[] zeroPos = new int[msb];
            int c = 0;
            for (int i = 0; i < msb; i++) {
                if (((N >> i) & 1) == 0) {
                    zeroPos[c++] = i;
                }
            }
            // Total compatible X is 2^c
            long total = 1L << c;
            if (K > total) {
                pw.println(-1);
            } else {
                long s = K - 1;  // zero-based index in the subset enumeration
                long Y = 0;
                for (int j = 0; j < c; j++) {
                    if (((s >> j) & 1) == 1) {
                        Y |= (1L << zeroPos[j]);
                    }
                }
                long X = N + Y;
                pw.println(X);
            }
        }
        pw.flush();
    }
}