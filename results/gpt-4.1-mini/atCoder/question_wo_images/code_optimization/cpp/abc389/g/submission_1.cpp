#include <bits/stdc++.h>
using namespace std;

constexpr int MAXN = 30;
int n, mod;
int M;
int C[MAXN * (MAXN - 1) / 2 + 1][MAXN * (MAXN - 1) / 2 + 1];
int S[MAXN + 1][MAXN + 1][MAXN * (MAXN - 1) / 2 + 1];
int f[MAXN + 1][MAXN * (MAXN - 1) / 2 + 1][2][2 * MAXN + 1][MAXN + 1];

inline void add(int &x, int y) {
    x += y;
    if (x >= mod) x -= mod;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> mod;
    M = n * (n - 1) / 2;

    // Precompute binomial coefficients modulo mod
    for (int i = 0; i <= M; i++) {
        C[i][0] = 1;
        for (int j = 1; j <= i; j++) {
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
            if (C[i][j] >= mod) C[i][j] -= mod;
        }
    }

    // Precompute S[m][d][e]
    // S[m][d][e] = number of ways to add e edges connecting d new vertices to m old vertices,
    // such that the new vertices form an independent set (no edges among them)
    // The formula:
    // For d=1: S[m][1][e] = C[m][e]
    // For d>1: S[m][d][e] = sum_{t=1}^e S[m][d-1][e-t] * (C[m + d -1][t] - C[d -1][t]) mod
    // We optimize by prefix sums to avoid O(e^2) complexity.

    for (int m = 1; m <= n; m++) {
        for (int d = 1; d <= n - m; d++) {
            if (d == 1) {
                for (int e = 0; e <= M; e++) {
                    if (e <= m) S[m][d][e] = C[m][e];
                    else S[m][d][e] = 0;
                }
            } else {
                // Precompute prefix sums for S[m][d-1][*]
                static int prefix[MAXN * (MAXN - 1) / 2 + 1];
                prefix[0] = S[m][d - 1][0];
                for (int e = 1; e <= M; e++) {
                    prefix[e] = prefix[e - 1] + S[m][d - 1][e];
                    if (prefix[e] >= mod) prefix[e] -= mod;
                }

                for (int e = 0; e <= M; e++) {
                    // sum over t=1 to e of S[m][d-1][e-t] * (C[m + d -1][t] - C[d -1][t])
                    // = sum over t=1 to e of S[m][d-1][e-t] * val_t
                    // We reverse index: let s = e - t, t = e - s
                    // sum_{s=0}^{e-1} S[m][d-1][s] * val_{e - s}
                    // So we can precompute val array and do convolution-like sum

                    // Precompute val array for t=1..e
                    // val_t = (C[m + d -1][t] - C[d -1][t] + mod) % mod
                    // We'll compute on the fly to save memory

                    int res = 0;
                    // To optimize, we can precompute val array for max t = e
                    // But since e can be up to M ~ 435, we do direct loop here.

                    // To optimize further, we can precompute val array once per (m,d)
                    // Let's do that.

                    static int val[MAXN * (MAXN - 1) / 2 + 1];
                    for (int t = 1; t <= e; t++) {
                        int tmp = C[m + d - 1][t] - C[d - 1][t];
                        if (tmp < 0) tmp += mod;
                        val[t] = tmp;
                    }

                    for (int s = 0; s < e; s++) {
                        int t = e - s;
                        int mul = (int)((long long)S[m][d - 1][s] * val[t] % mod);
                        res += mul;
                        if (res >= mod) res -= mod;
                    }
                    S[m][d][e] = res;
                }
            }
        }
    }

    // DP initialization
    // f[i][j][k][l][m]:
    // i = number of vertices included so far
    // j = number of edges used so far
    // k = parity of distance layer (0 or 1)
    // l = difference between count of even and odd distance vertices + n (to keep index positive)
    // m = number of vertices in the last added layer

    // Initialize f with 0
    memset(f, 0, sizeof(f));
    // Start with vertex 1 at distance 0 (even), difference = n (since difference = even - odd)
    // So difference = 1 (even) - 0 (odd) = 1, stored as l = n + 1
    f[1][0][0][n + 1][1] = 1;

    // Iterate over layers
    for (int i = 1; i < n; i++) {
        for (int j = 0; j <= M; j++) {
            for (int k = 0; k < 2; k++) {
                for (int l = 1; l <= 2 * n; l++) {
                    for (int m_ = 1; m_ <= i; m_++) {
                        int cur = f[i][j][k][l][m_];
                        if (!cur) continue;

                        int rem = n - i;
                        // For each possible size d of next layer
                        for (int d = 1; d <= rem; d++) {
                            int maxE = M - j;
                            // For each possible number of edges e connecting new layer to previous layers
                            // e >= d (at least one edge per new vertex to keep connectivity)
                            // but S[m_][d][e] is defined for e >= 0, so we start from e = d
                            // but in original code e starts from d, so we do the same
                            for (int e = d; e <= maxE; e++) {
                                int ways = (int)((long long)cur * C[rem][d] % mod);
                                ways = (int)((long long)ways * S[m_][d][e] % mod);
                                if (ways == 0) continue;

                                int new_i = i + d;
                                int new_j = j + e;
                                int new_k = k ^ 1;
                                int new_l = l + ((k & 1) ? 1 : -1) * d;
                                if (new_l < 1 || new_l > 2 * n) continue;
                                add(f[new_i][new_j][new_k][new_l][d], ways);
                            }
                        }
                    }
                }
            }
        }
    }

    // Output answers for M = n-1 to n(n-1)/2
    // Sum over k=0,1 and m=1..n of f[n][M][k][n][m]
    // difference = 0 means l = n (since l = difference + n)
    for (int edges = n - 1; edges <= M; edges++) {
        int ans = 0;
        for (int k = 0; k < 2; k++) {
            for (int m_ = 1; m_ <= n; m_++) {
                add(ans, f[n][edges][k][n][m_]);
            }
        }
        cout << ans << " ";
    }
    cout << "\n";

    return 0;
}