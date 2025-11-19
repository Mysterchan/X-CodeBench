#include<iostream>
#include<vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<long long> a(n); // Use long long to prevent overflow
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    if (n == 2) { // Any two numbers form a geometric progression
        cout << "Yes" << endl;
        return 0;
    }

    long long r = a[1] * 1LL; // common ratio
    for (int i = 2; i < n; i++) {
        if (a[i-1] == 0 || a[i] * a[1] != a[i-1] * a[0]) { // Check for geometric progression condition
            cout << "No" << endl;
            return 0;
        }
    }
    
    cout << "Yes" << endl;
    return 0;
}