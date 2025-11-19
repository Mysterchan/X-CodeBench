#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, X;
    cin >> N >> X;
    vector<vector<pair<int, int>>> G(N + 2, vector<pair<int, int>>());
    long long S = 0;
    for (int i = 0; i < N; ++i) {
        int U, D;
        cin >> U >> D;
        S += U + D;
        G[i].push_back({N + 1, U});
        G[N + 1].push_back({i, 0});
        G[N].push_back({i, D});
        G[i].push_back({N, 0});
    }
    for (int i = 0; i < N - 1; ++i) {
        G[i].push_back({i + 1, X});
        G[i + 1].push_back({i, X});
    }
    vector<long long> v(N + 2, -1);
    priority_queue<pair<long long, int>> pq;
    pq.push({0, N});
    while (!pq.empty()) {
        pair<long long, int> T = pq.top();
        pq.pop();
        if (v[T.second] != -1 && v[T.second] <= T.first) continue;
        v[T.second] = T.first;
        for (int i = 0; i < G[T.second].size(); ++i) {
            pq.push({G[T.second][i].second + T.first, G[T.second][i].first});
        }
    }
    cout << S - N * v[N + 1] << endl;
}