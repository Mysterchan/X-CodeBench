#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<int> a(5);
    for (int i = 0; i < 5; i++) {
        cin >> a[i];
    }

    int inv = 0;
    for (int i = 0; i < 5; i++) {
        for (int j = i + 1; j < 5; j++) {
            if (a[i] > a[j]) inv++;
        }
    }

    cout << (inv == 1 ? "Yes" : "No");
    return 0;
}