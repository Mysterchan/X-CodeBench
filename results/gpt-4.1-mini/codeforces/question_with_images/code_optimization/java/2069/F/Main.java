import java.io.*;
import java.util.*;

public class Main {
    static final int N = 400000;
    static int n, q;
    static int[][] f = new int[N + 50][2];
    static int[] fa = new int[N + 50], sz = new int[N + 50];
    static List<Triple>[] op = new ArrayList[2];

    static class Triple {
        int time, x, y;
        Triple(int time, int x, int y) {
            this.time = time;
            this.x = x;
            this.y = y;
        }
    }

    static int find(int x) {
        while (x != fa[x]) x = fa[x];
        return x;
    }

    static class SegmentTree {
        List<int[]>[] v = new List[N * 4 + 50];

        SegmentTree() {
            for (int i = 0; i < v.length; i++) {
                v[i] = new ArrayList<>();
            }
        }

        void add(int id, int l, int r, int x, int y, int[] pair) {
            if (x <= l && r <= y) {
                v[id].add(pair);
                return;
            }
            int mid = (l + r) >>> 1;
            if (x <= mid) add(id << 1, l, mid, x, y, pair);
            if (y > mid) add(id << 1 | 1, mid + 1, r, x, y, pair);
        }

        void dfs(int id, int l, int r, int ti) {
            List<int[]> st = new ArrayList<>();
            for (int[] p : v[id]) {
                int x = find(p[0]), y = find(p[1]);
                if (x == y) continue;
                if (sz[x] < sz[y]) {
                    int temp = x;
                    x = y;
                    y = temp;
                }
                st.add(new int[]{y, fa[y], sz[y]});
                fa[y] = x;
                sz[x] += sz[y];
                tot--;
            }
            if (l == r) {
                f[l][ti] = tot;
            } else {
                int mid = (l + r) >>> 1;
                dfs(id << 1, l, mid, ti);
                dfs(id << 1 | 1, mid + 1, r, ti);
            }
            for (int i = st.size() - 1; i >= 0; i--) {
                int[] x = st.get(i);
                sz[fa[x[0]]] -= x[2];
                fa[x[0]] = x[1];
                sz[x[0]] = x[2];
                tot++;
            }
        }
    }

    static int tot;

    public static void main(String[] args) throws IOException {
        // Use BufferedReader and BufferedWriter for faster IO
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        q = Integer.parseInt(st.nextToken());
        tot = n;

        for (int i = 0; i < 2; i++) op[i] = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            fa[i] = i;
            sz[i] = 1;
        }

        for (int i = 1; i <= q; i++) {
            st = new StringTokenizer(br.readLine());
            String type = st.nextToken();
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            if (x > y) {
                int tmp = x;
                x = y;
                y = tmp;
            }
            op[type.equals("B") ? 1 : 0].add(new Triple(i, x, y));
        }

        SegmentTree sb = new SegmentTree();

        for (int T = 0; T <= 1; T++) {
            Map<Long, Integer> mp = new HashMap<>();
            for (Triple tri : op[T]) {
                long key = ((long)tri.x << 20) | tri.y; // combine x,y into a long key (20 bits per coordinate is enough for 4e5)
                if (mp.containsKey(key)) {
                    sb.add(1, 1, q, mp.get(key), tri.time - 1, new int[]{tri.x, tri.y});
                    mp.remove(key);
                } else {
                    mp.put(key, tri.time);
                }
            }
            for (Map.Entry<Long, Integer> entry : mp.entrySet()) {
                long key = entry.getKey();
                int x = (int)(key >> 20);
                int y = (int)(key & ((1 << 20) - 1));
                sb.add(1, 1, q, entry.getValue(), q, new int[]{x, y});
            }
            // Reset DSU for next graph
            for (int i = 1; i <= n; i++) {
                fa[i] = i;
                sz[i] = 1;
            }
            tot = n;
            sb.dfs(1, 1, q, T);
        }

        for (int i = 1; i <= q; i++) {
            bw.write((f[i][0] - f[i][1]) + "\n");
        }
        bw.flush();
    }
}