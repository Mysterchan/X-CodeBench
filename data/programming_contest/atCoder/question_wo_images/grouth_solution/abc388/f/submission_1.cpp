#include<algorithm>
#include<bitset>
#include<climits>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iomanip>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<string>
#include<unordered_map>
#include<unordered_set>
#include<vector>
#include<random>

using namespace std;

#define int long long
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

constexpr ll mod = 998244353;

#define lson(x) (x << 1)
#define rson(x) (x << 1 | 1)

inline int lowbit(int x) {
    return x & (-x);
}

inline ll ksm(ll a, ll b) {
    ll res = 1;
    while (b) {
        if (b & 1) res = res * a % mod;
        a = a * a % mod;
        b >>= 1;
    }
    return res;
}

constexpr int maxn = 2e4 + 10;
constexpr int base = 29;
constexpr int eps = 1e-7;
constexpr int intinf = 1e9 + 10;
constexpr int dx[] = { 1,-1,0,0 };
constexpr int dy[] = { 0,0,1,-1 };

int n, m, a, b, l[maxn], r[maxn];

int martix_G[21][21][41], martix_B[21][21][41], ans[21], cur[21];

void mul(int r) {
    for (int k = 1; k <= 20; k++)
        for (int i = 1; i <= 20; i++)
            for (int j = 1; j <= 20; j++) {
                martix_G[i][j][r] |= (martix_G[i][k][r - 1] & martix_G[k][j][r - 1]);
                martix_B[i][j][r] |= (martix_B[i][k][r - 1] & martix_B[k][j][r - 1]);
            }
}

void mul_G(int x) {
    for (int bit = 40; bit >= 0; bit--)
        if ((x >> bit) & 1) {
            for (int i = 1; i <= 20; i++) cur[i] = 0;
            for (int i = 1; i <= 20; i++)
                for (int j = 1; j <= 20; j++)
                    cur[i] |= martix_G[i][j][bit] & ans[j];
            for (int i = 1; i <= 20; i++) ans[i] = cur[i];
        }
}

void mul_B(int x) {
    for (int bit = 40; bit >= 0; bit--)
        if ((x >> bit) & 1) {
            for (int i = 1; i <= 20; i++) cur[i] = 0;
            for (int i = 1; i <= 20; i++)
                for (int j = 1; j <= 20; j++)
                    cur[i] |= martix_B[i][j][bit] & ans[j];
            for (int i = 1; i <= 20; i++) ans[i] = cur[i];
        }
}

void solve(int id) {
    cin >> n >> m >> a >> b;
    for (int i = 1; i <= m; i++)
        cin >> l[i] >> r[i];
    ans[1] = 1;
    for (int i = a; i <= b; i++) martix_G[1][i][0] = 1;
    for (int i = 2; i <= 20; i++) martix_G[i][i - 1][0] = martix_B[i][i - 1][0] = 1;
    for (int i = 1; i <= 40; i++) mul(i);
    r[0] = 1;
    for (int i = 1; i <= m; i++) {
        mul_G(l[i] - r[i - 1] - 1);
        mul_B(r[i] - l[i] + 1);
    }
    mul_G(n - r[m]);
    if (ans[1]) cout << "Yes\n";
    else cout << "No\n";

}

signed main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int T = 1;
    //cin >> T;
    for (int i = 1; i <= T; i++)
        solve(i);
    return 0;
}