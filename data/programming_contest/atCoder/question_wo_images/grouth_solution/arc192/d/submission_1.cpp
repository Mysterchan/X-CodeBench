const int MOD = 998'244'353;

#include <bits/stdc++.h>

using namespace std;

#ifdef LOCAL
#define dbg(x) cerr << __LINE__ << " " << #x << " " << x << endl
#define ln cerr << __LINE__ << " fine, thanks" << endl
#else
#define dbg(x) void(0)
#define ln void(0)
#endif 

template <typename T>
istream& operator>>(istream& in, vector<T>& a)
{
    for (auto& e : a) in >> e;
    return in;
}

template <typename F, typename S>
istream& operator>>(istream& in, pair<F, S>& p)
{
    in >> p.first >> p.second;
    return in;
}

template <typename T>
ostream& operator<<(ostream& out, const vector<T>& a)
{
    for (auto &e : a)
    {
        out << e << " ";
        if (typeid(T) != typeid(int) && typeid(T) != typeid(long long))
            out << "\n";
    }
    return out;
}

template <typename F, typename S>
ostream& operator<<(ostream& out, const pair<F, S>& p)
{
    out << p.first << " " << p.second;
    return out;
}

template <const int mod = MOD>
struct modint
{
    int val;

    modint()
    {
        val = 0;
    }

    modint(int x)
    {
        if (x < 0 || x >= mod)
            x = x % mod;
        if (x < 0)
            x += mod;
        val = x;
    }

    modint(long long x)
    {
        if (x < 0 || x >= mod)
            x = x % mod;
        if (x < 0)
            x += mod;
        val = x;
    }

    inline modint<mod> operator+=(const modint<mod>& other)
    {
        val += other.val;
        if (val >= mod)
            val -= mod;
        return *this;
    }

    inline modint<mod> operator-=(const modint<mod>& other)
    {
        val -= other.val;
        if (val < 0)
            val += mod;
        return *this;
    }

    inline modint<mod> operator*=(const modint<mod>& other)
    {
        val = 1ll * val * other.val % mod;
        return *this;
    }

    inline modint<mod> operator/=(const modint<mod>& other)
    {
        *this *= inv(other);
        return *this;
    }

    inline bool operator==(const modint<mod>& other)
    {
        return val == other.val;
    }
};

template <const int mod>
inline modint<mod> operator+(modint<mod> x, const modint<mod>& y)
{
    x += y;
    return x;
}

template <const int mod>
inline modint<mod> operator+(modint<mod> x, const long long& y)
{
    x += y;
    return x;
}

template <const int mod>
inline modint<mod> operator+(const long long& x, modint<mod> y)
{
    y += x;
    return y;
}

template <const int mod>
inline modint<mod> operator-(modint<mod> x, const modint<mod>& y)
{
    x -= y;
    return x;
}

template <const int mod>
inline modint<mod> operator-(modint<mod> x, const long long& y)
{
    x -= y;
    return x;
}

template <const int mod>
inline modint<mod> operator-(const long long& x, const modint<mod>& y)
{
    return modint<mod>(x - y.val);
}

template <const int mod>
inline modint<mod> operator*(modint<mod> x, const modint<mod>& y)
{
    x *= y;
    return x;
}

template <const int mod>
inline modint<mod> operator*(modint<mod> x, const long long& y)
{
    x *= y;
    return x;
}

template <const int mod>
inline modint<mod> operator*(const long long& x, modint<mod> y)
{
    y *= x;
    return y;
}

template <const int mod>
inline modint<mod> binpow(const modint<mod>& x, long long d)
{
    modint<mod> res = 1, f = x;
    while (d >= 1)
    {
        if (d % 2) res *= f;
        f *= f;
        d /= 2;
    }
    return res;
}

template <const int mod>
inline modint<mod> inv(const modint<mod>& x)
{
    return binpow(x, mod - 2);
}

template <const int mod>
inline modint<mod> operator/(modint<mod> x, const modint<mod>& y)
{
    x /= y;
    return x;
}

template <const int mod>
inline modint<mod> operator/(modint<mod> x, const long long& y)
{
    x /= y;
    return x;
}

template <const int mod>
inline modint<mod> operator/(const long long& x, const modint<mod>& y)
{
    return (modint<mod>(x) / y);
}

template <const int mod>
istream& operator>>(istream& in, modint<mod>& a)
{
    in >> a.val;
    return in;
}

template <const int mod>
ostream& operator<<(ostream& out, const modint<mod>& a)
{
    out << a.val;
    return out;
}

inline long long binpow(long long x, long long d, long long mod)
{
    long long res = 1 % mod, f = x % mod;
    while (d >= 1)
    {
        if (d % 2) res = res * f % mod;
        f = f * f % mod;
        d /= 2;
    }
    return res;
}

#define forn(i, n) for (int i = 0; (i) != (n); (i)++)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define popcount(x) __builtin_popcount(x)
#define popcountll(x) __builtin_popcountll(x)
#define fi first
#define se second
#define re return
#define pb push_back
#define uniq(x) sort(all(x)); (x).resize(unique(all(x)) - (x).begin())
#define safe(x, n) (0 <= (x) && (x) < (n))
#define withBit(mask, i) ((mask & (1LL << (i))) > 0)

using mint = modint<MOD>;

void solve()
{
    int n;
    cin >> n;
    n--;

    vector<int> a(n);
    cin >> a;

    mint ans = 1;
    const int N = 1000;
    vector<int> sieve(N + 1);
    for (int p = 2; p <= N; p++) {
        if (sieve[p]) continue;

        for (int j = p; j <= N; j += p) sieve[j] = 1;
        
        vector<int> cnt(n);
        for (int i = 0; i < n; i++) {
            while (a[i] % p == 0) {
                a[i] /= p;
                cnt[i]++;
            }
        }

        int sum = accumulate(all(cnt), 0);
        if (sum == 0) continue;

        vector<mint> pows(sum + 1);
        pows[0] = 1;
        for (int i = 1; i <= sum; i++) pows[i] = pows[i - 1] * p;

        vector<pair<mint, mint> > dp0(sum + 1), dp1(sum + 1);
        for (int cur = 1; cur <= sum; cur++) {
            dp0[cur] = {pows[cur], 0};
        }
        dp0[0] = {0, pows[0]};

        int ind = -1;
        for (auto e : cnt) {
            if (e == 0) {
                for (int i = 0; i <= sum; i++) {
                    dp0[i].first *= pows[i];
                    dp0[i].second *= pows[i];
                }
                continue;
            }

            ind++;

            for (int i = 0; i <= sum; i++) {
                dp1[i] = {0, 0};
            }

            for (int i = e + 1; i <= sum; i++) {
                dp1[i - e].first += dp0[i].first * pows[i - e];
                dp1[i - e].second += dp0[i].second * pows[i - e];
            }
            dp1[0].second += dp0[e].first * pows[0];
            dp1[0].second += dp0[e].second * pows[0];

            for (int i = 0; i + e <= sum; i++) {
                dp1[i + e].first += dp0[i].first * pows[i + e];
                dp1[i + e].second += dp0[i].second * pows[i + e];
            }

            swap(dp0, dp1);
        }

        mint total = 0;
        for (int x = 0; x <= sum; x++) {
            total += dp0[x].second;
        }
        ans *= total;
    }
    cout << ans << "\n";
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    #ifdef LOCAL
    double st = clock();
    #endif 

    int t = 1;
    #ifdef tests
    cin >> t;
    #endif
    while (t--)
    {
        solve();
    }

    #ifdef LOCAL
    cerr << setprecision(5) << "Succeed in " << (clock() - st) / CLOCKS_PER_SEC << " s\n";
    #endif 
}
