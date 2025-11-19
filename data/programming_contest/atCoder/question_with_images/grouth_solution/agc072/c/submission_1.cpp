#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

namespace PTqwq {

int readqwq() {
    int x = 0;
    bool f = false;
    char c = getchar();
    for (; c < '0' || c > '9'; c = getchar()) f |= (c == '-');
    for (; c >= '0' && c <= '9'; c = getchar()) x = (x << 1) + (x << 3) + (c - '0');
    if (f) {
        x = -x;
    }
    return x;
}

ll readllqwq() {
    ll x = 0;
    bool f = false;
    char c = getchar();
    for (; c < '0' || c > '9'; c = getchar()) f |= (c == '-');
    for (; c >= '0' && c <= '9'; c = getchar()) x = (x << 1) + (x << 3) + (c - '0');
    if (f) {
        x = -x;
    }
    return x;
}

ll dp[120][120];
vector<int> ans;

void Solve() {
    int n = readqwq();
    ll k = readllqwq();
    for (int i = 1; i <= n; ++ i) {
        for (int j = 1; j <= n; ++ j) {
            dp[i][j] = 0;
        }
    }
    k --;
    dp[1][1] = k;
    for (ll i = 1; i <= n; ++ i) {
        for (ll j = 1; j <= n; ++ j) {
            ll T = dp[i][j] / (i + j);
            ll cntD = 0, cntR = 0;
            if (dp[i][j] % (i + j) <= i) {
                cntD = dp[i][j] % (i + j);
            } else {
                cntD = i;
                cntR = dp[i][j] % (i + j) - i;
            }
            if (i < n) {
                dp[i + 1][j] += (T * i + cntD);
            }
            if (j < n) {
                dp[i][j + 1] += (T * j + cntR);
            }
        }
    }
    int x = 1, y = 1;
    for (int i = 1; i <= n - 1; ++ i) {
        if (dp[x + 1][y] < dp[x][y + 1]) {
            x ++; ans.push_back(1);
        } else if (dp[x][y + 1] < dp[x + 1][y]) {
            y ++; ans.push_back(0);
        } else {
            x ++; ans.push_back(1);
        }
    }
    vector<int> sta = ans;
    while (!sta.empty()) {
        ans.push_back(1 - sta.back());
        sta.pop_back();
    }
    for (auto i : ans) {
        if (i == 0) {
            printf("R");
        } else {
            printf("D");
        }
    }
    printf("\n");
}

}

int main() {
    PTqwq::Solve();

    return 0;
}