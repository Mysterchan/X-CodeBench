#include <bits/stdc++.h>
using namespace std;

const int mod = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N; cin >> N;
    string s; cin >> s;

    // Count number of ones in s
    int k = 0;
    for (char c : s) if (c == '1') k++;

    // Number of edges = N (cycle edges) + k (edges to vertex N)
    // Each edge can be oriented in 2 ways independently
    // So total orientations = 2^(N + k)
    // The problem asks for the number of distinct in-degree sequences modulo 998244353

    // The key insight:
    // The in-degree sequences correspond to all possible sums of orientations.
    // The cycle edges form a cycle of length N, each vertex has degree 2 from cycle edges.
    // The edges to vertex N add degrees to vertex N and the connected vertices.
    //
    // The number of distinct in-degree sequences is 2^(N + k) modulo mod.

    // Compute 2^(N + k) mod
    int64_t exp = (int64_t)N + k;
    int64_t res = 1;
    int64_t base = 2;
    while (exp > 0) {
        if (exp & 1) res = (res * base) % mod;
        base = (base * base) % mod;
        exp >>= 1;
    }

    cout << res << "\n";
    return 0;
}