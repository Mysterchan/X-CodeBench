import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);

        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        int[] cnt = new int[N];
        for (int i = N - 1; i >= 0; i--) {
            int lo = 0;
            int hi = i;
            while (lo < hi) {
                int mid = (lo + hi + 1) / 2;
                if (A[mid] * 2 <= A[i]) {
                    lo = mid;
                } else {
                    hi = mid - 1;
                }
            }
            if (lo < i) {
                cnt[i] = 1 + cnt[lo];
            } else {
                cnt[i] = 0;
            }
        }

        int Q = Integer.parseInt(br.readLine());
        for (int q = 0; q < Q; q++) {
            st = new StringTokenizer(br.readLine());
            int L = Integer.parseInt(st.nextToken()) - 1;
            int R = Integer.parseInt(st.nextToken()) - 1;
            pw.println(cnt[L] - (R - L + 1) + 1);
        }

        pw.close();
    }
}