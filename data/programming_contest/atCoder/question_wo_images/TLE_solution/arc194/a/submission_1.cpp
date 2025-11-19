#include <bits/stdc++.h>
#define chmax(a, b) do { \
    if ((b) > a) a = (b); \
} while(0)
#define chmin(a, b) do { \
    if ((b) < a) a = (b); \
} while(0)
#define ft first
#define sd second
using namespace std;
using ll = long long;
using pii = pair<int, int>;

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

void solve() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }
    ll dp_sum[2][2] = {0};
    stack<ll> dp_value[2][2];
    int now = 1;
    for (int i = 1; i <= n; ++i) {
        const int last = now;
        now ^= 1;

        if (dp_sum[last][0] == dp_sum[last][1]) {
            if (dp_value[last][0].size() >= dp_value[last][1].size()) {
                dp_sum[now][0] = dp_sum[last][0] + a[i];
                dp_value[now][0] = dp_value[last][0];
            } else {
                dp_sum[now][0] = dp_sum[last][1] + a[i];
                dp_value[now][0] = dp_value[last][1];
            }
        } else if (dp_sum[last][0] > dp_sum[last][1]) {
            dp_sum[now][0] = dp_sum[last][0] + a[i];
            dp_value[now][0] = dp_value[last][0];
        } else {
            dp_sum[now][0] = dp_sum[last][1] + a[i];
            dp_value[now][0] = dp_value[last][1];
        }
        dp_value[now][0].push(a[i]);

        const ll quFang = (dp_value[last][0].empty() ? a[i] : dp_sum[last][0] - dp_value[last][0].top());
        const ll quTan = (dp_value[last][1].empty() ? a[i] : dp_sum[last][1] - dp_value[last][1].top());
        if (quFang == quTan) {
            dp_sum[now][1] = quFang;
            if (dp_value[last][0].size() >= dp_value[last][0].size()) {
                if (dp_value[last][0].empty()) {
                    dp_value[last][0].push(a[i]);
                } else {
                    dp_value[last][0].pop();
                }
                dp_value[now][1] = dp_value[last][0];
            } else {
                if (dp_value[last][1].empty()) {
                    dp_value[last][1].push(a[i]);
                } else {
                    dp_value[last][1].pop();
                }
                dp_value[now][1] = dp_value[last][1];
            }
        } else if (quFang > quTan) {
            dp_sum[now][1] = quFang;
            if (dp_value[last][0].empty()) {
                dp_value[last][0].push(a[i]);
            } else {
                dp_value[last][0].pop();
            }
            dp_value[now][1] = dp_value[last][0];
        } else {
            dp_sum[now][1] = quTan;
            if (dp_value[last][1].empty()) {
                dp_value[last][1].push(a[i]);
            } else {
                dp_value[last][1].pop();
            }
            dp_value[now][1] = dp_value[last][1];
        }

    }

    cout << max(dp_sum[now][0], dp_sum[now][1]) << '\n';
}