#include <bits/stdc++.h>
#pragma GCC optimize ("O3,unroll-loops")
#pragma GCC target ("avx,avx2,fma")

#define endl '\n'
using namespace std;
using ll = long long;
using vl = vector<ll>;
using vvl = vector<vl>;
using pll = pair<ll, ll>;
using ld = long double;

void setup() {
#ifdef KIMHS
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
#endif
}

template <typename T>
istream& operator>>(istream &is, vector<T> &arr) {
    for (auto &x: arr) is>>x;
    return is;
}

constexpr ll MOD = 1e9+7;
constexpr ll INF = 2e18;

void preprocess() {
    ll i, j;
}

void solve(ll tc) {
    int i, j, k;
    ll n; cin>>n;
    ll px, py, qx, qy; cin>>px>>py>>qx>>qy;
    vector<int> arr(n); cin>>arr;
    unordered_map<int, bool> dp;
    dp[arr[0]] = 1;
    for (i=1;i<n;i++) {
        unordered_map<int, bool> new_dp;
        for (j=-10000;j<=10000;j++) {
            if (dp[j-arr[i]]) new_dp[j] = 1;
            if (dp[j+arr[i]]) new_dp[j] = 1;
        }
        swap(dp, new_dp);
    }
    int min_dist = INF, max_dist = accumulate(arr.begin(), arr.end(), 0LL);
    for (auto &it: dp) min_dist = min(min_dist, abs(it.first));
    ll dist = (px-qx)*(px-qx) + (py-qy)*(py-qy);
    if ((ll)min_dist*min_dist <= dist && dist <= (ll)max_dist*max_dist) cout<<"Yes\n";
    else cout<<"No\n";
}

int main() {
    setup();
    preprocess();

    ll testcase = 1;
    cin >> testcase;
    for (ll i = 1; i <= testcase; i++) {
        solve(i);
    }
}