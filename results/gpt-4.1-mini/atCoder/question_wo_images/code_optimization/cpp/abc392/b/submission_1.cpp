#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    vector<bool> present(N + 1, false);

    for (int i = 0; i < M; i++) {
        int x; cin >> x;
        present[x] = true;
    }

    vector<int> missing;
    for (int i = 1; i <= N; i++) {
        if (!present[i]) missing.push_back(i);
    }

    cout << (int)missing.size() << "\n";
    if (!missing.empty()) {
        for (int x : missing) cout << x << " ";
    }
    cout << "\n";

    return 0;
}