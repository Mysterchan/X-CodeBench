#include <iostream>
#include <vector>
#include <numeric>
#include <unordered_map>

using namespace std;

const int MOD = 998244353;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;
        vector<vector<int>> A(N, vector<int>(N));
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j)
                cin >> A[i][j];

        bool valid = true;

        // Check the matrix properties in one pass
        for (int i = 0; i < N; ++i) {
            if (A[i][i] == 0) { valid = false; break; }
            for (int j = i + 1; j < N; ++j) {
                if (A[i][j] != A[j][i]) { valid = false; break; }
            }
            if (!valid) break;
        }

        // Check connections from root (vertex 1)
        if (valid) {
            for (int j = 0; j < N; ++j) {
                if (A[0][j] == 0) { valid = false; break; }
            }
        }

        if (!valid) {
            cout << 0 << '\n';
            continue;
        }

        // Using a unique way to find components and possible tree counts
        vector<int> component(N, -1); // -1 means unvisited
        vector<int> size_comp(N, 0);
        vector<vector<int>> adj(N);

        for (int i = 0; i < N; ++i) {
            for (int j = i + 1; j < N; ++j) {
                if (A[i][j] == 1) {
                    adj[i].push_back(j);
                    adj[j].push_back(i);
                }
            }
        }

        long long num_trees = 1;
        vector<int> stack;
        for (int i = 0; i < N; ++i) {
            if (component[i] != -1) continue; // already visited
            int component_size = 0;
            stack.push_back(i);
            component[i] = i;
            while (!stack.empty()) {
                int u = stack.back(); stack.pop_back();
                component_size++;
                for (int v : adj[u]) {
                    if (component[v] == -1) {
                        component[v] = i; // this component
                        stack.push_back(v);
                    }
                }
            }
            // Calculate the number of ways to root trees in the component
            num_trees = num_trees * power(component_size, component_size - 2) % MOD;
        }

        cout << num_trees << '\n';
    }
    return 0;
}