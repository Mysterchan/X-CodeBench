#include<iostream>
#include<vector>
using namespace std;
using ll = long long;

int main() {
    int n;
    cin >> n;
    vector<ll> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    bool is_geometric = true;
    for (int i = 1; i < n - 1; i++) {
        if (a[0] * a[i + 1] != a[1] * a[i]) {
            is_geometric = false;
            break;
        }
    }
    
    if (is_geometric) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    
    return 0;
}