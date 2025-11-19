import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
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
    }

    public static void main(String[] args) {
        FastReader reader = new FastReader();
        int n = reader.nextInt();
        int[][] ranges = new int[n][2];
        for (int i = 0; i < n; i++) {
            ranges[i][0] = reader.nextInt();
            ranges[i][1] = reader.nextInt();
        }
        int q = reader.nextInt();
        int[] queries = new int[q];
        for (int i = 0; i < q; i++) {
            queries[i] = reader.nextInt();
        }

        int max = 500000;
        int[] diff = new int[max + 2];
        for (int[] range : ranges) {
            diff[range[0]]++;
            diff[range[1] + 1]--;
        }

        for (int i = 1; i <= max + 1; i++) {
            diff[i] += diff[i - 1];
        }

        for (int i = 1; i <= max + 1; i++) {
            diff[i] += diff[i - 1];
        }

        StringBuilder sb = new StringBuilder();
        for (int query : queries) {
            sb.append(diff[query]).append('\n');
        }

        System.out.println(sb);
    }
}