#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <array>
#define endl '\n'
#define ll long long
using namespace std;
const ll mod = 998244353;


void eachT()
{
    int n;
    cin >> n;
    vector<array<ll, 3>>dp(n + 1);
    vector<int>a(n + 1);
    for (int i = 1; i <= n; i++)
        cin >> a[i];
    dp[0][2] = 1;
    for (int i = 1; i <= n; i++)
    {
        if (a[i] == -1 || a[i] == i - 1)
            dp[i][0] += dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2], dp[i][0] %= mod;
        if (a[i] == -1 || a[i] != i - 1 && a[i] != i + 1)
            dp[i][1] += dp[i - 1][2]*(n-2)%mod, dp[i][1] %= mod;
        if (a[i] == -1 || a[i] == i + 1)
            dp[i][2] += dp[i - 1][2], dp[i][2] %= mod;
    }
    cout << (dp[n][0] + dp[n][1] + dp[n][2]) % mod << endl;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);
    int T = 1;
    while (T--)
        eachT();
}