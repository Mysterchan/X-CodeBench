#include <bits/stdc++.h>
using namespace std;
#define rep(i, a, n) for(int i = a; i < n; i++)
#define rrep(i, a, n) for(int i = a; i >= n; i--)
#define inr(l, x, r) (l <= x && x < r)
#define ll long long
#define ld long double

constexpr int IINF = 1001001001;
constexpr ll INF = 1e18;

template<class t,class u> void chmax(t&a,u b){if(a<b)a=b;}
template<class t,class u> void chmin(t&a,u b){if(b<a)a=b;}


int main(){
    int n, k; cin >> n >> k;
    vector<int> p(n*k);
    rep(i, 0, n*k){
        cin >> p[i]; p[i]--;
    }

    int ans = 0;
    vector<int> seen(n*k);
    rep(i, 0, n*k){
        if(seen[i]) continue;
        int pos = i;
        vector<int> q;
        while(!seen[pos]){
            q.push_back(pos);
            seen[pos] = 1;
            pos = p[pos];
        }
        int m = (int)q.size();
        if(m == 1) continue;

        vector<vector<int>> dp(m+1, vector<int>(m+1));
        rrep(l, m-1, 0){
            vector<int> same;
            rep(j, l+1, m){
                if(q[l]%n == q[j]%n) same.push_back(j);
            }
            rep(r, l+1, m+1){
                dp[l][r] = dp[l+1][r];
                for(auto nr: same){
                    if(nr < r) chmax(dp[l][r], dp[l+1][nr+1]+dp[nr][r]+1);
                }
            }
        }
        ans += dp[0][m];
    }
    cout << ans << endl;
    
    return 0;
}