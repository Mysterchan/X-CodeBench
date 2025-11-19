import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        long[] A = new long[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Long.parseLong(st.nextToken());
        }

        int Q = Integer.parseInt(br.readLine());
        int[][] queries = new int[Q][2];
        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine());
            queries[i][0] = Integer.parseInt(st.nextToken()) - 1; // Convert to 0-based index
            queries[i][1] = Integer.parseInt(st.nextToken()) - 1; // Convert to 0-based index
        }

        StringBuilder sb = new StringBuilder();
        for (int[] query : queries) {
            int L = query[0];
            int R = query[1];
            int count = 0;

            // Use two pointers to find valid pairs
            int i = L, j = L;
            while (i <= R) {
                // Move j to find a valid mochi that can be paired with A[i]
                while (j <= R && A[j] < 2 * A[i]) {
                    j++;
                }
                // Count how many mochi can be paired with A[i]
                count += (j - i - 1);
                i++;
            }

            // Each pair contributes to one kagamimochi
            sb.append(count / 2).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
    }
}