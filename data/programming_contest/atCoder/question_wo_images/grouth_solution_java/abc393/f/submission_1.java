import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.TreeSet;

public class Main {

    static class Query {
        int rankX;
        int queryId;
        Query(int rankX, int queryId) {
            this.rankX = rankX;
            this.queryId = queryId;
        }
    }

    static class RawQuery {
        int R;
        long X;
        int queryId;
        RawQuery(int R, long X, int queryId) {
            this.R = R;
            this.X = X;
            this.queryId = queryId;
        }
    }

    static class SegTree {
        int[] tree;
        int n;

        SegTree(int size) {
            n = size;

            tree = new int[4 * n];
        }

        void update(int v, int tl, int tr, int pos, int val) {
            if (tl == tr) {

                tree[v] = Math.max(tree[v], val);
            } else {
                int tm = (tl + tr) / 2;
                if (pos <= tm) {
                    update(2 * v, tl, tm, pos, val);
                } else {
                    update(2 * v + 1, tm + 1, tr, pos, val);
                }
                tree[v] = Math.max(tree[2 * v], tree[2 * v + 1]);
            }
        }

        public void pointUpdate(int pos, int val) {
            update(1, 1, n, pos, val);
        }

        int query(int v, int tl, int tr, int ql, int qr) {
            if (ql > qr) return 0;
            if (tl == ql && tr == qr) return tree[v];
            int tm = (tl + tr) / 2;
            return Math.max(
                query(2 * v, tl, tm, ql, Math.min(qr, tm)),
                query(2 * v + 1, tm + 1, tr, Math.max(ql, tm + 1), qr)
            );
        }

        public int rangeMaxQuery(int L, int R) {
            if (L > R) return 0;
            return query(1, 1, n, L, R);
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int Q = Integer.parseInt(st.nextToken());

        long[] A = new long[N];
        st = new StringTokenizer(br.readLine());

        Set<Long> allValues = new TreeSet<>();
        for (int i = 0; i < N; i++) {
            A[i] = Long.parseLong(st.nextToken());
            allValues.add(A[i]);
        }

        List<RawQuery> rawQueries = new ArrayList<>(Q);
        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine());
            int R = Integer.parseInt(st.nextToken());
            long X = Long.parseLong(st.nextToken());
            rawQueries.add(new RawQuery(R, X, i));
            allValues.add(X);
        }

        Map<Long, Integer> ranks = new HashMap<>();
        int V = 0;
        for (long val : allValues) {
            V++;
            ranks.put(val, V);
        }

        List<Query>[] queriesByR = new ArrayList[N + 1];
        for (int i = 0; i <= N; i++) {
            queriesByR[i] = new ArrayList<>();
        }

        for (RawQuery rq : rawQueries) {
            int rankX = ranks.get(rq.X);
            queriesByR[rq.R].add(new Query(rankX, rq.queryId));
        }

        SegTree ds = new SegTree(V);
        int[] answers = new int[Q];

        for (int R = 1; R <= N; R++) {

            long v = A[R - 1];
            int rank_v = ranks.get(v);

            int L = ds.rangeMaxQuery(1, rank_v - 1);
            int newL = L + 1;

            ds.pointUpdate(rank_v, newL);

            for (Query q : queriesByR[R]) {
                int rank_X = q.rankX;

                int ans = ds.rangeMaxQuery(1, rank_X);
                answers[q.queryId] = ans;
            }
        }

        for (int i = 0; i < Q; i++) {
            out.println(answers[i]);
        }
        out.flush();
    }
}