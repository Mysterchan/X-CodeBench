#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
#define pb push_back
#define all(a) a.begin(), a.end()
#define sz(a) ((int)a.size())
#ifdef Doludu
template <typename T>
ostream& operator << (ostream &o, vector<T> vec) {
    o << "{"; int f = 0;
    for (T i : vec) o << (f++ ? " " : "") << i;
    return o << "}";
}
void bug__(int c, auto ...a) {
    cerr << "\e[1;" << c << "m";
    (..., (cerr << a << " "));
    cerr << "\e[0m" << endl;
}
#define bug_(c, x...) bug__(c, __LINE__, "[" + string(#x) + "]", x)
#define bug(x...) bug_(32, x)
#define bugv(x...) bug_(36, vector(x))
#define safe bug_(33, "safe")
#else
#define bug(x...) void(0)
#define bugv(x...) void(0)
#define safe void(0)
#endif
const int mod = 998244353, N = 300007;

int main() {
    ios::sync_with_stdio(false), cin.tie(0);
    int n;
    cin >> n;
    vector <int> p(n);
    for (int i = 0; i < n; ++i) cin >> p[i], --p[i];
    vector <int> cnt(n + 1);
    vector <int> vis(n);
    vector <int> vec;
    int even_tot = 0;
    for (int i = 0; i < n; ++i) if (!vis[i]) {
        int c = 0;
        for (int j = i; !vis[j]; j = p[j]) vis[j] = true, c++;
        vec.pb(c);
        if (c % 2 == 0) even_tot += c / 2, cnt[c / 2]++;
    }
    for (int i = 1; i <= n; ++i) {
        while (cnt[i] > 2) cnt[i * 2]++, cnt[i] -= 2;
    }
    bitset <N> dp; dp.reset();
    dp[0] = 1;
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < cnt[i]; ++j) dp |= dp << i;
    }
    sort(all(vec), [&](int i, int j) {
        if ((i % 2) == (j % 2)) return i > j;
        return i % 2 == 0;
    });
    bug(vec);
    int q; cin >> q;
    while (q--) {
        int a, b, c; cin >> a >> b >> c;
        int base = 2 * a;
        if (a == b && a <= even_tot) {
            if (dp[a]) {
                cout << 4 * a << "\n";
            } else {
                cout << 4 * a - 1 << "\n";
            }
            continue;
        }
        int cnt00 = 0, cnt1 = 0, cnt2 = 0;
        for (int x : vec) {
            if (!a) break;
            if (x % 2 == 0) {
                if (a >= x / 2) {
                    cnt2 += x / 2;
                    a -= x / 2;
                } else {
                    cnt1 += 2;
                    cnt2 += a - 1;
                    a = 0;
                }
            } else if (x > 1) {
                int mn = min(a, x / 2);
                cnt1 += 2;
                cnt2 += mn - 1;
                a -= mn;
            }
        }
        for (int x : vec) {
            if (!a) break;
            if (x % 2 == 1) {
                a--;
                cnt00++;
                if (x > 1) {
                    cnt1 -= 2;
                    cnt2++;
                }
            }
        }
        cnt00 += a * 2;
        cnt2 -= a;
        a = 0;

        int ans = base - cnt00;
        int mn = min(b, cnt2);
        ans += mn * 2;
        b -= mn;
        ans += min(b, cnt1);
        
        cout << ans << "\n";
    }
}