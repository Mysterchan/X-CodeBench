#include <bits/stdc++.h>
using namespace std;

const int MAXN = 500 * 10; // Maximum value of NK = N * K where N <= 500 and K <= 10

int main() {
    cin.tie(0)->sync_with_stdio(0);

    int N, K;
    cin >> N >> K;

    vector<int> P(N * K);
    for (int &x : P) {
        cin >> x;
        x--; // Convert to 0-based index
    }

    vector<int> pos(N * K);
    for (int i = 0; i < N * K; i++) {
        pos[P[i]] = i; // Storing the positions of elements in P
    }

    int ans = 0;
    vector<bool> visited(N * K, false); // Track visited elements

    for (int i = 0; i < N * K; i++) {
        if (visited[i]) continue; // If already visited, skip

        vector<int> cycle;
        int x = i;
        while (!visited[x]) {
            visited[x] = true;
            cycle.push_back(x);
            x = pos[x]; // Moving to the next index in the cycle
        }

        int cycle_size = cycle.size();
        vector<int> cycle_pos(N); // Position indices grouped by modulo N
        for (int j : cycle) {
            cycle_pos[j % N]++;
        }

        // The maximum number of points gained from sorting this cycle
        int cycle_points = 0;
        for (int count : cycle_pos) {
            cycle_points += (count > 1) ? count - 1 : 0;
        }
        ans += cycle_points;
    }

    cout << ans << '\n';
}
