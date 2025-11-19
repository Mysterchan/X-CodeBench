#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    
    int n;
    cin >> n;
    
    vector<int> p(n), c(n);
    for (int i = 0; i < n; ++i) cin >> p[i];
    for (int i = 0; i < n; ++i) cin >> c[i];
    
    vector<int> colorSizeMappings(n + 1);
    for (int i = 0; i < n; ++i) {
        colorSizeMappings[c[i]] = max(colorSizeMappings[c[i]], p[i]);
    }

    ll ans = 0;
    vector<int> updateCosts(n + 1, 0);
    
    for (int i = 1; i <= n; ++i) {
        if (colorSizeMappings[i] > 0) {
            for (int j = colorSizeMappings[i]; j > 0; j--) {
                updateCosts[j] = min(updateCosts[j], (ll)c[i - 1]); // use previous color cost for update
            }
        }
    }
    
    for (int j = 1; j <= n; ++j) {
        if (updateCosts[j] == 0) continue; // No valid updates
        ans += updateCosts[j] * (j); // Total cost addition for each color
    }
    
    cout << ans << '\n';
}
