#include <bits/stdc++.h>
using namespace std;

const int MAXN = 3000000;

struct SegmentTree {
    int val[MAXN * 4];

    void build(int p, int l, int r) {
        if (l == r) {
            val[p] = 1;
        } else {
            int mid = (l + r) >> 1;
            build(p << 1, l, mid);
            build(p << 1 | 1, mid + 1, r);
            val[p] = val[p << 1] + val[p << 1 | 1];
        }
    }

    void modify(int p, int l, int r, int x) {
        if (l == r) {
            if (val[p]) {
                val[p] = 0;
            }
            return;
        }
        int mid = (l + r) >> 1;
        if (x <= mid) modify(p << 1, l, mid, x);
        else modify(p << 1 | 1, mid + 1, r, x);
        val[p] = val[p << 1] + val[p << 1 | 1];
    }

    int query(int p, int l, int r, int x) {
        if (l == r) return l;
        int mid = (l + r) >> 1;
        if (val[p << 1] >= x) return query(p << 1, l, mid, x);
        else return query(p << 1 | 1, mid + 1, r, x - val[p << 1]);
    }
} seg;

int q;
bool removed[MAXN + 1];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> q;
    seg.build(1, 1, MAXN);

    while (q--) {
        int a, b;
        cin >> a >> b;

        if (a <= MAXN && !removed[a]) {
            removed[a] = true;
            // Remove multiples of a efficiently
            // Instead of calling modify for each multiple, we can batch process:
            // But since we must remove multiples individually, we do it in steps of a.
            // To optimize, we can skip multiples already removed.
            for (int x = a; x <= MAXN; x += a) {
                if (removed[x]) continue; // Already removed as a multiple of smaller factor
                seg.modify(1, 1, MAXN, x);
                removed[x] = true;
            }
        }
        cout << seg.query(1, 1, MAXN, b) << "\n";
    }

    return 0;
}