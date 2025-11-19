#include <bits/stdc++.h>
using namespace std;
const int c=500005;
int n, m, k, deg[c], ps[c], pn[c];
int minlen;
int specel, spec2;
vector<int> sz[c];
void dfs(int a, int el, int b) {
    if (deg[a]>2) {
        minlen=min(minlen, b);
        return;
    }
    for (auto x:sz[a]) {
        if (x!=el) {
            dfs(x, a, b+1);
        }
    }
}
void solve() {
    cin >> n >> m >> k;
    for (int i=1; i<=m; i++) {
        int a, b;
        cin >> a >> b;
        sz[a].push_back(b), sz[b].push_back(a);
    }
    minlen=2*k;
    for (int i=1; i<=n; i++) {
        deg[i]=sz[i].size();
    }
    for (int i=1; i<=n; i++) {
        if (deg[i]%2) {
            dfs(i, 0, 0);
            
        }
    }

    for (int i=1; i<=n; i++) {
        for (auto x:sz[i]) {
            if (x>i) {
                if ((deg[i]+deg[x])%2) {
                    specel++;
                    pn[i]++, pn[x]++;
                } else {
                    ps[i]++, ps[x]++;
                }
            }
        }
    }
    for (int i=1; i<=n; i++) {
        int a=min(3, ps[i]), b=min(3, pn[i]);
        spec2+=a*b;
    }

    if (k==1) {
        cout << (specel<=2 ? "YES" : "NO") << "\n";
    } else if (k==2) {
        cout << (spec2<=2 ? "YES" : "NO") << "\n";
    } else {
        cout << ((minlen>=k || spec2==0) ? "YES" : "NO") << "\n";
    }

    
    for (int i=0; i<=n; i++) {
        deg[i]=0;
        sz[i].clear();
    }

    specel=0, spec2=0;
    for (int i=0; i<=n; i++) {
        ps[i]=0, pn[i]=0;
    }
}
int main() {
	ios_base::sync_with_stdio(false);
    int w;
    cin >> w;
    while (w--) {
        solve();
    }
}