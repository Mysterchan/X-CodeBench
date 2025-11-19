#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int t;
    cin >> t;
    while (t--) {
        long long s, k;
        cin >> s >> k;

        // Find the maximum power Gleb can maintain while reaching s
        long long max_power = k;
        
        // If k can be adjusted down to find the largest value that fits in [0, s]
        // Gleb can be at position s if (s - k) is divisible by k 
        // hence maximum will match what remains within bounds
        for (long long i = 0; i <= k; ++i) {
            if ((s - i) >= 0 && (s - i) % k == 0) {
                max_power = min(max_power, i);
            }
        }

        cout << max_power << "\n";
    }
    return 0;
}