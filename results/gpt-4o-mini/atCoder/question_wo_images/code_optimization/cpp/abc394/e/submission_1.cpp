#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<string> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];

    const int inf = 1e9;
    vector<vector<int>> G(N, vector<int>(N, inf));

    // Initialize distances based on direct edges
    for (int i = 0; i < N; i++) {
        G[i][i] = 0;
        for (int j = 0; j < N; j++) {
            if (A[i][j] != '-') {
                G[i][j] = 1;
            }
        }
    }

    // Floyd-Warshall variant for palindrome paths
    for (int k = 0; k < N; k++) {
        for (int i = 0; i < N; i++) {
            if (A[i][k] == '-') continue; // No path from i to k
            for (int j = 0; j < N; j++) {
                if (A[k][j] != '-' && A[i][k] == A[j][j]) { // Path from i to k to j forms potential palindrome
                    G[i][j] = min(G[i][j], G[i][k] + G[k][j]);
                }
            }
        }
    }

    // Output the results
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << (G[i][j] >= inf ? -1 : G[i][j]) << ' ';
        }
        cout << endl;
    }
    return 0;
}
