#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>;

const int N = 1 << 18, K = 1 << 10;

struct DS {
    int big[N / K], small[N];
    void ins(int x) {
        small[x]++;
        big[x >> 10]++;
    }
    void del(int x) {
        small[x]--;
        big[x >> 10]--;
    }
    int kth(int k) {
        k--;
        int cur = 0;
        while (big[cur] <= k) k -= big[cur++];
        cur <<= 10;
        while (small[cur] <= k) k -= small[cur++];
        return cur;
    }
} ds;

void ahcorz() {
    int n, m;
    cin >> n >> m;
    vvi adj(n);
    for (int i = 0, u, v; i < m; ++i) {
        cin >> u >> v;
        u--, v--;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vi block(n);
    int cur = 0;
    for (int i = 0; i < n; ++i) {
        if (cur >= n) break;
        int tot = 0;
        while (cur < n && tot < K) {
            tot += adj[cur].size() + 1;
            block[cur++] = i;
        }
    }

    int q;
    cin >> q;
    vector<array<int, 4>> qq(q);
    vi res(q);
    for (int i = 0; i < q; ++i) {
        int l, r, k;
        cin >> l >> r >> k;
        l--, r--;
        qq[i] = {l, r, k, i};
    }

    sort(qq.begin(), qq.end(), [&](array<int, 4> arr1, array<int, 4> arr2) {
        if (block[arr1[0]] != block[arr2[0]]) return block[arr1[0]] < block[arr2[0]];
        if (block[arr1[0]] & 1) return arr1[1] > arr2[1];
        else return arr1[1] < arr2[1];
    });

    vi val(n);
    int l = 0, r = 0;
    ds.ins(0);

    auto ins = [&](int i) {
        for (auto j : adj[i]) {
            if (j >= l && j <= r) {
                ds.del(val[j]);
                val[j] ^= i + 1;
                val[i] ^= j + 1;
                ds.ins(val[j]);
            }
        }
        ds.ins(val[i]);
    };

    auto del = [&](int i) {
        ds.del(val[i]);
        for (auto j : adj[i]) {
            if (j >= l && j <= r) {
                ds.del(val[j]);
                val[j] ^= i + 1;
                val[i] ^= j + 1;
                ds.ins(val[j]);
            }
        }
    };

    auto gogo = [&](int l2, int r2) {
        while (l > l2) {
            ins(l - 1);
            l--;
        }
        while (r < r2) {
            ins(r + 1);
            r++;
        }
        while (l < l2) {
            l++;
            del(l - 1);
        }
        while (r > r2) {
            r--;
            del(r + 1);
        }
    };

    for (auto [l2, r2, k, i] : qq) {
        gogo(l2, r2);
        res[i] = ds.kth(k);
    }

    for (int i = l; i <= r; ++i) ds.del(val[i]);
    for (int i = 0; i < q; ++i) cout << res[i] << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) ahcorz();
    return 0;
}