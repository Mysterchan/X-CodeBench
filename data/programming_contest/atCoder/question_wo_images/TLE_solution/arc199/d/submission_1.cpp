#include<iostream>
#include<cstring>
#include<vector>
#include<stdint.h>
using namespace std;
using LL = long long;
const int maxn = 2e5 + 5, mod = 998244353;
template<const int T>
struct ModInt {
    const static int mod = T;
    int x;
    ModInt(int x = 0) : x(x % mod) {}
    ModInt(long long x) : x(int(x % mod)) {} 
    int val() { return x; }
    ModInt operator + (const ModInt &a) const { int x0 = x + a.x; return ModInt(x0 < mod ? x0 : x0 - mod); }
    ModInt operator - (const ModInt &a) const { int x0 = x - a.x; return ModInt(x0 < 0 ? x0 + mod : x0); }
    ModInt operator * (const ModInt &a) const { return ModInt(1LL * x * a.x % mod); }
    ModInt operator / (const ModInt &a) const { return *this * a.inv(); }
    bool operator == (const ModInt &a) const { return x == a.x; };
    bool operator != (const ModInt &a) const { return x != a.x; };
    void operator += (const ModInt &a) { x += a.x; if (x >= mod) x -= mod; }
    void operator -= (const ModInt &a) { x -= a.x; if (x < 0) x += mod; }
    void operator *= (const ModInt &a) { x = 1LL * x * a.x % mod; }
    void operator /= (const ModInt &a) { *this = *this / a; }
    friend ModInt operator + (int y, const ModInt &a){ int x0 = y + a.x; return ModInt(x0 < mod ? x0 : x0 - mod); }
    friend ModInt operator - (int y, const ModInt &a){ int x0 = y - a.x; return ModInt(x0 < 0 ? x0 + mod : x0); }
    friend ModInt operator * (int y, const ModInt &a){ return ModInt(1LL * y * a.x % mod);}
    friend ModInt operator / (int y, const ModInt &a){ return ModInt(y) / a;}
    friend ostream &operator<<(ostream &os, const ModInt &a) { return os << a.x;}
    friend istream &operator>>(istream &is, ModInt &t){return is >> t.x;}

    ModInt pow(int64_t n) const {
        ModInt res(1), mul(x);
        while(n){
            if (n & 1) res *= mul;
            mul *= mul;
            n >>= 1;
        }
        return res;
    }
    
    ModInt inv() const {
        int a = x, b = mod, u = 1, v = 0;
        while (b) {
            int t = a / b;
            a -= t * b; swap(a, b);
            u -= t * v; swap(u, v);
        }
        if (u < 0) u += mod;
        return u;
    }
    
};
using mint = ModInt<mod>;

mint fact[maxn], invfact[maxn];

void init(){
    fact[0] = invfact[0] = 1;
    for(int i = 1; i < maxn; i++) fact[i] = fact[i - 1] * i;
    invfact[maxn - 1] = fact[maxn - 1].inv();
    for(int i = maxn - 2; i; i--)
        invfact[i] = invfact[i + 1] * (i + 1);  
}

inline mint C(int a, int b){
    if (a < 0 || b < 0 || a < b) return 0;
    return fact[a] * invfact[b] * invfact[a - b];
}

int main(){

#ifdef LOCAL
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
#endif

    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(0);

    init();
    int n, m;
    cin >> n >> m;
    vector<mint> dp(m + 1), cnt(m + 1);
    cnt[0] = 1;
    for(int i = 0; i < n; i++){
        vector<mint> ndp(m + 1), ncnt(m + 1);
        for(int j = 0; j <= m; j++){
            for(int k = j; k <= m; k++){
                ncnt[k] += cnt[j] * C(k + 1, j);
                ndp[k] += dp[j] * C(k + 1, j);
                ndp[k] += cnt[j] * C(k + 1, j - 1);
            }
            ndp[j] += ncnt[j] * (m - j);
        }
        dp.swap(ndp);
        cnt.swap(ncnt);
    }
    mint ans = 0;
    for(int i = 0; i <= m; i++){
        ans += dp[i] * C(m, i);
    }
    cout << ans << '\n';

}