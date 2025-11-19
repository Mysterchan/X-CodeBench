#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        // The total number of matches in a double-elimination tournament with n teams is always 2*n - 1
        cout << 2 * n - 1 << "\n";
    }
    return 0;
}