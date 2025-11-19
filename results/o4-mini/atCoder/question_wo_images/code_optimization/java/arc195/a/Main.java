#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    if (!(cin >> N >> M)) return 0;
    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    unordered_map<int, vector<int>> pos;
    pos.reserve(N * 2);
    for (int i = 0; i < N; i++) {
        pos[A[i]].push_back(i);
    }

    vector<vector<int>*> lists(M);
    for (int i = 0; i < M; i++) {
        int b;
        cin >> b;
        auto it = pos.find(b);
        if (it == pos.end()) {
            cout << "No\n";
            return 0;
        }
        lists[i] = &it->second;
    }

    // Compute lexicographically smallest match
    vector<int> L(M), R(M);
    int prev = -1;
    for (int i = 0; i < M; i++) {
        auto &v = *lists[i];
        auto it = std::upper_bound(v.begin(), v.end(), prev);
        if (it == v.end()) {
            cout << "No\n";
            return 0;
        }
        L[i] = *it;
        prev = L[i];
    }

    // Compute lexicographically largest match
    int next = N;
    for (int i = M - 1; i >= 0; i--) {
        auto &v = *lists[i];
        auto it = std::lower_bound(v.begin(), v.end(), next);
        if (it == v.begin()) {
            cout << "No\n";
            return 0;
        }
        --it;
        R[i] = *it;
        next = R[i];
    }

    // Check if there's any position where we can choose differently
    for (int i = 0; i < M; i++) {
        if (L[i] != R[i]) {
            cout << "Yes\n";
            return 0;
        }
    }
    cout << "No\n";
    return 0;
}