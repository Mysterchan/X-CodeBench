#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;
#define ll long long int
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define pb push_back
#define pp pop_back()
#define mod 1000000007
#define endl "\n"
#define N 200005
ll dx[] = { 1, -1, 0, 0, 1, 1, -1, -1 };
ll dy[] = { 0, 0, 1, -1, 1, -1, 1, -1 };
template <typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

ll n, m , ans;

bool valid(ll &x, ll &y,const vector<string>&s) {

    for (int i = 0;i + 1 < n;i++) {
        for (int j = 0;j + 1 < m;j++) {
            if (s[i][j] == '#' && s[i + 1][j] == '#' && s[i][j + 1] == '#' && s[i + 1][j + 1] == '#') {
                x = i, y = j;
                return true;
            }
        }
    }
    return false;
}

void dfs(ll cnt, vector<string>&s) {

    if (cnt >= ans) return;

    ll i, j;
    if (!valid(i, j,s)) {
        ans = min(ans, cnt);
        return;
    }
    vector<pair<ll, ll>> dir = { {i,j},{i + 1,j},{i,j + 1},{i + 1,j + 1} };

    for (auto [x1, y1] : dir) {
        if (s[x1][y1] == '#') {
            s[x1][y1] = '.';
            dfs(cnt + 1,s);
            s[x1][y1] = '#';
        }
    }
}

void domain_expension() {
    cin >> n >> m;
    vector<string>s(n);
    for (int i = 0;i < n;i++) cin >> s[i];


    ans = LLONG_MAX;
    dfs(0,s);

    cout << ans << endl;
}
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    while (t--)
        domain_expension();
    return 0;
}