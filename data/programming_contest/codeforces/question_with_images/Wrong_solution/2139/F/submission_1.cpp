#include <bits/stdc++.h>
using namespace std;
const int MAXN = 5010;
const int MOD = 1000000007;
long long fact[MAXN];
long long inv[MAXN];
long long modpow(long long base, long long exp)
{
    long long res = 1;
    while (exp)
    {
        if (exp & 1)
            res = res * base % MOD;
        base = base * base % MOD;
        exp >>= 1;
    }
    return res;
}
void precompute()
{
    fact[0] = 1;
    for (int i = 1; i < MAXN; i++)
    {
        fact[i] = fact[i - 1] * i % MOD;
    }
    inv[MAXN - 1] = modpow(fact[MAXN - 1], MOD - 2);
    for (int i = MAXN - 2; i >= 0; i--)
    {
        inv[i] = inv[i + 1] * (i + 1) % MOD;
    }
}
int main()
{
    precompute();
    int t;
    cin >> t;
    for (int test = 0; test < t; test++)
    {
        int n, m, q;
        cin >> n >> m >> q;
        vector<long long> a(n + 1);
        for (int i = 1; i <= n; i++)
        {
            cin >> a[i];
        }
        vector<pair<int, int>> ops(q + 1);
        for (int j = 1; j <= q; j++)
        {
            int i, x;
            cin >> i >> x;
            ops[j] = {i, x};
        }
        vector<int> type(q + 1);
        for (int j = 1; j <= q; j++)
        {
            int i = ops[j].first;
            int x = ops[j].second;
            if (x < a[i])
                type[j] = 0;
            else if (x > a[i])
                type[j] = 1;
            else
                type[j] = 2;
        }
        vector<long long> ans(n + 1);
        for (int k = 1; k <= n; k++)
        {
            long long sum_p = 0;
            int s = 0;
            for (int j = 1; j <= q; j++)
            {
                int i = ops[j].first;
                int x = ops[j].second;
                if (type[j] == 0 && i >= k || type[j] == 1 && i <= k)
                {
                    sum_p = (sum_p + x + k - i) % MOD;
                    s++;
                }
            }
            long long the_ans;
            if (s == 0)
            {
                the_ans = fact[q] * a[k] % MOD;
            }
            else
            {
                long long avg = sum_p * modpow(s, MOD - 2) % MOD;
                the_ans = fact[q] * avg % MOD;
            }
            ans[k] = the_ans;
        }
        for (int i = 1; i <= n; i++)
        {
            cout << ans[i] << " ";
        }
        cout << endl;
    }
    return 0;
}