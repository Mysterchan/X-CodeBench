#include <iostream>
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

using vi = vector<ll>;
#define pb push_back
#define nl '\n'
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()

const int MOD = 1000000007;

void setIO(string name = "")
{
    cin.tie(0)->sync_with_stdio(0);
    if (sz(name))
    {
        freopen((name + ".in").c_str(), "r", stdin);
        freopen((name + ".out").c_str(), "w", stdout);
    }
}
template <typename T>
void debug(T x) { cout << x << nl; }

void read(vector<ll> &a, int n)
{
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--)
    {
        int n, s;
        cin >> n >> s;
        int ans = 0;
        while (n--)
        {
            int dx, dy, x, y;
            cin >> dx >> dy >> x >> y;
            int px = dx == 1 ? s - x : x, py = dy == 1 ? s - y : y;
            ans += (px == py);
        }
        cout << ans << nl;
    }
}
