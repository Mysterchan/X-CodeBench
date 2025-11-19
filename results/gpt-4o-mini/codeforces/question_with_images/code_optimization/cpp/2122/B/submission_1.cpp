#include<iostream>
#include<vector>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        ll excessZeros = 0, excessOnes = 0;

        for (int i = 0; i < n; i++) {
            ll zeros, ones, reqZ, reqO;
            cin >> zeros >> ones >> reqZ >> reqO;

            excessZeros += max(0LL, zeros - reqZ);
            excessOnes += max(0LL, ones - reqO);
        }

        // The number of moves required is the maximum of excess zeros and excess ones
        cout << max(excessZeros, excessOnes) << endl;
    }

    return 0;
}