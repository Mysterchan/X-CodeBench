import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main {

    static class Node {
        long min, max, lazy;
        Node() {
            this.min = Long.MAX_VALUE;
            this.max = Long.MIN_VALUE;
            this.lazy = 0;
        }
    }

    static int M = 500000;
    static Node[] tree = new Node[4 * M];

    static void apply(int v, long val) {
        tree[v].min += val;
        tree[v].max += val;
        tree[v].lazy += val;
    }

    static void push(int v) {
        if (tree[v].lazy != 0) {
            apply(2 * v, tree[v].lazy);
            apply(2 * v + 1, tree[v].lazy);
            tree[v].lazy = 0;
        }
    }

    static void pull(int v) {
        tree[v].min = Math.min(tree[2 * v].min, tree[2 * v + 1].min);
        tree[v].max = Math.max(tree[2 * v].max, tree[2 * v + 1].max);
    }

    static void build(int v, int tl, int tr) {
        tree[v] = new Node();
        if (tl == tr) {
            tree[v].min = tl;
            tree[v].max = tl;
        } else {
            int tm = (tl + tr) / 2;
            build(2 * v, tl, tm);
            build(2 * v + 1, tm + 1, tr);
            pull(v);
        }
    }

    static void range_add(int v, int tl, int tr, int ql, int qr, int val) {
        if (ql > qr) return;
        if (tl == ql && tr == qr) {
            apply(v, val);
            return;
        }
        push(v);
        int tm = (tl + tr) / 2;
        range_add(2 * v, tl, tm, ql, Math.min(qr, tm), val);
        range_add(2 * v + 1, tm + 1, tr, Math.max(ql, tm + 1), qr, val);
        pull(v);
    }

    static int find_first_ge(int v, int tl, int tr, int L) {
        if (tree[v].max < L) return -1;
        if (tl == tr) {
            return (tree[v].min >= L) ? tl : -1;
        }
        push(v);
        int tm = (tl + tr) / 2;
        int res_left = find_first_ge(2 * v, tl, tm, L);
        if (res_left != -1) {
            return res_left;
        }
        return find_first_ge(2 * v + 1, tm + 1, tr, L);
    }

    static int find_last_le(int v, int tl, int tr, int R) {
        if (tree[v].min > R) return -1;
        if (tl == tr) {
            return (tree[v].max <= R) ? tl : -1;
        }
        push(v);
        int tm = (tl + tr) / 2;
        int res_right = find_last_le(2 * v + 1, tm + 1, tr, R);
        if (res_right != -1) {
            return res_right;
        }
        return find_last_le(2 * v, tl, tm, R);
    }

    static long point_query(int v, int tl, int tr, int pos) {
        if (tl == tr) {
            return tree[v].min;
        }
        push(v);
        int tm = (tl + tr) / 2;
        if (pos <= tm) {
            return point_query(2 * v, tl, tm, pos);
        } else {
            return point_query(2 * v + 1, tm + 1, tr, pos);
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());

        build(1, 1, M);

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int L = Integer.parseInt(st.nextToken());
            int R = Integer.parseInt(st.nextToken());

            int x_min = find_first_ge(1, 1, M, L);
            int x_max = find_last_le(1, 1, M, R);

            if (x_min != -1 && x_max != -1 && x_min <= x_max) {
                range_add(1, 1, M, x_min, x_max, 1);
            }
        }

        int Q = Integer.parseInt(br.readLine());
        for (int i = 0; i < Q; i++) {
            int X = Integer.parseInt(br.readLine());
            out.println(point_query(1, 1, M, X));
        }
        out.flush();
    }
}