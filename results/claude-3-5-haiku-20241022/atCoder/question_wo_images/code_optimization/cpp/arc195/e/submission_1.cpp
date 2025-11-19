#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N = 200005, M = 998244353;

int ast(int x, int n)
{
    int ans = 1;
    while (n)
    {
        if (n % 2 == 1)
            ans = (ans * 1LL * x) % M;
        x = (x * 1LL * x) % M;
        n /= 2;
    }
    return ans;
}

int f[N], rf[N];
void pre()
{
    f[0] = 1;
    for (int i = 1; i < N; ++i)
        f[i] = (f[i - 1] * 1LL * i) % M;
    rf[N - 1] = ast(f[N - 1], M - 2);
    for (int i = N - 2; i >= 0; --i)
        rf[i] = (rf[i + 1] * 1LL * (i + 1)) % M;
}

int C(int n, int k)
{
    if (k < 0 || k > n)
        return 0;
    return (f[n] * 1LL * rf[k]) % M * rf[n - k] % M;
}

int n, qq;
int a[N];
int dp[N];
int p[N];
int s[N];
int ss[N];

void solv()
{
    cin >> n >> qq;
    for (int x = 2; x <= n; ++x)
        cin >> a[x];

    for (int x = 2; x <= n; ++x)
    {
        dp[x] = (f[x - 1] * 1LL * a[x]) % M;
        dp[x] = (dp[x] + p[x - 1] * 1LL * f[x - 2]) % M;
        p[x] = (p[x - 1] + dp[x] * 1LL * rf[x - 1]) % M;
    }

    for (int x = 2; x <= n; ++x)
    {
        int numer = (f[n - 1] * 1LL * (x - 1)) % M;
        numer = (numer * 1LL * rf[n - x]) % M;
        s[x] = numer;
        
        ll contrib = (f[n - 1] * 1LL * (x - 1)) % M;
        contrib = (contrib * 1LL * rf[n - x + 1]) % M;
        contrib = (contrib * 1LL * (n - x + 1)) % M;
        s[x] = (s[x] - contrib + M) % M;
    }
    
    for (int x = 2; x <= n; ++x)
    {
        ll val = (f[n - 1] * 1LL * (x - 1)) % M;
        val = (val * 1LL * rf[n - x + 1]) % M;
        ss[x] = val;
    }

    for (int x = 2; x <= n; ++x)
        s[x] = (s[x - 1] + s[x] * 1LL * a[x]) % M;
    for (int x = 2; x <= n; ++x)
        ss[x] = (ss[x] * 1LL * a[x]) % M;
    
    while (qq--)
    {
        int x, y;
        cin >> x >> y;

        if (x == 1)
        {
            int ans = (dp[y] * 1LL * f[n - 1]) % M;
            ans = (ans * 1LL * rf[y - 1]) % M;
            cout << ans << "\n";
            continue;
        }
        int ans = (dp[x] * 1LL * f[n - 1]) % M;
        ans = (ans * 1LL * rf[x - 1]) % M;
        int yans = (dp[y] * 1LL * f[n - 1]) % M;
        yans = (yans * 1LL * rf[y - 1]) % M;
        ans = (ans + yans) % M;
        yans = (s[x - 1] + ss[x]) % M;
        ans = (ans - yans) % M;
        ans = (ans - yans) % M;
        ans = (ans + M + M) % M;
        cout << ans << "\n";
    }
}

int main()
{
    ios_base::sync_with_stdio(false), cin.tie(0);
    pre();
    int tt = 1;
    while (tt--)
    {
        solv();
    }
    return 0;
}