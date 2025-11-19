import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int Q = Integer.parseInt(br.readLine());
        long[] prefixSums = new long[Q + 1];
        int front = 0, back = 0;
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < Q; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int opt = Integer.parseInt(st.nextToken());
            if (opt == 1) {
                long l = Long.parseLong(st.nextToken());
                prefixSums[++back] = prefixSums[back - 1] + l;
            } else if (opt == 2) {
                front++;
            } else {
                int k = Integer.parseInt(st.nextToken());
                // head coordinate = prefixSums[front + k - 1] - prefixSums[front]
                sb.append(prefixSums[front + k - 1] - prefixSums[front]).append('\n');
            }
        }
        System.out.print(sb);
    }
}