#include <iostream>

#define ll long long

using namespace std;

const int P = 998244353;
const int N = 510;

int n, m;
int p[N], now[N], tmp[N];
ll g[N][N], f[N][N];
bool avail[N][N];

int main (void) {

    scanf ("%d%d", &n, &m);
    for (int i = 1, u; i <= n; i ++) scanf ("%d", p + i);
    for (int j = n; j; j --) p[j] = (p[j] - p[1] + n) % n + 1;
    for (int i = 1; i <= n; i ++) for (int j = i; j <= n; j ++) avail[i][j] = true;

    for (int i = 2; i <= m; i ++) {
        for (int i = 1; i <= n; i ++) scanf ("%d", now + i);
        for (int j = n; j; j --) now[j] = (now[j] - now[1] + n) % n + 1;
        for (int i = 1; i <= n; i ++) tmp[p[i]] = now[i];
        for (int j = 1; j <= n; j ++) {
            int mx = tmp[j], mn = tmp[j];
            for (int k = j + 1; k <= n; k ++) {
                mx = max (mx, tmp[k]), mn = min (mn, tmp[k]);
                if (mx - mn != k - j) avail[j][k] = false;
            }
        }
    }

    for (int i = 1; i <= n + 1; i ++) g[i][i - 1] = 1;
    for (int len = 1; len <= n; len ++) {
        for (int i = 1; i <= n; i ++) {
            int j = i + len - 1;
            if (j > n) break ;
            if (avail[i][j])
            for (int k = i; k <= j; k ++) (f[i][j] += g[i][k - 1] * g[k + 1][j]) %= P;
            for (int k = i; k <= j; k ++)     (g[i][j] += f[i][k] * g[k + 1][j]) %= P;
        }
    }

    printf ("%lld\n", g[2][n]);

    return 0;
}