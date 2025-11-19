# include <iostream>
# include <vector>

using std::cin;
using std::cout;
using std::vector;

constexpr int mod = 998244353;

vector<vector<bool>> g;
vector<vector<int>> f0, f1;

int dp1(int s, int t);

int dp0(int s, int t) {
    if (t < s) {
        return 1;
    }


    int res = 0;

    for (int i = s; i <= t; ++i) {
        res += int((1ll * dp1(s, i) * dp0(i + 1, t)) % mod);
        res %= mod;
    }

    return res;
}

int dp1(int s, int t) {
    if (t < s) {
        return 1;
    }

    if (!g[s][t]) {
        return 0;
    }

    int res = 0;

    for (int root = s; root <= t; ++root) {
        res += int((1ll * dp0(s, root - 1) * dp0(root + 1, t)) % mod);
        res %= mod;
    }

    return res;
}

int main() {
    std::ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    g.resize(n, vector<bool>(n, true));
    f0.resize(n, vector<int>(n, 0));
    f1.resize(n, vector<int>(n, 0));

    vector<vector<int>> sequences(m, vector<int>(n));

    for (auto &a: sequences[0]) {
        cin >> a;
        a -= 1;
    }

    for (int i = 1; i < m; ++i) {
        auto &sequence = sequences[i];

        for (int j = 0; j < n; ++j) {
            cin >> sequence[sequences[0][j]];
            sequence[sequences[0][j]] -= 1;
        }

        for (int j = n - 1; j >= 0; --j) {
            sequence[j] = (sequence[j] - sequence[0] + n) % n;
        }
    }

    for (int i = 1; i < m; ++i) {
        const auto &sequence = sequences[i];

        for (int l = 0; l < n; ++l) {
            int mn = n, mx = -1;

            for (int r = l; r < n; ++r) {
                mn = std::min(mn, sequence[r]);
                mx = std::max(mx, sequence[r]);

                g[l][r] = g[l][r] & (mx - mn == r - l);
            }
        }
    }

    cout << dp0(1, n - 1);

    return 0;
}
