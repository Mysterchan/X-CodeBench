#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> p(n), c(n);
    for(int i = 0; i < n; i++) cin >> p[i];
    for(int i = 0; i < n; i++) cin >> c[i];

    // Group p[i] by color c[i]
    vector<vector<int>> v(n);
    for(int i = 0; i < n; i++) {
        v[c[i] - 1].push_back(p[i]);
    }

    ll ans = 0;
    // For each color, find length of LIS of p[i] in that color
    // Use O(k log k) LIS with vector and binary search
    for(int i = 0; i < n; i++) {
        vector<int>& arr = v[i];
        if(arr.empty()) continue;
        vector<int> lis;
        for(int x : arr) {
            auto it = lower_bound(lis.begin(), lis.end(), x);
            if(it == lis.end()) lis.push_back(x);
            else *it = x;
        }
        ans += (ll)(arr.size() - (int)lis.size()) * (i + 1);
    }

    cout << ans << '\n';
}