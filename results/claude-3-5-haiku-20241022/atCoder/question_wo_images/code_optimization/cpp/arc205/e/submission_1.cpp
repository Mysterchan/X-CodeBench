#include <bits/stdc++.h>
using namespace std;

const int mod = 998244353;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    vector<int> a(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
    }
    
    vector<long long> s(1 << 20, 1);
    
    for (int i = 1; i <= n; i++) {
        s[a[i]] = s[a[i]] * a[i] % mod;
        
        for (int j = 0; j < 20; j++) {
            if (a[i] >> j & 1) {
                s[a[i]] = s[a[i]] * s[a[i] ^ (1 << j)] % mod;
            }
        }
        
        cout << s[a[i]] << '\n';
    }
    
    return 0;
}