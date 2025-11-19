import java.util.*;

public class Main {
    static final int N = 400000;
    static int n, t, tot;
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
        List<int[]>[] v = new ArrayList[N * 4 + 50];

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
            int mid = (l + r) / 2;
            if (x <= mid) add(id * 2, l, mid, x, y, pair);
            if (y > mid) add(id * 2 + 1, mid + 1, r, x, y, pair);
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
                int mid = (l + r) / 2;
                dfs(id * 2, l, mid, ti);
                dfs(id * 2 + 1, mid + 1, r, ti);
            }
            Collections.reverse(st);
            for (int[] i : st) {
                sz[fa[i[0]]] -= i[2];
                fa[i[0]] = i[1];
                sz[i[0]] = i[2];
                tot++;
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        t = sc.nextInt();
        tot = n;

        for (int i = 0; i < 2; i++) op[i] = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            fa[i] = i;
            sz[i] = 1;
        }

        for (int i = 1; i <= t; i++) {
            String type = sc.next();
            int j = sc.nextInt(), k = sc.nextInt();
            if (j > k) {
                int temp = j;
                j = k;
                k = temp;
            }
            op[type.equals("B") ? 1 : 0].add(new Triple(i, j, k));
        }

        SegmentTree sb = new SegmentTree();

        for (int T = 0; T <= 1; T++) {
            Map<String, Integer> mp = new HashMap<>();
            for (Triple tri : op[T]) {
                String key = tri.x + "," + tri.y;
                if (mp.containsKey(key)) {
                    sb.add(1, 1, t, mp.get(key), tri.time - 1, new int[]{tri.x, tri.y});
                    mp.remove(key);
                } else {
                    mp.put(key, tri.time);
                }
            }
            for (Map.Entry<String, Integer> entry : mp.entrySet()) {
                String[] parts = entry.getKey().split(",");
                int x = Integer.parseInt(parts[0]);
                int y = Integer.parseInt(parts[1]);
                sb.add(1, 1, t, entry.getValue(), t, new int[]{x, y});
            }
            sb.dfs(1, 1, t, T);
        }

        for (int i = 1; i <= t; i++) {
            System.out.println(f[i][0] - f[i][1]);
        }
    }
}
