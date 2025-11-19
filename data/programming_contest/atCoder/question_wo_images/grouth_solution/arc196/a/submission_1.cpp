#include <iostream>
#include <vector>
#include <set>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 300005;
int n, a[N];
long long ans, sum1, sum2, f[N], g[N];
multiset<int> s1, s2;
void solve(long long *dp)
{
    sum1 = sum2 = 0;
    s1.clear(), s2.clear();
    for (int i = 2; i <= n; i += 2)
    {
        s2.insert(a[i]), sum2 += a[i];
        s2.insert(a[i - 1]), sum2 += a[i - 1];
        while (s1.size() != s2.size())
        {
            s1.insert(*s2.begin());
            sum2 -= *s2.begin();
            sum1 += *s2.begin();
            s2.erase(s2.begin());
        }
        if (s1.size())
        {
            while (*s1.rbegin() > *s2.begin())
            {
                s1.insert(*s2.begin());
                sum2 -= *s2.begin();
                sum1 += *s2.begin();
                s2.erase(s2.begin());
                s2.insert(*s1.rbegin());
                sum2 += *s1.rbegin();
                sum1 -= *s1.rbegin();
                s1.erase(--s1.end());
            }
        }
        dp[i] = sum2 - sum1;
    }
}
signed main()
{
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> a[i];
    if (!(n & 1))
    {
        sort(a + 1, a + n + 1);
        for (int i = 1; 2 * i <= n; i++)
        {
            ans += a[n - i + 1] - a[i];
        }
    }
    else
    {
        solve(f), reverse(a + 1, a + n + 1), solve(g);
        for (int i = 1; i <= n; i += 2)
        {
            ans = max(ans, f[i - 1] + g[n - i]);
        }
    }
    cout << ans << endl;
}