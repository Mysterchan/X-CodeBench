#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <bitset>
#include <unordered_map>
#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
using namespace std;

typedef double db;
typedef long long ll;
typedef unsigned long long ull;

const int N    = 110;
const int LOGN = 10;
const ll  TMD  = 998244353;
const ll  INF  = 2147483647;

int T, n;
ll s[N], fac[N], inv[N];
ll dp[N][N][LOGN][LOGN];


ll pw(ll a, ll b) {
    ll r = 1;
    a %= TMD;
    while (b > 0) {
        if (b & 1) r = (r * a) % TMD;
        a = (a * a) % TMD;
        b >>= 1;
    }
    return r;
}


ll C(int n_, int m_) {
    if (n_ < m_ || n_ < 0 || m_ < 0) return 0;
    return fac[n_] * inv[m_] % TMD * inv[n_ - m_] % TMD;
}


void init_C() {
    fac[0] = 1;
    for (int i = 1; i < N; i++) {
        fac[i] = fac[i - 1] * i % TMD;
    }
    inv[N - 1] = pw(fac[N - 1], TMD - 2);
    for (int i = N - 2; i >= 0; i--) {
        inv[i] = inv[i + 1] * (i + 1) % TMD;
    }
}


void init() {
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> s[i];
    }
    for (int i = 1; i <= n+4; i++)
        for (int j = 1; j <= n+4; j++)
            for (int ii = 0; ii < LOGN; ii++)
                for (int jj = 0; jj < LOGN; jj++)
                    dp[i][j][ii][jj] = 0;

    dp[1][1][0][1] = (s[1] < 1);
    for (int i = 2; i <= n; i++) {
        dp[i][i][1][0] = (s[i] < 1);
    }
    for (int i = 1; i <= n; i++) {   // auxiliary
        dp[i][i - 1][0][0] = dp[i + 1][i][0][0] = 1;
    }
}

inline int ABS(int x) {
    return x < 0 ? -x : x;
}


void solve() {
    for (int len = 2; len <= n; len++) {
        for (int l = 1; l + len - 1 <= n; l++) {
            int r = l + len - 1;
            for (int ii = 0; ii < LOGN; ii++) {
                for (int jj = 0; jj < LOGN; jj++) {
                    ll &cur = dp[l][r][ii][jj];
                    for (int k = l; k <= r; k++) {
                        int tagl = 0, tagr = 0;
                        if (l == 1 && r == n) {
                        } else if (l == 1) {
                            tagr = 1;
                        } else if (r == n) {
                            tagl = 1;
                        } else {
                            if (ABS(l - 1 - k) <= ABS(k - (r + 1))) tagl = 1;
                            else                                   tagr = 1;
                        }
                        if (ii - tagl < 0 || jj - tagr < 0) continue;

                        if (s[k] == -1) {
                            ll suml = 0, sumr = 0;
                            for (int kk = 0; kk < LOGN; kk++)
                                suml = (suml + dp[l][k - 1][ii - tagl][kk]) % TMD;
                            for (int kk = 0; kk < LOGN; kk++)
                                sumr = (sumr + dp[k + 1][r][kk][jj - tagr]) % TMD;
                            cur = (cur + suml * sumr % TMD * C(r - l, k - l)) % TMD;
                        } else {
                            for (int kk = 0; kk < LOGN; kk++) {
                                int need = s[k] - kk;
                                if (need < 0 || need >= LOGN) continue;
                                cur = (cur
                                       + dp[l][k - 1][ii - tagl][kk]
                                       * dp[k + 1][r][need][jj - tagr] % TMD
                                       * C(r - l, k - l)
                                      ) % TMD;
                            }
                        }
                    }
                }
            }
        }
    }
    cout << dp[1][n][0][0] << '\n';
}

int main() {
    fastio;
    init_C();
    cin >> T;
    while (T--) {
        init();
        solve();
    }
    return 0;
}
