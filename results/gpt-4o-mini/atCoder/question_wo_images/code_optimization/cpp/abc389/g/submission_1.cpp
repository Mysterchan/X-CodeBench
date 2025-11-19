#include <bits/stdc++.h>
using namespace std;

const int N = 35;
long long mod, C[N * N][N * N], S[N][N][N * N];
int f[N][N * N / 2][2][N + N][N];

inline void add(int &x, int y) {
    (x += y) >= mod ? x -= mod : 0;
}

void precompute(int n) {
    for (int i = 0; i <= n * N; i++) {
        C[i][0] = 1;
        for (int j = 1; j <= i; j++) {
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % mod;
        }
    }

    for (int m = 1; m <= n; m++) {
        for (int d = 1; d <= n - m; d++) {
            if (d == 1) {
                for (int e = d; e <= n * (n - 1) / 2; e++) {
                    S[m][d][e] = C[m][e];
                }
            } else {
                for (int e = d; e <= n * (n - 1) / 2; e++) {
                    for (int t = 1; t <= e; t++) {
                        add(S[m][d][e], S[m][d - 1][e - t] * (C[d - 1 + m][t] - C[d - 1][t]) % mod);
                    }
                }
            }
        }
    }
}

int main() {
    int n;
    cin >> n >> mod;

    precompute(n);

    int M = n * (n - 1) / 2;
    f[1][0][0][1 + n][1] = 1;

    for (int i = 1; i < n; i++) {
        for (int j = 0; j <= M; j++) {
            for (int k = 0; k < 2; k++) {
                for (int l = 1; l < 2 * n; l++) {
                    if (f[i][j][k][l][1]) {
                        for (int d = 1; d <= n - i; d++) {
                            for (int e = d; e <= M - j; e++) {
                                add(f[i + d][j + e][k ^ 1][l + ((k & 1) ? 1 : -1) * d][d], 
                                   f[i][j][k][l][1] * C[n - i][d] % mod * S[1][d][e] % mod);
                            }
                        }
                    }
                }
            }
        }
    }

    for (int m = n - 1; m <= n * (n - 1) / 2; m++) {
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            add(ans, f[n][m][0][n][i]);
            add(ans, f[n][m][1][n][i]);
        }
        cout << ans << " ";
    }
    cout << endl;

    return 0;
}