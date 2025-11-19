#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>

using namespace std;;
using namespace __gnu_pbds;

template<typename T>
using oset = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;


#define ll long long
#define ar array
#define ld double
#define int long long
#define all(v) v.begin(), v.end()
 #pragma GCC optimize("O3,Ofast,unroll-loops")

const int N = 5e5 + 20;
const int K = 500;
const int M = 20;
const int LOG = 20;
const int INF = 1e15;	
int MOD = 998244353;
const ld EPS = 1e-12;

template<typename T>
inline void chmin(T &x,T y){x = min(x, y);}
template<typename T>
inline void chmax(T &x,T y){x = max(x, y);}
inline void mm(int &x){x = (x % MOD + MOD) % MOD;};

int P(int a,int b){
    int res = 1;
    while(b){
        if(b % 2)mm(res *= a);
        b /= 2;
        mm(a *= a);
    }
    return res;
}

struct DSU{
    int n, m;
    vector<int> p;

    DSU(int a,int b){
        n = a;
        m = b;
        p.clear();
        p.resize(n * m);
        iota(all(p), 0);
    }

    int fnd(int x){
        if(p[x] == x)return x;
        return p[x] = fnd(p[x]);
    }

    bool upd(int x1, int y1,int x2,int y2){
        assert(0 <= x1 && x1 < n);
        assert(0 <= x2 && x2 < n);
        assert(0 <= y1 && y1 < m);
        assert(0 <= y2 && y2 < m);
        int a = x1 * m + y1;
        int b = x2 * m + y2;
        a = fnd(a);
        b = fnd(b);
        if(a == b)return 0;
        p[a] = b;
        return 1;
    }

    bool qry(int x1, int y1,int x2,int y2){
        assert(0 <= x1 && x1 < n);
        assert(0 <= x2 && x2 < n);
        assert(0 <= y1 && y1 < m);
        assert(0 <= y2 && y2 < m);

        int a = x1 * m + y1;
        int b = x2 * m + y2;
        a = fnd(a);
        b = fnd(b);
        return a == b;
    }
};

int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

void orz(){
    int n, m;
    cin>>n>>m;
    int A[n][m];
    for(int i = 0;i < n;i++){
        for(int j = 0;j < m;j++)cin>>A[i][j];
    }
    int q;
    cin>>q;
    int ans[q] = {0};
    ar<int,5> Q[q];
    int L[q], R[q];
    for(int i =0 ;i < q;i++){
        int x1, y1, z1, x2, y2, z2;
        cin>>x1>>y1>>z1>>x2>>y2>>z2;
        --x1, --y1, -- x2, --y2;
        int k = min(z1, z2);
        ans[i] = abs(z1 - z2);
        Q[i] = {x1, y1, x2, y2, k}; 
        L[i] = 0;
        R[i] = k + 1;
    }

    vector<ar<int,3>> v;;
    for(int i = 0;i < n;i++){
        for(int j = 0;j < m;j++){
            v.push_back({A[i][j], i, j});
        }
    }
    sort(all(v));
    reverse(all(v));
    while(1){

        vector<ar<int,2>> que;
        for(int i = 0;i < q;i++){
            if(R[i] - L[i] > 1)que.push_back({(R[i] + L[i]) / 2, i});
        }
        if(que.empty())break;
        sort(all(que));
        reverse(all(que));
        int i = 0;
        DSU dsu(n, m);
        bool vis[n][m];
        memset(vis, 0, sizeof vis);
        for(auto [mid, j]: que){
            while(i < v.size() && v[i][0] >= mid){
                int x = v[i][1];
                int y = v[i][2];
                vis[x][y] = 1;
                for(int d = 0;d < 4;d++){
                    int nx = x + dx[d];
                    int ny = y + dy[d];
                    if(nx >= 0 && nx < n && ny >= 0 && ny < m && vis[nx][ny])dsu.upd(x, y, nx, ny);
                }
                i++;
            }
            if(dsu.qry(Q[j][0], Q[j][1], Q[j][2], Q[j][3]))L[j] = mid;
            else R[j] = mid;
        }
    }
    for(int i = 0;i < q;i++)cout<<ans[i] + 2 * (Q[i][4] - L[i])<<'\n';
}   
signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--)orz();
}  