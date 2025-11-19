import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br;
    static PrintWriter out;
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        out = new PrintWriter(System.out);

        int T = readInt();
        int[] a = new int[T];
        int[] b = new int[T];

        for (int i = 0; i < T; i++) {
            a[i] = readInt();
            b[i] = readInt();
        }

        TreeSet<Integer> removed = new TreeSet<>();

        for (int i = 0; i < T; i++) {
            int ai = a[i];
            int bi = b[i];

            int multiple = ai;
            while (multiple <= 1000000) {
                removed.add(multiple);
                multiple += ai;
            }

            int count = 0;
            int num = 1;

            while (true) {
                if (!removed.contains(num)) {
                    count++;
                    if (count == bi) {
                        out.println(num);
                        break;
                    }
                }
                num++;
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