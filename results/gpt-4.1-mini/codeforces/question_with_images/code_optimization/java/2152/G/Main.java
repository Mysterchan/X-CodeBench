import java.io.*;
import java.util.*;

public class Main {
    static int n, q;
    static ArrayList<Integer>[] tree;
    static int[] a;
    static int[] in, out;
    static int time;
    static SegmentTree segTree;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder outSb = new StringBuilder();
        int t = Integer.parseInt(br.readLine());
        // sum of n and q over all test cases <= 250000, so we can reuse arrays with max size

        while (t-- > 0) {
            n = Integer.parseInt(br.readLine());
            a = new int[n + 1];
            String[] parts = br.readLine().split(" ");
            for (int i = 1; i <= n; i++) {
                a[i] = Integer.parseInt(parts[i - 1]);
            }

            tree = new ArrayList[n + 1];
            for (int i = 1; i <= n; i++) tree[i] = new ArrayList<>();

            for (int i = 0; i < n - 1; i++) {
                parts = br.readLine().split(" ");
                int u = Integer.parseInt(parts[0]);
                int v = Integer.parseInt(parts[1]);
                tree[u].add(v);
                tree[v].add(u);
            }

            in = new int[n + 1];
            out = new int[n + 1];
            time = 0;
            dfs(1, 0);

            // Build segment tree on Euler order
            int[] base = new int[n + 1];
            for (int i = 1; i <= n; i++) {
                base[in[i]] = a[i];
            }
            segTree = new SegmentTree(n);
            segTree.build(base);

            q = Integer.parseInt(br.readLine());
            // Initial answer
            outSb.append(segTree.getMinPaths()).append('\n');

            for (int i = 0; i < q; i++) {
                int v = Integer.parseInt(br.readLine());
                segTree.update(in[v], out[v]);
                outSb.append(segTree.getMinPaths()).append('\n');
            }
        }
        System.out.print(outSb);
    }

    static void dfs(int u, int p) {
        in[u] = ++time;
        for (int w : tree[u]) {
            if (w != p) {
                dfs(w, u);
            }
        }
        out[u] = time;
    }

    static class SegmentTree {
        int size;
        Node[] tree;

        static class Node {
            int sum; // number of monsters in segment
            int minPaths; // minimal number of paths needed in segment
            boolean flip; // lazy flip flag

            Node() {
                sum = 0;
                minPaths = 0;
                flip = false;
            }
        }

        SegmentTree(int n) {
            size = 1;
            while (size < n) size <<= 1;
            tree = new Node[size << 1];
            for (int i = 0; i < tree.length; i++) tree[i] = new Node();
        }

        void build(int[] base) {
            // base is 1-indexed, build leaves at [size..size+n-1]
            for (int i = 1; i < base.length; i++) {
                tree[size + i - 1].sum = base[i];
                tree[size + i - 1].minPaths = base[i];
            }
            for (int i = size - 1; i > 0; i--) {
                pull(i);
            }
        }

        void pull(int i) {
            Node left = tree[i << 1];
            Node right = tree[i << 1 | 1];
            Node cur = tree[i];
            cur.sum = left.sum + right.sum;
            // minPaths = max(minPaths_left, minPaths_right) + (if both > 0 then -1 else 0)
            // Because minimal paths = sum of children's minPaths - number of edges connecting them if both have monsters
            // But since this is a tree rooted at 1, and we want minimal paths covering all monsters starting at root,
            // the formula is:
            // minPaths = left.minPaths + right.minPaths - (left.minPaths > 0 && right.minPaths > 0 ? 1 : 0)
            // This is because if both children have monsters, their paths can be merged at this node.
            int leftPaths = left.minPaths;
            int rightPaths = right.minPaths;
            if (leftPaths > 0 && rightPaths > 0) {
                cur.minPaths = leftPaths + rightPaths - 1;
            } else {
                cur.minPaths = leftPaths + rightPaths;
            }
        }

        void applyFlip(int i) {
            Node cur = tree[i];
            cur.sum = (segmentLength(i) - cur.sum);
            // flip minPaths accordingly:
            // if sum == 0 => minPaths = 0
            // else minPaths = 1 (since after flip, monsters become non-monsters and vice versa)
            // But we must recalc minPaths properly:
            // Actually, flipping means monsters become non-monsters and vice versa.
            // For a leaf node, minPaths = sum (0 or 1)
            // For internal nodes, minPaths = sum of children's minPaths - (if both children have monsters then 1 else 0)
            // But after flip, minPaths = number of connected components of monsters in segment.
            // Since we don't store structure here, we can just flip minPaths as:
            // minPaths = (sum == 0) ? 0 : 1 (for leaves)
            // For internal nodes, we just mark flip and recalc on push.
            // So we just mark flip and recalc on push.
            cur.flip ^= true;
        }

        int segmentLength(int i) {
            // length of segment represented by node i
            // size of segment tree is size
            // node i covers segment [l,r]
            // We can store l,r or calculate on the fly
            // To avoid complexity, we store l,r in arrays
            // But to keep code simple and fast, we store l,r in arrays
            // Let's store l,r arrays
            return r[i] - l[i] + 1;
        }

        int[] l, r;

        void buildLR() {
            l = new int[tree.length];
            r = new int[tree.length];
            buildLR(1, 1, size);
        }

        void buildLR(int i, int left, int right) {
            l[i] = left;
            r[i] = right;
            if (left == right) return;
            int mid = (left + right) >> 1;
            buildLR(i << 1, left, mid);
            buildLR(i << 1 | 1, mid + 1, right);
        }

        void push(int i) {
            Node cur = tree[i];
            if (cur.flip) {
                applyFlip(i << 1);
                applyFlip(i << 1 | 1);
                cur.flip = false;
            }
        }

        void update(int L, int R) {
            if (l == null) buildLR();
            update(1, L, R);
        }

        void update(int i, int L, int R) {
            if (r[i] < L || l[i] > R) return;
            if (L <= l[i] && r[i] <= R) {
                applyFlip(i);
                return;
            }
            push(i);
            update(i << 1, L, R);
            update(i << 1 | 1, L, R);
            pull(i);
        }

        int getMinPaths() {
            return tree[1].minPaths;
        }
    }
}