import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br;
    static PrintWriter out;
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        out = new PrintWriter(System.out);

        int Q = readInt();
        int[] A = new int[Q];
        int[] B = new int[Q];

        for (int i = 0; i < Q; i++) {
            A[i] = readInt();
            B[i] = readInt();
        }

        BitSet removed = new BitSet(100001); // Using BitSet to mark removed multiples
        for (int i = 0; i < Q; i++) {
            int a_i = A[i];
            int b_i = B[i];

            // Remove multiples of a_i
            for (int j = a_i; j <= 100000; j += a_i) {
                removed.set(j);
            }

            // Find the b_i-th smallest positive integer not removed
            int count = 0;
            for (int num = 1; ; num++) {
                if (!removed.get(num)) {
                    count++;
                    if (count == b_i) {
                        out.println(num);
                        break;
                    }
                }
            }
        }

        out.close();
    }

    static String next() throws IOException {
        while (st == null || !st.hasMoreTokens())
            st = new StringTokenizer(br.readLine());
        return st.nextToken();
    }

    static int readInt() throws IOException {
        return Integer.parseInt(next());
    }
}