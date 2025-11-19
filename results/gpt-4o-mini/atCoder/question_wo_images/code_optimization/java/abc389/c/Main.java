import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int Q = Integer.parseInt(br.readLine());
        long[] queue = new long[Q];
        long offset = 0;
        int size = 0;
        int front = 0;

        for (int i = 0; i < Q; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int opt = Integer.parseInt(st.nextToken());
            if (opt == 1) {
                long l = Long.parseLong(st.nextToken());
                queue[size++] = (size == 1) ? 0 : queue[size - 1] + l;
            } else if (opt == 2) {
                offset += queue[front++];
            } else {
                int k = Integer.parseInt(st.nextToken());
                System.out.println(queue[front + k - 1] - offset);
            }
        }
    }
}