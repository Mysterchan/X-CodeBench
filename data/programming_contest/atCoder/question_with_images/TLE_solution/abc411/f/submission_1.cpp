#include <bits/stdc++.h>
#define pii pair<ll, ll>
typedef long long ll;
using namespace std;

const int MAX = 300007;
set<int> G[MAX];
pii E[MAX];

struct UF {
    ll R[MAX], Z[MAX];
    UF() {
        iota(R, R + MAX, 0);
        fill(Z, Z + MAX, 1);
    }

    int Find(int n) {
        if (n == R[n]) return n;
        return R[n] = Find(R[n]);
    }

    void Union(int a, int b) {
        a = Find(a), b = Find(b);
        if (a == b) return;
        R[a] = b;
        Z[b] += Z[a];
    }
} UF;

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int N, M, Q;
    cin >> N >> M;

    for (int i = 1; i <= M; ++i) {
        int a, b;
        cin >> a >> b;
        E[i] = {a, b};
        G[a].insert(b);
        G[b].insert(a);
    }

    int ans = M;
    cin >> Q;

    while (Q--) {
        int en;
        cin >> en;
        auto [a, b] = E[en];

        a = UF.Find(a), b = UF.Find(b);

        if (a != b) {
            if (G[a].size() < G[b].size()) swap(a, b);
            UF.Union(a,b);
            for(int n:G[a]){
                if(n==b)continue;
                n=UF.Find(n);
                G[b].insert(n);
                int t=G[n].size();
                G[n].erase(a);
                G[n].insert(b);
                ans+=(int)G[n].size()-t;
            }
        G[b].erase(a);
        ans--;
    }

        cout << ans << '\n';
    }
    return 0;
}
