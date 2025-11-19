#include <bits/stdc++.h>
using namespace std;

#define pi pair<int, int>
#define int int64_t
#define all(x) (x).begin(), (x).end()

const int MOD = 1000000007;

int dp[805][805];

void solve()
{
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];
    if (n < 3)
    {
        cout << 0 << "\n";
        return;
    }
    vector<int> vals(2 * n);
    for (int i = 0; i < 2 * n; i++)
        vals[i] = a[i % n];
    memset(dp, 0, sizeof(dp));
    auto getDP = [&](int l, int r) -> int
    {
        if (l > r)
            return 0;
        return dp[l][r];
    };
    for (int l = 0; l + 2 < 2 * n; l++)
        dp[l][l + 2] = vals[l] * vals[l + 1] * vals[l + 2];
    for (int length = 4; length <= n; length++)
    {
        for (int l = 0; l + length - 1 < 2 * n; l++)
        {
            int r = l + length - 1;
            dp[l][r] = max(dp[l + 1][r], dp[l][r - 1]);

            for (int i = l + 1; i + 1 <= r; i++)
            {
                for (int j = i + 1; j <= r; j++)
                {
                    int sumVal = getDP(l + 1, i - 1) + getDP(i + 1, j - 1) + getDP(j + 1, r) + vals[l] * vals[i] * vals[j];
                    dp[l][r] = max(dp[l][r], sumVal);
                }
            }
        }
    }
    int ans = 0;
    for (int i = 0; i < n; i++)
        ans = max(ans, dp[i][i + n - 1]);
    cout << ans << "\n";
}

signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;
    while (t--)
        solve();

    return 0;
}