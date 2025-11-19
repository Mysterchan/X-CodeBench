#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> p(n), c(n);
        for (int &x : p) cin >> x;
        for (int &x : c) cin >> x;

        // This will be the frequency map for colors
        unordered_map<int, int> color_count;
        for (int i = 0; i < n; ++i) {
            color_count[c[i]]++;
        }

        // Count the number of blocks falling on each height
        vector<int> height_count(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            height_count[p[i]]++;
        }

        // Calculate the total arrangements
        ll result = 1;
        for (int i = 1; i <= n; ++i) {
            if (height_count[i] > 0) {
                // For each color count, we can arrange them in `factorial[color_count[color]] / factorial[count for that height]`
                ll arrangements = 1;
                for (auto &[color, count] : color_count) {
                    arrangements = (arrangements * 1LL * count) % MOD;
                }
                // Using the factorial of the color counts according to the blocks on that height
                result = (result * arrangements) % MOD;
            }
        }
        
        // Finally output the result
        cout << result << '\n';
    }

    return 0;
}