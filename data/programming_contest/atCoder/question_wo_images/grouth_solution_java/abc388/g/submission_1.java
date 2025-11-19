import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main {

    static long[] A;
    static int[] d;
    static int[] segTree;

    static int lowerBound(int start, int end, long target) {
        int low = start;
        int high = end;
        int ans = end + 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (A[mid] >= target) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }

    static void build(int v, int tl, int tr) {
        if (tl == tr) {
            segTree[v] = d[tl];
        } else {
            int tm = (tl + tr) / 2;
            build(2 * v, tl, tm);
            build(2 * v + 1, tm + 1, tr);
            segTree[v] = Math.max(segTree[2 * v], segTree[2 * v + 1]);
        }
    }

    static int query(int v, int tl, int tr, int ql, int qr) {
        if (ql > qr) {
            return 0;
        }
        if (tl == ql && tr == qr) {
            return segTree[v];
        }
        int tm = (tl + tr) / 2;
        return Math.max(
                query(2 * v, tl, tm, ql, Math.min(qr, tm)),
                query(2 * v + 1, tm + 1, tr, Math.max(ql, tm + 1), qr)
        );
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);

        int N = Integer.parseInt(br.readLine());
        A = new long[N + 1];
        d = new int[N + 1];
        segTree = new int[4 * (N + 1)];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            A[i] = Long.parseLong(st.nextToken());
        }

        for (int j = 1; j <= N; j++) {
            long target = 2L * A[j];
            int k = lowerBound(j + 1, N, target);
            if (k > N) {
                d[j] = N + 1;
            } else {
                d[j] = k - j;
            }
        }

        build(1, 1, N);

        int Q = Integer.parseInt(br.readLine());
        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine());
            int L = Integer.parseInt(st.nextToken());
            int R = Integer.parseInt(st.nextToken());

            int Nq = R - L + 1;
            int Kmax = Nq / 2;

            int low = 0;
            int high = Kmax;
            int ans = 0;

            while (low <= high) {
                int K = low + (high - low) / 2;
                if (K == 0) {
                    ans = K;
                    low = K + 1;
                    continue;
                }

                int d_required = Nq - K;
                int max_d_needed = query(1, 1, N, L, L + K - 1);

                if (max_d_needed <= d_required) {
                    ans = K;
                    low = K + 1;
                } else {
                    high = K - 1;
                }
            }
            out.println(ans);
        }
        out.flush();
    }
}