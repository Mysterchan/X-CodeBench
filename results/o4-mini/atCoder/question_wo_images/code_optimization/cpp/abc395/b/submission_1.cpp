#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            int layer = min(min(i, j), min(N - 1 - i, N - 1 - j));
            char c = (layer % 2 == 0 ? '#' : '.');
            cout << c;
        }
        cout << '\n';
    }
    return 0;
}