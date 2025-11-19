#include <bits/stdc++.h>
using namespace std;

#define ull unsigned long long
#define ll long long
#define ui unsigned int
#define sortva(v) sort(v.begin(), v.end())
#define endl "\n"
#define fon for (int i = 0; i < n; i++)
const ll MOD = 1e9 + 7;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--)
    {
        ll x, y;
        cin >> x >> y;
        ll ans = -1;
        if (y > x)
            ans = 2;
        if (ans == -1)
        {
            for (ll a = 1; a <= x; a++)
            {
                ll b = y;
                ll c = x - a;
                if (a < b && b < c && a + c == x && b == y)
                {
                    ans = 3;
                    break;
                }
            }
        }
        cout << ans << "\n";
    }

    return 0;
}
