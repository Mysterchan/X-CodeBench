#include <iostream>
#include <vector>
#include <string>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N; cin >> N;
    vector<string> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];

    const int INF = 1 << 20;
    // dist[i][j] = shortest palindrome path length from i to j
    vector<vector<int>> dist(N, vector<int>(N, INF));

    // Queue for BFS on pairs (i,j)
    queue<pair<int,int>> q;

    // Initialize dist[i][i] = 0 (empty path is palindrome)
    for (int i = 0; i < N; i++) {
        dist[i][i] = 0;
        q.emplace(i, i);
    }

    // For edges i->j with label c, dist[i][j] = 1 (single edge palindrome)
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (A[i][j] != '-') {
                dist[i][j] = 1;
                q.emplace(i, j);
            }
        }
    }

    // BFS on pairs (i,j)
    // dist[i][j] = minimal length of palindrome path from i to j
    while (!q.empty()) {
        auto [i, j] = q.front(); q.pop();
        int cur_dist = dist[i][j];

        // Try to extend palindrome by adding matching edges at front and back
        // For all edges k->i and j->l with same label
        for (int k = 0; k < N; k++) {
            if (A[k][i] == '-') continue;
            char c = A[k][i];
            for (int l = 0; l < N; l++) {
                if (A[j][l] == c) {
                    int nd = cur_dist + 2;
                    if (dist[k][l] > nd) {
                        dist[k][l] = nd;
                        q.emplace(k, l);
                    }
                }
            }
        }
    }

    // Output results
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (dist[i][j] == INF) cout << -1;
            else cout << dist[i][j];
            cout << (j == N - 1 ? '\n' : ' ');
        }
    }

    return 0;
}