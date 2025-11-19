import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    static int N, Q;
    static long[] A;
    static int[] next; // next[i]: smallest j > i with A[j] >= 2*A[i]
    static int[] dp;   // dp[i]: max pairs from i to end

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        A = new long[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Long.parseLong(st.nextToken());
        }

        // Precompute next[i] using two pointers
        next = new int[N];
        int j = 0;
        for (int i = 0; i < N; i++) {
            while (j < N && A[j] < 2 * A[i]) j++;
            next[i] = j;
        }

        // dp[i]: max pairs from i to end
        dp = new int[N + 1];
        dp[N] = 0;
        for (int i = N - 1; i >= 0; i--) {
            // Option 1: skip i
            int res = dp[i + 1];
            // Option 2: pair i with next[i] if possible
            if (next[i] < N) {
                res = Math.max(res, 1 + dp[next[i] + 1]);
            }
            dp[i] = res;
        }

        Q = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int _q = 0; _q < Q; _q++) {
            st = new StringTokenizer(br.readLine());
            int L = Integer.parseInt(st.nextToken()) - 1;
            int R = Integer.parseInt(st.nextToken()) - 1;

            // We want max pairs in A[L..R]
            // Use binary search on dp to find max pairs in [L,R]
            // We'll do a binary search on number of pairs k:
            // Check if dp[L] can form k pairs within R

            // But dp is global, so we need a way to get dp restricted to [L,R].
            // We'll do a binary search on answer k in [0, (R-L+1)/2]

            int left = 0, right = (R - L + 1) / 2;
            int ans = 0;
            while (left <= right) {
                int mid = (left + right) / 2;
                if (canForm(L, R, mid)) {
                    ans = mid;
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
            sb.append(ans).append('\n');
        }

        bw.write(sb.toString());
        bw.flush();
    }

    // Check if we can form k pairs in A[L..R]
    // We'll greedily try to form k pairs starting from L
    static boolean canForm(int L, int R, int k) {
        int count = 0;
        int i = L;
        while (i <= R && count < k) {
            int nxt = next[i];
            if (nxt > R) return false;
            count++;
            i = nxt + 1;
        }
        return count == k;
    }
}