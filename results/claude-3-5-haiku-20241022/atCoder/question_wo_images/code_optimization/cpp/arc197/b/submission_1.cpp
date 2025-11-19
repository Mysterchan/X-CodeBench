#pragma GCC optimize("O3")
#include <bits/stdc++.h>
#pragma GCC target("avx,avx2,sse,sse4,popcnt")
using namespace std;

using ll = long long;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int T;
    cin >> T;
    
    while(T--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for(auto &x : a) cin >> x;
        
        sort(a.begin(), a.end());
        
        int maxScore = 0;
        
        // Precompute prefix sums
        vector<ll> prefix(n + 1, 0);
        for(int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + a[i];
        }
        
        // Try all possible subsequences defined by range [i, j)
        for(int i = 0; i < n; i++) {
            for(int j = i + 1; j <= n; j++) {
                ll sum = prefix[j] - prefix[i];
                int len = j - i;
                
                // Binary search for the largest k such that a[i+k-1] * len <= sum
                // This gives us how many elements from the left are <= average
                int left = 0, right = len;
                while(left < right) {
                    int mid = (left + right + 1) / 2;
                    if((ll)a[i + mid - 1] * len <= sum) {
                        left = mid;
                    } else {
                        right = mid - 1;
                    }
                }
                
                int score = len - left;
                maxScore = max(maxScore, score);
            }
        }
        
        cout << maxScore - 1 << "\n";
    }
    
    return 0;
}