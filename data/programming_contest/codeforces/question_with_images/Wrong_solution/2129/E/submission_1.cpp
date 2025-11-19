#include <bits/stdc++.h>
using namespace std;

const int MAX_VAL = 1 << 18;

struct SegTree {
    int n;
    vector<int> tree;
    SegTree(int size) {
        n = size;
        tree.resize(4 * n, 0);
    }
    void update(int idx, int l, int r, int pos, int delta) {
        if (l == r) {
            tree[idx] += delta;
            return;
        }
        int mid = (l + r) / 2;
        if (pos <= mid) {
            update(2 * idx, l, mid, pos, delta);
        } else {
            update(2 * idx + 1, mid + 1, r, pos, delta);
        }
        tree[idx] = tree[2 * idx] + tree[2 * idx + 1];
    }
    int kth(int idx, int l, int r, int k) {
        if (l == r) {
            return l;
        }
        int mid = (l + r) / 2;
        if (tree[2 * idx] >= k) {
            return kth(2 * idx, l, mid, k);
        } else {
            return kth(2 * idx + 1, mid + 1, r, k - tree[2 * idx]);
        }
    }
    void update(int pos, int delta) {
        update(1, 0, n - 1, pos, delta);
    }
    int kth(int k) {
        return kth(1, 0, n - 1, k);
    }
};

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        int n, m;
        scanf("%d %d", &n, &m);
        vector<vector<int>> adj(n + 1);
        for (int i = 0; i < m; i++) {
            int u, v;
            scanf("%d %d", &u, &v);
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        int q;
        scanf("%d", &q);
        vector<tuple<int, int, int, int>> queries;
        for (int i = 0; i < q; i++) {
            int l, r, k;
            scanf("%d %d %d", &l, &r, &k);
            queries.emplace_back(l, r, k, i);
        }

        int block_size = sqrt(n);
        sort(queries.begin(), queries.end(), [block_size](const auto &a, const auto &b) {
            auto [l1, r1, k1, i1] = a;
            auto [l2, r2, k2, i2] = b;
            int block1 = l1 / block_size;
            int block2 = l2 / block_size;
            if (block1 != block2) 
                return block1 < block2;
            else 
                return (block1 & 1) ? (r1 > r2) : (r1 < r2);
        });

        vector<int> F(n + 1, 0);
        vector<bool> in(n + 1, false);
        SegTree seg_tree(MAX_VAL);

        int cur_l = 1, cur_r = 0;
        vector<int> answers(q);

        auto add = [&](int u) {
            in[u] = true;
            for (int v : adj[u]) {
                if (in[v]) {
                    seg_tree.update(F[v], -1);
                    F[v] ^= u;
                    seg_tree.update(F[v], 1);
                    F[u] ^= v;
                }
            }
            seg_tree.update(F[u], 1);
        };

        auto remove = [&](int u) {
            seg_tree.update(F[u], -1);
            for (int v : adj[u]) {
                if (in[v]) {
                    seg_tree.update(F[v], -1);
                    F[v] ^= u;
                    seg_tree.update(F[v], 1);
                }
            }
            in[u] = false;
        };

        for (auto [l, r, k, idx] : queries) {
            while (cur_l > l) {
                add(--cur_l);
            }
            while (cur_r < r) {
                add(++cur_r);
            }
            while (cur_l < l) {
                remove(cur_l++);
            }
            while (cur_r > r) {
                remove(cur_r--);
            }
            answers[idx] = seg_tree.kth(k);
        }

        for (int i = 0; i < q; i++) {
            printf("%d\n", answers[i]);
        }
    }
    return 0;
}