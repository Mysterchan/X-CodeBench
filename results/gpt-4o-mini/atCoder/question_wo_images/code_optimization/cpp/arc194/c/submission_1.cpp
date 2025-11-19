#include<bits/stdc++.h>
using namespace std;
#define vi vector<int>
#define vll vector<long long>

void solve() {
    int n; 
    cin >> n;
    vi a(n), b(n);
    vll c(n);
    cin >> a >> b >> c;

    // Cost to change from A to B
    long long changeCost = 0;
    
    // Accumulators for costs of flips
    long long flip_0_to_1 = 0; // Cost to flip 0 to 1
    long long flip_1_to_0 = 0; // Cost to flip 1 to 0

    for (int i = 0; i < n; i++) {
        if (a[i] == 0 && b[i] == 1) {
            flip_0_to_1 += c[i];
        } else if (a[i] == 1 && b[i] == 0) {
            flip_1_to_0 += c[i];
        }
    }

    // The result is the total flip costs
    changeCost = flip_0_to_1 + flip_1_to_0;
    
    cout << changeCost << '\n';
}

signed main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(0);
    
    int t = 1;
    for(int i = 1; i <= t; i++) {   
        solve();
    }
    return 0;
}
