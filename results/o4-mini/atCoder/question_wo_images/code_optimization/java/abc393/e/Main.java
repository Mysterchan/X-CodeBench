import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] A = new int[N];
        st = new StringTokenizer(br.readLine());
        int maxA = 0;
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
            if (A[i] > maxA) maxA = A[i];
        }

        // freq[x] = number of times x appears in A
        int[] freq = new int[maxA + 1];
        for (int x : A) {
            freq[x]++;
        }

        // cnt[d] = number of elements in A divisible by d
        int[] cnt = new int[maxA + 1];
        for (int d = 1; d <= maxA; d++) {
            for (int m = d; m <= maxA; m += d) {
                cnt[d] += freq[m];
            }
        }

        // ans[x] = maximum d dividing x with cnt[d] >= K
        int[] ans = new int[maxA + 1];
        // Since 1 always divides every A[i] and cnt[1] = N >= K, every ans[x] >= 1
        // We iterate d from 1..maxA so larger d overwrite smaller
        for (int d = 1; d <= maxA; d++) {
            if (cnt[d] >= K) {
                for (int m = d; m <= maxA; m += d) {
                    ans[m] = d;
                }
            }
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int x : A) {
            bw.write(ans[x] + "\n");
        }
        bw.flush();
    }
}