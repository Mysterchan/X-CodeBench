#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    int prev, curr;
    cin >> prev;
    for (int i = 1; i < N; ++i) {
        cin >> curr;
        if (prev >= curr) {
            cout << "No\n";
            return 0;
        }
        prev = curr;
    }
    cout << "Yes\n";
    return 0;
}