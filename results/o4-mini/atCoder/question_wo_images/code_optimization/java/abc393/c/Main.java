import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long n = Long.parseLong(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        long[] edges = new long[m];
        int k = 0;
        long removals = 0;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            if (u == v) {
                // self-loop, must remove
                removals++;
            } else {
                // encode unordered pair
                int a = u < v ? u : v;
                int b = u < v ? v : u;
                edges[k++] = ((long)a << 32) | (b & 0xffffffffL);
            }
        }
        // sort the non-loop edges
        if (k > 0) {
            Arrays.sort(edges, 0, k);
            // count unique edges
            long unique = 1;
            long prev = edges[0];
            for (int i = 1; i < k; i++) {
                long cur = edges[i];
                if (cur != prev) {
                    unique++;
                    prev = cur;
                }
            }
            // duplicates = total non-loops - unique distinct
            removals += (k - unique);
        }
        PrintWriter out = new PrintWriter(System.out);
        out.println(removals);
        out.flush();
    }
}