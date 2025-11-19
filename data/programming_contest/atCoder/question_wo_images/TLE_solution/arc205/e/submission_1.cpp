#include <bits/stdc++.h>
#define fi first
#define se second
#define int long long
#define pb emplace_back
#define F(i, a, b) for (int i = (a); i <= (b); ++i)
#define dF(i, a, b) for (int i = (a); i >= (b); --i)
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

const int N = 400005, B = 10000, mod = 998244353;
int n, a[N], s[1 << 20], f[1 << 20];
signed main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);
    cin >> n;
    F(i, 1, n) 
        cin >> a[i];
    int lst = 1;
    fill(s, s + (1 << 20), 1);
    fill(f, f + (1 << 20), 1);
    F(i, 1, n) {
        if (i % B == 0) {
            F(j, lst, i) f[a[j]] = f[a[j]] * a[j] % mod;
            memcpy(s, f, sizeof f);
            F(j, 0, 19) F(k, 1, (1 << 20) - 1) 
                if (k >> j & 1) s[k] = s[k] * s[k ^ (1 << j)] % mod;
            lst = i + 1;
        }
        int ans = s[a[i]];
        F(j, lst, i) {
            if ((a[j] | a[i]) == a[i]) {
                ans = ans * a[j] % mod;
            }
        }
        cout << ans << '\n';
    }
    return 0;
}