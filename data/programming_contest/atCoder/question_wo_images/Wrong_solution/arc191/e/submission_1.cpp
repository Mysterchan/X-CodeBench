#include <bits/stdc++.h>
using namespace std;

constexpr int N = 2e5 + 5, MOD = 998244353;

int n, x, y;
array<int, N> a, b, fac, ifac, suf;

inline int qpow(int a, int b)
{
    int res = 1, base = a;
    while (b)
    {
        if (b & 1) res = 1ll * res * base % MOD;
        base = 1ll * base * base % MOD;
        b >>= 1;
    }
    return res;
}

inline int binom(int n, int m)
{
    if (n < m || n < 0 || m < 0) return 0;
    return 1ll * fac[n] * ifac[m] % MOD * ifac[n - m] % MOD;
}

int main()
{
    ios::sync_with_stdio(0), cin.tie(0);
    fac[0] = 1;
    for (int i = 1; i < N; i++) fac[i] = 1ll * fac[i - 1] * i % MOD;
    ifac[N - 1] = qpow(fac[N - 1], MOD - 2);
    for (int i = N - 2; i >= 0; i--) ifac[i] = 1ll * ifac[i + 1] * (i + 1) % MOD;
    cin >> n >> x >> y;
    for (int i = 1; i <= n; i++) cin >> a[i] >> b[i];
    if ((x & 1) && (y & 1))
    {
        int c0 = 0, c1 = 0;
        for (int i = 1; i <= n; i++) c0 += (b[i] & 1);
        c1 = n - c0;
        int ans = 0;
        int res = qpow(2, c1);
        for (int i = c0 / 2 + 1; i <= c0; i++) ans += 1ll * binom(c0, i) * res % MOD, ans >= MOD ? ans -= MOD : 0;
        cout << ans << "\n";
    }
    else if (x % 2 == 0 && y % 2 == 0)
    {
        int c0 = 0, c1 = 0;
        for (int i = 1; i <= n; i++) c0 += (b[i] & 1) || (a[i] & 1);
        c1 = n - c0;
        int ans = 0;
        int res = qpow(2, c1);
        for (int i = c0 / 2 + 1; i <= c0; i++) ans += 1ll * binom(c0, i) * res % MOD, ans >= MOD ? ans -= MOD : 0;
        cout << ans << "\n";
    }
    else if ((x & 1) && y % 2 == 0)
    {
        int c2 = 0, c10 = 0, c00 = 0;
        for (int i = 1; i <= n; i++)
        {
            int x = a[i] & 1, y = b[i] & 1;
            if (!x && !y) c00++;
            else if (!x && y) c2++;
            else if (x && !y) c10++;
            else c2++;
        }
        for (int y = c10; y >= 0; y--)
        {
            suf[y] = suf[y + 1] + binom(c10, y);
            suf[y] >= MOD ? suf[y] -= MOD : 0;
        }
        int v0 = qpow(2, c00), ans = 0;
        for (int x = 0; x <= c2; x++)
        {
            int res = binom(c2, x);
            int ylim = max(0, c2 + c10 - 2 * x + 1);
            res = 1ll * res * suf[min(ylim, N - 1)] % MOD * v0 % MOD;
            ans += res, ans >= MOD ? ans -= MOD : 0;
        }
        cout << ans << "\n";
    }
    else
    {
        int c2 = 0, c10 = 0, c00 = 0;
        for (int i = 1; i <= n; i++)
        {
            int x = a[i] & 1, y = b[i] & 1;
            if (!x && !y) c00++;
            else if (!x && y) c2++;
            else if (x && !y) c10++;
            else c2++;
        }
        for (int y = c10; y >= 0; y--)
        {
            suf[y] = suf[y + 1] + binom(c10, y);
            suf[y] >= MOD ? suf[y] -= MOD : 0;
        }
        int v0 = qpow(2, c00), ans = 0;
        for (int x = 0; x <= c2; x++)
        {
            int res = binom(c2, x);
            int ylim = max(0, c2 - 2 * x + 1);
            res = 1ll * res * suf[min(ylim, N - 1)] % MOD * v0 % MOD;
            ans += res, ans >= MOD ? ans -= MOD : 0;
        }
        cout << ans << "\n";
    }
    return 0;
}

