#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, m;
    cin >> n >> m;

    // The maximum number of black edges after operations is:
    // total edges = n*(n-1)/2
    // parity flips the count by m%2
    // So answer = total_edges - (m % 2)
    // No need to read edges since only parity of m matters.

    // Just read and discard edges to avoid runtime error
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
    }

    long long total_edges = n * (n - 1) / 2;
    cout << total_edges - (m % 2) << "\n";

    return 0;
}