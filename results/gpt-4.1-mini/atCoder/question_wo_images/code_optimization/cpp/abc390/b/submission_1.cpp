#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    // For N=2, always Yes
    if (n == 2) {
        cout << "Yes\n";
        return 0;
    }

    // Check ratio using cross multiplication to avoid floating point errors
    // ratio = a[1]/a[0], check a[i]*a[0] == a[i-1]*a[1] for all i>=2
    for (int i = 2; i < n; i++) {
        if (a[i] * a[0] != a[i - 1] * a[1]) {
            cout << "No\n";
            return 0;
        }
    }
    cout << "Yes\n";
    return 0;
}