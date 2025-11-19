#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        long long surplusZeros = 0, surplusOnes = 0;
        for (int i = 0; i < n; i++) {
            long long a, b, c, d;
            cin >> a >> b >> c >> d;
            surplusZeros += a - c;
            surplusOnes += b - d;
        }
        // The minimal number of operations is the total number of misplaced zeros (or ones),
        // which must be equal since total zeros and ones are conserved.
        // So answer = surplusZeros (which equals surplusOnes)
        cout << surplusZeros << "\n";
    }
    return 0;
}