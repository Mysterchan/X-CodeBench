import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);

        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        long[] A = new long[N];
        for (int i = 0; i < N; i++) {
            A[i] = Long.parseLong(st.nextToken());
        }

        long xor = 0;
        for (long a : A) {
            xor ^= a;
        }

        Set<Long> set = new HashSet<>();
        for (long i = 0; i < (1 << N); i++) {
            long temp = 0;
            for (int j = 0; j < N; j++) {
                if (((i >> j) & 1) == 1) {
                    temp ^= A[j];
                }
            }
            set.add(temp);
        }

        long ans = 0;
        for (long x : set) {
            if (x == 0) continue;
            long temp = 0;
            for (int i = 0; i < 60; i++) {
                if (((x >> i) & 1) == 1) {
                    temp ^= (xor >> i);
                }
            }
            if (temp == x) {
                ans++;
            }
        }

        pw.println(ans + 1);

        pw.close();
    }
}