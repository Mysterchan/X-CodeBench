#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
#define pb push_back
#define all(a) a.begin(), a.end()
#define sz(a) ((int)a.size())
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
    
    // Precompute prefix sums for fast query processing
    int m = sz(vec);
    vector<int> pref_even_half(m + 1), pref_odd_floor(m + 1);
    vector<int> even_cnt(m + 1), odd_gt1_cnt(m + 1), odd_cnt(m + 1);
    
    for (int i = 0; i < m; ++i) {
        pref_even_half[i + 1] = pref_even_half[i];
        pref_odd_floor[i + 1] = pref_odd_floor[i];
        even_cnt[i + 1] = even_cnt[i];
        odd_gt1_cnt[i + 1] = odd_gt1_cnt[i];
        odd_cnt[i + 1] = odd_cnt[i];
        
        if (vec[i] % 2 == 0) {
            pref_even_half[i + 1] += vec[i] / 2;
            even_cnt[i + 1]++;
        } else {
            if (vec[i] > 1) {
                pref_odd_floor[i + 1] += vec[i] / 2;
                odd_gt1_cnt[i + 1]++;
            }
            odd_cnt[i + 1]++;
        }
    }
    
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
        int a_orig = a;
        
        // Binary search for how many even cycles we can fully use
        int lo = 0, hi = even_cnt[m];
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (pref_even_half[mid] <= a) lo = mid;
            else hi = mid - 1;
        }
        
        if (lo < even_cnt[m] && pref_even_half[lo] < a) {
            cnt2 += pref_even_half[lo];
            a -= pref_even_half[lo];
            // Partial even cycle
            cnt1 += 2;
            cnt2 += a - 1;
            a = 0;
        } else if (lo == even_cnt[m]) {
            cnt2 += pref_even_half[lo];
            a -= pref_even_half[lo];
        }
        
        // Process odd cycles > 1
        if (a > 0) {
            int take = min(a, odd_gt1_cnt[m]);
            cnt1 += take * 2;
            cnt2 += min(a, pref_odd_floor[m]) - take;
            a -= take;
        }
        
        // Process remaining odd cycles of size 1
        int odd1_used = min(a, odd_cnt[m] - odd_gt1_cnt[m]);
        cnt00 += odd1_used;
        a -= odd1_used;
        
        // Adjust for odd cycles > 1 when we use their center
        int adjust = min(odd1_used, odd_gt1_cnt[m]);
        if (adjust > 0 && odd_gt1_cnt[m] > 0) {
            cnt1 -= adjust * 2;
            cnt2 += adjust;
        }
        
        cnt00 += a * 2;
        cnt2 -= a;

        int ans = base - cnt00;
        int mn = min(b, cnt2);
        ans += mn * 2;
        b -= mn;
        ans += min(b, cnt1);
        
        cout << ans << "\n";
    }
}