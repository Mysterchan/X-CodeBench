#include<bits/stdc++.h>
using namespace std;
using i64 = long long;
using u64 = unsigned long long;

constexpr int inf = 1e9;
constexpr i64 INF = LLONG_MAX;
constexpr int N = 2e6 + 10;
constexpr int P = 676767677;
constexpr int K = 0;
constexpr double eps = 1e-6;

void solve() {
    i64 x;
    cin >> x;

    int ans = 1;
    while(x != 1) {
        ans++;
        x /= ans;
    }

    cout << ans << "\n";
    return;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    int t = 1;
    while(t--) solve();
    return 0;
}