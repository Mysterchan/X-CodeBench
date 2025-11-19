#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    vector<bool> present(N + 1, false);
    for (int i = 0; i < M; i++) {
        int x;
        cin >> x;
        present[x] = true;
    }

    vector<int> missing;
    missing.reserve(N - M);
    for (int i = 1; i <= N; i++) {
        if (!present[i]) {
            missing.push_back(i);
        }
    }

    cout << missing.size() << "\n";
    if (!missing.empty()) {
        for (int i = 0; i < (int)missing.size(); i++) {
            if (i) cout << " ";
            cout << missing[i];
        }
        cout << "\n";
    }
    return 0;
}