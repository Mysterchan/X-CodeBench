#include <bits/stdc++.h>
using namespace std;
#define LZW0063 ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)

const int mod = 1e9 + 7;

void solve() {
    long long a, b, k; 
    cin >> a >> b >> k;

    long long n = ((a - 1) * k) % mod + 1;
    long long m = ((b - 1) * k) % mod + 1;

    // Output results
    cout << n << " " << m << "\n";
}

int main() {
    LZW0063;
    int TC;
    cin >> TC;
    while (TC--) solve();
    return 0;
}