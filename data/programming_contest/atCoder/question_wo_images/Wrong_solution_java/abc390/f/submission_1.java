import java.util.*;
import java.io.*;

public class Main {
    static class SegTree {
        int N;
        long[] tree;
        long INF = (long) 1e18;

        SegTree(int n) {
            N = 1;
            while (N < n) N <<= 1;
            tree = new long[N << 1];
            Arrays.fill(tree, INF);
        }

        void update(int i, long val) {
            i += N;
            tree[i] = val;
            while (i > 1) {
                i >>= 1;
                tree[i] = Math.min(tree[i << 1], tree[(i << 1) | 1]);
            }
        }

        long query(int l, int r) {
            l += N;
            r += N;
            long ans = INF;
            while (l <= r) {
                if ((l & 1) == 1) ans = Math.min(ans, tree[l++]);
                if ((r & 1) == 0) ans = Math.min(ans, tree[r--]);
                l >>= 1;
                r >>= 1;
            }
            return ans;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[] A = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken()) - 1;
        }

        long ans = 0;
        int[] last = new int[N];
        Arrays.fill(last, -1);
        SegTree seg = new SegTree(N);
        seg.update(0, 0);
        for (int i = 0; i < N; i++) {
            int k = last[A[i]];
            if (k == -1) {
                ans += (i + 1);
                seg.update(i, i - seg.query(0, i - 1));
            } else {
                ans += (i - seg.query(k, i - 1));
                seg.update(i, k - seg.query(k, i - 1));
            }
            last[A[i]] = i;
        }
        pw.println(ans);

        pw.close();
    }
}