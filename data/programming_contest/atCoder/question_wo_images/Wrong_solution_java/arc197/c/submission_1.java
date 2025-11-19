import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br;
    static PrintWriter out;
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        out = new PrintWriter(new OutputStreamWriter(System.out));

        int T = readInt();
        int[] a = new int[T];
        int[] b = new int[T];
        int range = 0;

        for (int j = 0; j < T; j++) {
            a[j] = readInt();
            b[j] = readInt();
            range = Math.max(range, b[j]);
        }

        Set<Integer> fins = new TreeSet<>();
        HashMap<Integer, Integer> map = new HashMap<>();
        int p = b[0];

        for (int i = 0; i < T; i++) {
            map.put(a[i], 0);
            for (Map.Entry<Integer, Integer> en : map.entrySet()) {
                int key = en.getKey();
                int j = en.getValue() + 1;
                for (; key * j <= p; j++) {
                    fins.add(key * j);
                }
                map.put(key, j - 1);
            }

            p = b[i];
            for (int e : fins) {
                if (e < p) {
                    p++;
                } else {
                    break;
                }
            }

            out.println(p);
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