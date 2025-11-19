#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, M;
    cin >> N >> M;

    vector<vector<int>> graph(N + 1);
    vector<int> degree(N + 1, 0);

    for (int i = 0; i < M; ++i) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
        degree[u]++;
        degree[v]++;
    }

    long long answer = 0;

    for (int start = 1; start <= N; ++start) {
        for (int end : graph[start]) {
            if (end <= start) continue; // Ensure unique edges (start, end) by keeping start < end
            long long cycle_count = 1; // To count the cycles through (start, end)
            // Count pairs of edges connecting to other vertices that can form cycles
            for (int next_start : graph[start]) {
                if (next_start == end) continue;
                cycle_count = (cycle_count * (degree[next_start] - 1)) % MOD; // Each next_start can form a cycle with (start, end)
            }
            answer = (answer + cycle_count) % MOD;
        }
    }

    cout << answer << endl;
}