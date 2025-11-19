#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll dp[20][10][2][2]; // pos, maxDigit, isLimit, isNumStarted

// digits vector to store the digits of the number
vector<int> digits;

// pos: current position in digits
// maxDigit: the top digit chosen (most significant digit)
// isLimit: whether the current prefix is limited by the original number's prefix
// isNumStarted: whether we have chosen the top digit yet
ll dfs(int pos, int maxDigit, bool isLimit, bool isNumStarted) {
    if (pos == (int)digits.size()) {
        // If number started (top digit chosen), count 1
        return isNumStarted ? 1 : 0;
    }
    if (dp[pos][maxDigit][isLimit][isNumStarted] != -1) {
        return dp[pos][maxDigit][isLimit][isNumStarted];
    }
    ll res = 0;
    int up = isLimit ? digits[pos] : 9;
    for (int d = 0; d <= up; d++) {
        if (!isNumStarted) {
            // We haven't chosen the top digit yet
            // We can choose d as top digit if d > 0 (since number >= 10)
            // or skip leading zeros (but number must be >= 10, so leading zero not allowed)
            if (d == 0) continue; // top digit can't be zero
            // Choose d as top digit
            res += dfs(pos + 1, d, isLimit && (d == up), true);
        } else {
            // Number started, top digit fixed as maxDigit
            // Check if current digit d < maxDigit
            if (d < maxDigit) {
                res += dfs(pos + 1, maxDigit, isLimit && (d == up), true);
            }
            // else skip d >= maxDigit
        }
    }
    return dp[pos][maxDigit][isLimit][isNumStarted] = res;
}

ll solve(ll x) {
    if (x < 10) return 0; // no snake numbers less than 10
    digits.clear();
    while (x > 0) {
        digits.push_back(x % 10);
        x /= 10;
    }
    reverse(digits.begin(), digits.end());
    memset(dp, -1, sizeof(dp));
    return dfs(0, 0, true, false);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll L, R;
    cin >> L >> R;
    cout << solve(R) - solve(L - 1) << "\n";
    return 0;
}