#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<vector<int>> G(N);
    
    for (int i = 0; i < N - 1; ++i) {
        int a, b;
        cin >> a >> b;
        a--; b--; // Convert to 0-indexed
        G[a].push_back(b);
        G[b].push_back(a);
    }

    vector<int> degrees(N);
    for (int i = 0; i < N; ++i) {
        degrees[i] = G[i].size();
    }

    // Check for the alkane properties
    int count_degree_4 = 0;
    for (int deg : degrees) {
        if (deg < 1 || deg > 4) {
            cout << -1 << endl;
            return 0;
        }
        if (deg == 4) {
            count_degree_4++;
        }
    }

    // If there are no vertices of degree 4, output -1
    if (count_degree_4 == 0) {
        cout << -1 << endl;
        return 0;
    }

    // Count the maximum number of vertices that can form an alkane
    int alkane_size = 0;
    for (int deg : degrees) {
        if (deg == 1) {
            alkane_size += 1; // Count leaves
        } else if (deg == 4) {
            alkane_size += 5; // Count degree 4 vertices and their leaves
        }
    }

    cout << alkane_size << endl;

    return 0;
}
