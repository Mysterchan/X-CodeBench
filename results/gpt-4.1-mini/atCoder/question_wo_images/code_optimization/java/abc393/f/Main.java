import java.util.*;
import java.io.*;

public class Main {
    static class SegmentTree {
        int[] tree;
        int n;

        public SegmentTree(int n) {
            this.n = n;
            tree = new int[4 * n];
        }

        void update(int idx, int val) {
            update(idx, val, 0, 0, n - 1);
        }

        void update(int idx, int val, int node, int l, int r) {
            if (idx < l || idx > r) return;
            if (l == r) {
                if (val > tree[node]) tree[node] = val;
                return;
            }
            int mid = (l + r) >>> 1;
            update(idx, val, 2 * node + 1, l, mid);
            update(idx, val, 2 * node + 2, mid + 1, r);
            tree[node] = Math.max(tree[2 * node + 1], tree[2 * node + 2]);
        }

        int query(int l, int r) {
            if (l > r) return 0;
            return query(l, r, 0, 0, n - 1);
        }

        int query(int l, int r, int node, int tl, int tr) {
            if (l > r) return 0;
            if (l == tl && r == tr) return tree[node];
            int mid = (tl + tr) >>> 1;
            return Math.max(query(l, Math.min(r, mid), 2 * node + 1, tl, mid),
                    query(Math.max(l, mid + 1), r, 2 * node + 2, mid + 1, tr));
        }
    }

    static class Query {
        int r, x, idx;

        public Query(int r, int x, int idx) {
            this.r = r;
            this.x = x;
            this.idx = idx;
        }
    }

    public static void main(String[] args) throws IOException {
        // Fast IO
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        int[] a = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        Query[] queries = new Query[q];
        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken()) - 1;
            int x = Integer.parseInt(st.nextToken());
            queries[i] = new Query(r, x, i);
        }

        // Coordinate compression of values in a and queries.x
        // Collect all values
        int[] vals = new int[n + q];
        System.arraycopy(a, 0, vals, 0, n);
        for (int i = 0; i < q; i++) {
            vals[n + i] = queries[i].x;
        }
        Arrays.sort(vals);
        int m = 0;
        for (int i = 1; i < vals.length; i++) {
            if (vals[i] != vals[m]) vals[++m] = vals[i];
        }
        m++; // number of unique values

        // Map original values to compressed indices
        // Using binary search
        for (int i = 0; i < n; i++) {
            a[i] = Arrays.binarySearch(vals, 0, m, a[i]);
        }
        for (int i = 0; i < q; i++) {
            queries[i].x = Arrays.binarySearch(vals, 0, m, queries[i].x);
        }

        // Sort queries by r ascending
        Arrays.sort(queries, (o1, o2) -> Integer.compare(o1.r, o2.r));

        SegmentTree seg = new SegmentTree(m);
        int[] answers = new int[q];

        int currPos = 0;
        for (Query query : queries) {
            // Process array elements up to query.r
            while (currPos <= query.r) {
                int val = a[currPos];
                int best = seg.query(0, val - 1) + 1;
                seg.update(val, best);
                currPos++;
            }
            // Query the segment tree for max LIS length with values <= query.x
            answers[query.idx] = seg.query(0, query.x);
        }

        for (int ans : answers) {
            pw.println(ans);
        }
        pw.close();
    }
}