#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    vector<pair<int,int>> edges;
    edges.reserve(M);
    long long self_loops = 0;

    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        if (u == v) {
            self_loops++;
        } else {
            if (u > v) swap(u, v);
            edges.emplace_back(u, v);
        }
    }

    sort(edges.begin(), edges.end());
    long long duplicates = 0;
    for (size_t i = 1; i < edges.size(); i++) {
        if (edges[i] == edges[i - 1]) {
            duplicates++;
        }
    }

    cout << (self_loops + duplicates) << "\n";
    return 0;
}