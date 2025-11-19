#include <bits/stdc++.h>
using namespace std;
#define m_p make_pair
#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x).size())
#define fi first
#define se second
typedef long long ll;
mt19937 rnd(chrono::steady_clock::now().time_since_epoch().count());
mt19937 rnf(2106);
const int N = 200005;

int n;
int a[N];

int F(int l, int r, int q1)
{
    l += 2;
    r -= 1;
    if (l > r)
        return 0;
    if (l == 1 && r == n)
    {
        if (q1 == n)
            return 0;
        return 2 - (r - l + 1);
    }
    return 1 - (r - l + 1);
}

int go()
{
    set<int> s;
    a[n + 1] = a[n + 2] = 0;
    s.insert(-1);
    for (int i = 0; i <= n + 1; ++i)
    {
        if (a[i] + a[i + 1] == 0)
            s.insert(i);
    }
    int q000 = 0;
    for (int i = 1; i + 2 <= n; ++i)
    {
        if (a[i] + a[i + 1] + a[i + 2] == 0)
            ++q000;
    }
    int q1 = 0;
    for (int i = 1; i <= n; ++i)
        q1 += a[i];

    int ans = n;
    ans -= q000;
    for (auto it = s.begin(); it != s.end(); ++it)
    {
        auto jt = it;
        ++jt;
        if (jt != s.end())
            ans += F(*it, *jt, q1);
    }
    return ans;
}

void solv()
{
    cin >> n;
    for (int i = 1; i <= n; ++i)
        cin >> a[i];

    set<int> s;
    a[n + 1] = a[n + 2] = 0;
    s.insert(-1);
    for (int i = 0; i <= n + 1; ++i)
    {
        if (a[i] + a[i + 1] == 0)
            s.insert(i);
    }
    int q000 = 0;
    for (int i = 1; i + 2 <= n; ++i)
    {
        if (a[i] + a[i + 1] + a[i + 2] == 0)
            ++q000;
    }
    int q1 = 0;
    for (int i = 1; i <= n; ++i)
        q1 += a[i];

    int qq;
    cin >> qq;
    while (qq--)
    {
        int i;
        cin >> i;
        a[i] ^= 1;

        cout << go() << "\n";
    }
}

int main()
{
    #ifdef SOMETHING
    freopen("input.txt", "r", stdin);
    #endif
    ios_base::sync_with_stdio(false), cin.tie(0);

    int tt = 1;
    while (tt--)
    {
        solv();
    }
    return 0;
}
