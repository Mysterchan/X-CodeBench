import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine().trim());
        long[] A = new long[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Long.parseLong(st.nextToken());
        }

        final long NEG_INF = Long.MIN_VALUE / 4;
        long dpEven = 0;
        long dpOdd  = NEG_INF;

        for (int i = 1; i <= N; i++) {
            long val = A[i - 1];

            if ((i & 1) == 1) {

                long newDpOdd = dpOdd;
                if (dpEven != NEG_INF) {
                    newDpOdd = Math.max(newDpOdd, dpEven + val);
                }
                dpOdd = newDpOdd;

            } else {

                long newDpEven = dpEven;
                if (dpOdd != NEG_INF) {
                    newDpEven = Math.max(newDpEven, dpOdd + val);
                }
                dpEven = newDpEven;

            }
        }

        long answer = ((N & 1) == 0) ? dpEven : dpOdd;
        System.out.println(answer);
    }
}