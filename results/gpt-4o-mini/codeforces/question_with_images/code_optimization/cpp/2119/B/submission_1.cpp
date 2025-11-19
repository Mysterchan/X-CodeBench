#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n; 
    cin >> n;
    long long px, py, qx, qy; 
    cin >> px >> py >> qx >> qy;
    
    vector<int> arr(n);
    long long total_distance = 0;
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
        total_distance += arr[i];
    }

    long long dx = abs(px - qx);
    long long dy = abs(py - qy);
    long long required_distance = dx + dy;

    if (required_distance <= total_distance && (total_distance - required_distance) % 2 == 0) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t; 
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}