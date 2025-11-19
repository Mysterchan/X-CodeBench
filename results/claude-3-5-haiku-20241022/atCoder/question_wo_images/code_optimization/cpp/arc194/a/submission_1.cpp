#include <bits/stdc++.h>
using namespace std;
using ll = long long;

void solve();

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);
    int t = 1;
    while (t--) {
        solve();
    }
    return 0;
}

constexpr int N = 2e5 + 3;
ll a[N];

struct State {
    ll sum;
    int size;
    ll last;
};

void solve() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }
    
    State dp[2][2];
    dp[1][0] = {0, 0, 0};
    dp[1][1] = {0, 0, 0};
    
    int now = 1;
    for (int i = 1; i <= n; ++i) {
        const int last = now;
        now ^= 1;
        
        // Operation 0: append a[i]
        if (dp[last][0].sum > dp[last][1].sum || 
            (dp[last][0].sum == dp[last][1].sum && dp[last][0].size >= dp[last][1].size)) {
            dp[now][0] = {dp[last][0].sum + a[i], dp[last][0].size + 1, a[i]};
        } else {
            dp[now][0] = {dp[last][1].sum + a[i], dp[last][1].size + 1, a[i]};
        }
        
        // Operation 1: delete last element
        ll quFang = (dp[last][0].size == 0) ? 0 : dp[last][0].sum - dp[last][0].last;
        ll quTan = (dp[last][1].size == 0) ? 0 : dp[last][1].sum - dp[last][1].last;
        
        if (quFang > quTan || 
            (quFang == quTan && dp[last][0].size >= dp[last][1].size)) {
            if (dp[last][0].size == 0) {
                dp[now][1] = {a[i], 1, a[i]};
            } else {
                dp[now][1] = {quFang, dp[last][0].size - 1, 
                              (dp[last][0].size == 1) ? 0 : dp[last][0].last};
            }
        } else {
            if (dp[last][1].size == 0) {
                dp[now][1] = {a[i], 1, a[i]};
            } else {
                dp[now][1] = {quTan, dp[last][1].size - 1,
                              (dp[last][1].size == 1) ? 0 : dp[last][1].last};
            }
        }
    }
    
    cout << max(dp[now][0].sum, dp[now][1].sum) << '\n';
}