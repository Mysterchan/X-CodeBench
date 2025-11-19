#include <bits/stdc++.h>
using namespace std;
const int N = 300007;

int main() {
    ios::sync_with_stdio(false), cin.tie(0);
    int n;
    cin >> n;
    vector<int> p(n);
    for (int i = 0; i < n; ++i) {
        cin >> p[i];
        --p[i]; // converting to zero-based index
    }
    
    vector<int> cycle_size; // To store sizes of cycles in permutation
    vector<bool> visited(n, false); // Keep track of visited nodes
    for (int i = 0; i < n; ++i) {
        if (!visited[i]) {
            int count = 0, j = i;
            do {
                visited[j] = true;
                j = p[j];
                ++count;
            } while (j != i);
            cycle_size.push_back(count);
        }
    }
    
    int even_count = 0; // Count of even-sized cycles
    vector<int> cnt(n + 1, 0); // Count of cycle sizes
    for (int size : cycle_size) {
        cnt[size]++;
        if (size % 2 == 0) even_count += size / 2;
    }
    
    // Convert pairs of cycles into larger cycles
    for (int i = 1; i <= n; ++i) {
        while (cnt[i] > 2) {
            cnt[i * 2]++;
            cnt[i] -= 2;
        }
    }
    
    bitset<N> dp; 
    dp.reset();
    dp[0] = 1; // Base case: 0 size can always be formed

    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < cnt[i]; ++j) {
            dp |= dp << i; // Shift and add combinations
        }
    }
    
    int q; 
    cin >> q;
    while (q--) {
        int a, b, c;
        cin >> a >> b >> c;
        int base = 2 * a; // Base score calculation
        
        if (a == b && a <= even_count) {
            cout << (dp[a] ? 4 * a : 4 * a - 1) << "\n";
            continue;
        }
        
        int cnt00 = 0, cnt1 = 0, cnt2 = 0;
        for (int size : cycle_size) {
            if (a <= 0) break;
            if (size % 2 == 0) {
                if (a >= size / 2) {
                    cnt2 += size / 2;
                    a -= size / 2;
                } else {
                    cnt1 += 2;
                    cnt2 += a - 1;
                    a = 0;
                }
            } else if (size > 1) {
                int mn = min(a, size / 2);
                cnt1 += 2;
                cnt2 += mn - 1;
                a -= mn;
            }
        }
        
        for (int size : cycle_size) {
            if (a <= 0) break;
            if (size % 2 == 1) {
                a--;
                cnt00++;
                if (size > 1) {
                    cnt1 -= 2;
                    cnt2++;
                }
            }
        }
        
        cnt00 += a * 2; // Add remaining a * 2 to cnt00
        cnt2 -= a; // Use up a for cnt2

        int ans = base - cnt00; // Calculate initial answer
        ans += min(b, cnt2) * 2; // Use cnt2 for b score
        b -= min(b, cnt2); // Reduce b
        ans += min(b, cnt1); // Add remaining cnt1
        cout << ans << "\n"; // Output answer for the query
    }
}
