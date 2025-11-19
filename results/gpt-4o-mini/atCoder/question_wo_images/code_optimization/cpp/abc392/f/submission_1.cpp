#include<bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        int pos;
        cin >> pos;
        // Insert in reverse to maintain the correct order
        a.insert(a.begin() + pos - 1, i + 1);
    }
    for (int i = 0; i < n; i++) {
        cout << a[i] << ' ';
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    solve();
    return 0;
}