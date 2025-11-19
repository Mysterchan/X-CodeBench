import java.util.*;

public class Main {
    static int[] ans;

    static int ls(int x) {
        return x << 1;
    }

    static int rs(int x) {
        return x << 1 | 1;
    }

    static void push_up(int p) {
        ans[p] = ans[ls(p)] + ans[rs(p)];
    }

    static void update(int nl, int nr, int l, int r, int p, int k) {
        if (nl <= l && r <= nr) {
            ans[p] += k;
            return;
        }
        int mid = (l + r) >> 1;
        if (nl <= mid) update(nl, nr, l, mid, ls(p), k);
        if (nr > mid) update(nl, nr, mid + 1, r, rs(p), k);
        push_up(p);
    }

    static int query(int q_x, int q_y, int l, int r, int p) {
        int res = 0;
        if (q_x <= l && r <= q_y) return ans[p];
        int mid = (l + r) >> 1;
        if (q_x <= mid) res += query(q_x, q_y, l, mid, ls(p));
        if (q_y > mid) res += query(q_x, q_y, mid + 1, r, rs(p));
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        ans = new int[8 * n + 10];
        List<List<int[]>> list = new ArrayList<>();
        list.add(new ArrayList<>());
        for (int i = 1; i <= 2 * n; ++i)
            list.add(new ArrayList<>());
        for (int i = 1; i <= m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            list.get(a).add(new int[]{b});
            update(a, a, 1, 2 * n, 1, 1);
            update(b, b, 1, 2 * n, 1, -1);
        }
        int q = sc.nextInt();
        for (int i = 1; i <= q; ++i) {
            int c = sc.nextInt();
            int d = sc.nextInt();
            list.get(c).add(new int[]{d, i});
        }
        int[] out = new int[q + 10];
        for (int i = 1; i <= 2 * n; ++i) {
            if (i % 2 == 1) {
                for (int[] j : list.get(i))
                    out[j[1]] = query(i, j[0], 1, 2 * n, 1);
            } else {
                for (int[] j : list.get(i)) {
                    update(i, i, 1, 2 * n, 1, -2);
                    update(j[0], j[0], 1, 2 * n, 1, 2);
                }
            }
        }
        for (int i = 1; i <= q; ++i)
            System.out.println(out[i]);
    }
}