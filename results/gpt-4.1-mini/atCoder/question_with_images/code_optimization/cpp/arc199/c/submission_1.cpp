#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::vector;

constexpr int mod = 998244353;

int n, m;
vector<vector<bool>> g;
vector<vector<int>> f0, f1;

int dp0(int s, int t);
int dp1(int s, int t);

int dp0(int s, int t) {
    if (t < s) return 1;
    int &res = f0[s][t];
    if (res != -1) return res;
    res = 0;
    for (int i = s; i <= t; ++i) {
        int val = (int)((1LL * dp1(s, i) * dp0(i + 1, t)) % mod);
        res += val;
        if (res >= mod) res -= mod;
    }
    return res;
}

int dp1(int s, int t) {
    if (t < s) return 1;
    int &res = f1[s][t];
    if (res != -1) return res;
    if (!g[s][t]) return res = 0;
    res = 0;
    for (int root = s; root <= t; ++root) {
        int val = (int)((1LL * dp0(s, root - 1) * dp0(root + 1, t)) % mod);
        res += val;
        if (res >= mod) res -= mod;
    }
    return res;
}

int main() {
    std::ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;

    g.assign(n, vector<bool>(n, true));
    f0.assign(n, vector<int>(n, -1));
    f1.assign(n, vector<int>(n, -1));

    vector<vector<int>> sequences(m, vector<int>(n));

    // Read first permutation and convert to zero-based
    for (int j = 0; j < n; ++j) {
        cin >> sequences[0][j];
        --sequences[0][j];
    }

    // Read other permutations in a way that aligns with sequences[0]
    for (int i = 1; i < m; ++i) {
        auto &seq = sequences[i];
        for (int j = 0; j < n; ++j) {
            cin >> seq[sequences[0][j]];
            --seq[sequences[0][j]];
        }
        // Normalize so that seq[0] becomes 0 modulo n
        int base = seq[0];
        for (int j = 0; j < n; ++j) {
            seq[j] = (seq[j] - base + n) % n;
        }
    }

    // Build g matrix: g[l][r] = true if for all permutations,
    // the segment [l,r] forms a contiguous interval in the circle
    for (int i = 1; i < m; ++i) {
        const auto &seq = sequences[i];
        for (int l = 0; l < n; ++l) {
            int mn = n, mx = -1;
            for (int r = l; r < n; ++r) {
                int val = seq[r];
                if (val < mn) mn = val;
                if (val > mx) mx = val;
                // If interval length matches max-min, it's contiguous
                g[l][r] = g[l][r] && (mx - mn == r - l);
            }
        }
    }

    // Compute and output the result
    cout << dp0(1, n - 1) << "\n";

    return 0;
}