#include <bits/stdc++.h>
using namespace std;
const int mod = 998244353;
const int maxN = 200100;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for(int i = 0; i < n; i++) {
            cin >> a[i];
        }
        
        long long total = 0;
        // This will hold the current sum for f(a_l...a_r)
        long long current = 0;
        
        for(int i = 0; i < n; i++) {
            long long aSum = 0, bSum = 0;

            // For each starting index `i`, we calculate f(a_l...a_r)
            for(int j = i; j < n; j++) {
                if(j % 2 == 1) {
                    aSum += a[j]; // odd index
                    bSum = max(bSum - a[j], 0LL);
                } else {
                    bSum += a[j]; // even index
                    aSum = max(aSum - a[j], 0LL);
                }

                current = (aSum + bSum) % mod;
                total = (total + current) % mod;
            }
        }
        
        cout << total << endl;
    }
    return 0;
}