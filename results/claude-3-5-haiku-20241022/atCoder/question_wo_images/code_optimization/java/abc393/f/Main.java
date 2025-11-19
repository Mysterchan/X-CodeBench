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
                tree[node] = Math.max(tree[node], val);
                return;
            }
            int mid = (l + r) / 2;
            update(idx, val, 2 * node + 1, l, mid);
            update(idx, val, 2 * node + 2, mid + 1, r);
            tree[node] = Math.max(tree[2 * node + 1], tree[2 * node + 2]);
        }

        int query(int l, int r) {
            return query(l, r, 0, 0, n - 1);
        }

        int query(int l, int r, int node, int tl, int tr) {
            if (l > r) return 0;
            if (l == tl && r == tr) return tree[node];
            int mid = (tl + tr) / 2;
            return Math.max(query(l, Math.min(r, mid), 2 * node + 1, tl, mid),
                    query(Math.max(l, mid + 1), r, 2 * node + 2, mid + 1, tr));
        }
    }

    static class Query {
        int idx, x;

        public Query(int idx, int x) {
            this.idx = idx;
            this.x = x;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        List<Query>[] queriesAtPos = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            queriesAtPos[i] = new ArrayList<>();
        }

        List<Integer> xs = new ArrayList<>();
        for (int x : a) xs.add(x);
        
        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken()) - 1;
            int x = Integer.parseInt(st.nextToken());
            xs.add(x);
            queriesAtPos[r].add(new Query(i, x));
        }

        Collections.sort(xs);
        xs = new ArrayList<>(new LinkedHashSet<>(xs));

        for (int i = 0; i < n; i++) {
            a[i] = Collections.binarySearch(xs, a[i]);
        }
        
        for (int i = 0; i < n; i++) {
            for (Query query : queriesAtPos[i]) {
                query.x = Collections.binarySearch(xs, query.x);
            }
        }

        SegmentTree segmentTree = new SegmentTree(xs.size());
        int[] answers = new int[q];

        for (int i = 0; i < n; i++) {
            int curr = segmentTree.query(0, a[i] - 1) + 1;
            segmentTree.update(a[i], curr);
            
            for (Query query : queriesAtPos[i]) {
                answers[query.idx] = segmentTree.query(0, query.x);
            }
        }

        for (int answer : answers) {
            pw.println(answer);
        }

        pw.close();
    }
}