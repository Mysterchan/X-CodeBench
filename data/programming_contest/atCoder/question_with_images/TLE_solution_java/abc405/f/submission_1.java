import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] segments = new int[M][2];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            segments[i][0] = a;
            segments[i][1] = b;
        }

        int Q = Integer.parseInt(br.readLine());

        for (int q = 0; q < Q; q++) {
            st = new StringTokenizer(br.readLine());
            int c = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());

            int count = 0;

            for (int i = 0; i < M; i++) {
                if (intersects(segments[i][0], segments[i][1], c, d, 2 * N)) {
                    count++;
                }
            }

            pw.println(count);
        }

        pw.flush();
        pw.close();
        br.close();
    }

    static boolean intersects(int a, int b, int c, int d, int maxPoint) {

        if (a > b) {
            int temp = a; a = b; b = temp;
        }
        if (c > d) {
            int temp = c; c = d; d = temp;
        }

        boolean cBetweenAB = isBetweenInCircle(a, b, c, maxPoint);

        boolean dBetweenAB = isBetweenInCircle(a, b, d, maxPoint);

        return cBetweenAB != dBetweenAB;
    }

    static boolean isBetweenInCircle(int a, int b, int x, int maxPoint) {
        if (a <= b) {

            return a < x && x < b;
        } else {

            return x > a || x < b;
        }
    }
}