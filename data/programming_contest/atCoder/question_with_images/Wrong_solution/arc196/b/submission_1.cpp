#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define int ll
#define ft first
#define sc second
#define pb push_back
#define all(x) x.begin(), x.end()
#define pi pair<int, int>
#define vi vector<int>
#define tii tuple<int, int, int>
#define tiii tuple<int, int, int, int>
#define tiiii tuple<int, int, int, int, int>
#define vpi vector<pi>
#define vtii vector<tii>
#define vtiii vector<tiii>

const int MOD = 998244353, INF = int(1e18), L = (1 << 22);

vpi graf[L];

void add_edge(int a, int b, int v){
    graf[a].pb({b, v}); graf[b].pb({a, v});
}

void add_square(bool t, int n, int h, int w){
    int N = h * w, M = 4 * N;
    if(t){     
        add_edge(n, n + 2 * N, 1);
        add_edge(n + N, n + 3 * N, 1);
    }else{
        for(int i = 0; i < 4; i++) add_edge(n + i * N, (n + (i + 1) * N - 1) % M + 1, 1);
    }
    add_edge(n + 3 * N, (n) % (h * w) + 1 + N, 0);
    add_edge(n + 2 * N, (n + w - 1) % (h * w) + 1, 0);
}

int c[L];

bool dfs(int u){
    for(auto [i, j] : graf[u]){
        if(c[i] >= 0 && c[i] != (c[u] ^ j)){
            return 0;
        }else if(c[i] >= 0) continue;
        c[i] = c[u] ^ j;
        if(!dfs(i)) return 0;
    }
    return 1;
}

void solve(){
    int H, W;
    cin >> H >> W;
    int N = H * W, M = 4 * N;
    vector<vi> num;
    vector<vi> m;

    num.resize(H, vi(W));
    m.resize(H, vi(W));
    for(int i = 0; i < H; i++){
        for(int j = 0; j < W; j++){
            char a;
            cin >> a;
            m[i][j] = (a == 'A');
            num[i][j] = i * W + j + 1;
        }
    }

    for(int i= 0; i < H; i++){
        for(int j = 0; j < W; j++){
            add_square(m[i][j], num[i][j], H, W);
        }
    }

    int ans = 1;
    for(int i = 0; i <= M; i++) c[i] = -1;
    for(int i = 1; i <= M; i++){
        if(c[i] >= 0) continue;
        c[i] = 0;
        if(!dfs(i)){
            for(int j = 0; j <= M; j++) graf[j].clear();
            cout << "0\n";
            return;
        }
        ans = (ans * 2LL) % MOD;
    }
    cout << ans << "\n";
    for(int i = 0; i <= M; i++) graf[i].clear();
    return;

}
signed main(){
    ios_base::sync_with_stdio(0);
    cin.tie(NULL); cout.tie(NULL);
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}