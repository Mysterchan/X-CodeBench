#include <bits/stdc++.h>
using namespace std;
const int M = 500000;
const int STSIZE = 4 * M + 20;
struct Node {
    int mn, mx, lz;
} st[STSIZE];

inline void push(int idx) {
    int v = st[idx].lz;
    if (v != 0) {
        int l = idx << 1, r = l | 1;
        st[l].lz += v;
        st[l].mn += v;
        st[l].mx += v;
        st[r].lz += v;
        st[r].mn += v;
        st[r].mx += v;
        st[idx].lz = 0;
    }
}

void build(int idx, int l, int r) {
    st[idx].lz = 0;
    if (l == r) {
        st[idx].mn = st[idx].mx = l;
    } else {
        int mid = (l + r) >> 1;
        build(idx << 1, l, mid);
        build(idx << 1 | 1, mid + 1, r);
        st[idx].mn = l;
        st[idx].mx = r;
    }
}

void update(int idx, int l, int r, int ql, int qr, int v) {
    if (qr < l || r < ql) return;
    if (ql <= l && r <= qr) {
        st[idx].lz += v;
        st[idx].mn += v;
        st[idx].mx += v;
        return;
    }
    push(idx);
    int mid = (l + r) >> 1;
    if (ql <= mid) update(idx << 1, l, mid, ql, qr, v);
    if (qr > mid) update(idx << 1 | 1, mid + 1, r, ql, qr, v);
    st[idx].mn = min(st[idx << 1].mn, st[idx << 1 | 1].mn);
    st[idx].mx = max(st[idx << 1].mx, st[idx << 1 | 1].mx);
}

int find_first(int idx, int l, int r, int target) {
    if (st[idx].mx < target) return M + 1;
    if (l == r) return l;
    push(idx);
    int mid = (l + r) >> 1;
    if (st[idx << 1].mx >= target) return find_first(idx << 1, l, mid, target);
    else return find_first(idx << 1 | 1, mid + 1, r, target);
}

int find_last(int idx, int l, int r, int target) {
    if (st[idx].mn > target) return 0;
    if (l == r) return l;
    push(idx);
    int mid = (l + r) >> 1;
    if (st[idx << 1 | 1].mn <= target) return find_last(idx << 1 | 1, mid + 1, r, target);
    else return find_last(idx << 1, l, mid, target);
}

int query(int idx, int l, int r, int pos) {
    if (l == r) return st[idx].mn;
    push(idx);
    int mid = (l + r) >> 1;
    if (pos <= mid) return query(idx << 1, l, mid, pos);
    else return query(idx << 1 | 1, mid + 1, r, pos);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    build(1, 1, M);
    for (int i = 0; i < N; i++) {
        int L, R;
        cin >> L >> R;
        int lp = find_first(1, 1, M, L);
        if (lp > M) continue;
        int rp = find_last(1, 1, M, R);
        if (rp < lp) continue;
        update(1, 1, M, lp, rp, 1);
    }
    int Q;
    cin >> Q;
    while (Q--) {
        int x;
        cin >> x;
        int ans = query(1, 1, M, x);
        cout << ans << '\n';
    }
    return 0;
}