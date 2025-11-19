#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <queue>
#include <ctime>
#include <cassert>
#include <complex>
#include <string>
#include <cstring>
#include <chrono>
#include <random>
#include <bitset>
#include <fstream>
#include <array>
#include <functional>
#include <memory>
using namespace std;
using ll = long long;
using ld = long double;
#define debug(x) std::cerr << __FUNCTION__ << ":" << __LINE__ << " " << #x << " = " << x << '\n';
const ll INF = 4e18;
const ll mod = 998244353;
ll get_sum(vector<vector<ll>> &dp, ll lvl, ll l, ll r){
    ll tor = 0;
    if (l == 0){
        tor = dp[lvl][r] % mod;
    }
    else{
        tor = (dp[lvl][r] - dp[lvl][l - 1] + mod) % mod;
    }
    return tor;
}
void solve(){
    ll n, m, d;
    cin >> n >> m >> d;
    vector<vector<char>> matrix(n, vector<char>(m, '.'));
    for (int i = 0; i < n; i++){
        for (int j =0; j < m; j++){
            cin >> matrix[i][j];
        }
    }
    reverse(matrix.begin(), matrix.end());
    vector<vector<ll>> dp(n, vector<ll>(m, 0));
    vector<ll> helperl(m);
    vector<ll> helperr(m);
    for (int i = 0; i < m; i++){
        for (int j = i; j >= 0; j--){
            ll rst = (j - i) * (j - i) + 1;
            if (rst <= d){
                helperl[i] = j;
            }
        }
        for (int j = i; j < m; j++){
            ll rst = (j - i) * (j - i) + 1;
            if (rst <= d){
                helperr[i] = j;
            }
        }
    }
    for (int i = 0; i < m; i++){
        if (matrix[0][i] == 'X'){
            dp[0][i]=1;
        }
    }
    vector<ll> tot(m);
    for (int i =1; i < m; i++){
        dp[0][i]+=dp[0][i-1];
        dp[0][i]%=mod;
    }
    for (int i =0; i < m; i++){
        if (matrix[0][i] == 'X') {
            tot[i] = get_sum(dp, 0, max(0LL, i - d), min(m - 1, i + d));
        }
        tot[i]%=mod;
    }
    dp[0]=tot;
    for (int i =1; i < m; i++){
        dp[0][i]+=dp[0][i-1];
        dp[0][i]%=mod;
    }
    for (int i = 1; i < n; i++){
        for (int j = 0; j < m; j++){
            tot[j]=0;
        }
        for (int j =0; j < m; j++){
            if (matrix[i][j] == 'X') {
                dp[i][j] = dp[i][j] + get_sum(dp, i - 1, helperl[j], helperr[j]);
                dp[i][j] %= mod;
            }
        }
        for (int j =1;j<m;j++){
            dp[i][j]+=dp[i][j-1];
            dp[i][j]%=mod;
        }
        for (int j =0; j < m; j++){
            if (matrix[i][j] =='X') {
                tot[j] = get_sum(dp, i, max(0LL, j - d), min(m - 1, j + d));
            }
            tot[j]%=mod;
        }
        dp[i]=tot;
        for (int j =1;j<m;j++){
            dp[i][j]+=dp[i][j-1];
            dp[i][j]%=mod;
        }
    }
    cout << dp[n - 1][m-1] % mod << '\n';
}
int main(){
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}