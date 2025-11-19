#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    int n;
    vector<int> f;
    Fenwick(int _n=0): n(_n), f(n+1, 0) {}
    // initialize tree for all ones in O(n)
    void init_ones() {
        for (int i = 1; i <= n; i++) {
            f[i] = i & -i;
        }
    }
    // add v at position i (1-based)
    void update(int i, int v) {
        for (; i <= n; i += i & -i) {
            f[i] += v;
        }
    }
    // sum of [1..i]
    int query(int i) const {
        int s = 0;
        for (; i > 0; i -= i & -i) s += f[i];
        return s;
    }
    // find smallest idx such that sum[1..idx] >= k, assumes all values non-negative and k>=1
    int find_kth(int k) const {
        int idx = 0;
        int bitMask = 1 << (31 - __builtin_clz(n));
        for (int step = bitMask; step > 0; step >>= 1) {
            int nxt = idx + step;
            if (nxt <= n && f[nxt] < k) {
                k -= f[nxt];
                idx = nxt;
            }
        }
        return idx + 1;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<int> P(N+1);
    for(int i = 1; i <= N; i++){
        cin >> P[i];
    }

    Fenwick fw(N);
    fw.init_ones();

    vector<int> ans(N+1);
    // process from i = N down to 1
    for(int i = N; i >= 1; i--){
        int k = P[i];
        // find the k-th free slot
        int pos = fw.find_kth(k);
        ans[pos] = i;
        fw.update(pos, -1);
    }

    // output
    for(int i = 1; i <= N; i++){
        if(i > 1) cout << ' ';
        cout << ans[i];
    }
    cout << '\n';
    return 0;
}