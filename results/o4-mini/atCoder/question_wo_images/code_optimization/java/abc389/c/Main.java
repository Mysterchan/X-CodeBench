import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int Q = Integer.parseInt(br.readLine());
        long[] prefix = new long[Q + 5];
        int front = 0, back = 0;
        StringBuilder sb = new StringBuilder();
        for (int qi = 0; qi < Q; qi++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int type = Integer.parseInt(st.nextToken());
            if (type == 1) {
                long l = Long.parseLong(st.nextToken());
                back++;
                prefix[back] = prefix[back - 1] + l;
            } else if (type == 2) {
                // remove front snake
                front++;
            } else {
                int k = Integer.parseInt(st.nextToken());
                // head of k-th snake = original head at index front+k-1 minus shift prefix[front]
                long ans = prefix[front + k - 1] - prefix[front];
                sb.append(ans).append('\n');
            }
        }
        System.out.print(sb);
    }
}