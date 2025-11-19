#include <bits/stdc++.h>
#define ll long long
using namespace std;
inline ll Read() {
    int sig = 1; ll num = 0; char c = getchar();
    while(!isdigit(c)) { if(c == '-') sig = -1; c = getchar(); }
    while(isdigit(c)) num = (num << 3) + (num << 1) + (c ^ 48), c = getchar();
    return num * sig;
}
void Write(ll x) {
    if(x < 0) putchar('-'), x = -x;
    if(x > 9) Write(x / 10);
    putchar((x % 10) ^ 48);
}
const int N = 24;
const ll Mod = 998244353;
int n, m; ll cnt[1 << N], f[(1 << N) + 5], g[1 << N], p[1 << N], q[1 << N];
void Add(ll &x, ll y) { x += y; if(x >= Mod) x -= Mod; }
void Solve(int l, int r) {
    if(l + 1 == r) { Add(p[l], f[l]), f[l + 1] = g[l] = (cnt[l] * p[l] - q[l] + Mod) % Mod, Add(q[l], g[l]); return ; }
    int i, mid = (l + r) >> 1;
    for(i = l; i < mid; i++) Add(p[i + mid - l], Mod - p[i]), Add(q[i + mid - l], Mod - q[i]);
    Solve(l, mid);
    for(i = l; i < mid; i++) Add(p[i + mid - l], p[i]), Add(q[i + mid - l], q[i]);
    Solve(mid, r);
}
int main() {
    int i, j; n = Read(), m = Read(); while(m--) cnt[Read()]++;
    for(i = 0; i < n; i++) for(j = 1; j < (1 << n); j++) if((j >> i) & 1) Add(cnt[j], cnt[j ^ (1 << i)]);
    f[0] = 1, Solve(0, 1 << n), Write(f[1 << n]);
}