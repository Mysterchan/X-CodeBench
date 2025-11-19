#include <bits/stdc++.h>
using namespace std;
using ll = long long;
constexpr ll MOD = 998244353;

inline ll mod_add(ll a, ll b) {
    a += b;
    if (a >= MOD) a -= MOD;
    return a;
}

inline ll mod_sub(ll a, ll b) {
    a -= b;
    if (a < 0) a += MOD;
    return a;
}

inline ll mod_mul(ll a, ll b) {
    return (a * b) % MOD;
}

ll mod_pow(ll base, ll exp) {
    ll res = 1;
    ll cur = base % MOD;
    while (exp > 0) {
        if (exp & 1) res = mod_mul(res, cur);
        cur = mod_mul(cur, cur);
        exp >>= 1;
    }
    return res;
}

struct Combination {
    int n;
    vector<ll> fact, inv_fact;

    Combination(int n_): n(n_) {
        fact.resize(n+1);
        inv_fact.resize(n+1);
        fact[0] = 1;
        for (int i = 1; i <= n; i++) fact[i] = mod_mul(fact[i-1], i);
        inv_fact[n] = mod_pow(fact[n], MOD - 2);
        for (int i = n-1; i >= 0; i--) inv_fact[i] = mod_mul(inv_fact[i+1], i+1);
    }

    ll binom(int n_, int k_) {
        if (k_ < 0 || k_ > n_) return 0;
        return mod_mul(fact[n_], mod_mul(inv_fact[k_], inv_fact[n_-k_]));
    }
};

// NTT implementation for convolution modulo 998244353
// Reference: https://cp-algorithms.com/math/fft.html#ntt
struct NTT {
    static constexpr int mod = 998244353;
    static constexpr int root = 15311432; // 3^(119) mod mod
    static constexpr int root_1 = 469870224; // inverse of root
    static constexpr int root_pw = 1 << 23;

    static void ntt(vector<ll> & a, bool invert) {
        int n = (int)a.size();
        for (int i = 1, j = 0; i < n; i++) {
            int bit = n >> 1;
            for (; j & bit; bit >>= 1)
                j ^= bit;
            j ^= bit;
            if (i < j) swap(a[i], a[j]);
        }

        for (int len = 2; len <= n; len <<= 1) {
            ll wlen = invert ? root_1 : root;
            for (int i = len; i < root_pw; i <<= 1)
                wlen = (wlen * wlen) % mod;
            for (int i = 0; i < n; i += len) {
                ll w = 1;
                for (int j = 0; j < len / 2; j++) {
                    ll u = a[i + j], v = (a[i + j + len / 2] * w) % mod;
                    a[i + j] = u + v < mod ? u + v : u + v - mod;
                    a[i + j + len / 2] = u - v >= 0 ? u - v : u - v + mod;
                    w = (w * wlen) % mod;
                }
            }
        }
        if (invert) {
            ll n_inv = mod_pow(n, mod - 2);
            for (ll & x : a) x = (x * n_inv) % mod;
        }
    }

    static vector<ll> multiply(const vector<ll> & a, const vector<ll> & b) {
        vector<ll> fa(a.begin(), a.end()), fb(b.begin(), b.end());
        int n = 1;
        while (n < (int)(a.size() + b.size() - 1)) n <<= 1;
        fa.resize(n);
        fb.resize(n);

        ntt(fa, false);
        ntt(fb, false);
        for (int i = 0; i < n; i++) {
            fa[i] = (fa[i] * fb[i]) % mod;
        }
        ntt(fa, true);
        fa.resize(a.size() + b.size() - 1);
        return fa;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; ll x, y;
    cin >> n >> x >> y;
    vector<ll> A(n), B(n);
    for (int i = 0; i < n; i++) cin >> A[i] >> B[i];

    // If parity of X and Y are same or all A_i == 0
    // Use simplified counting
    bool same_parity = ((x & 1) == (y & 1));
    bool all_zero_a = true;
    for (int i = 0; i < n; i++) {
        if (A[i] != 0) {
            all_zero_a = false;
            break;
        }
    }

    if (same_parity || all_zero_a) {
        // c[i] = A[i]*(x+1) + B[i]
        // Count how many c[i] are even and odd
        int even = 0, odd = 0;
        ll x1 = x + 1;
        for (int i = 0; i < n; i++) {
            ll c = A[i] * x1 + B[i];
            if ((c & 1) == 0) even++;
            else odd++;
        }

        Combination comb(odd);
        ll ans = 0;
        // sum of binom(odd, i) for i > odd/2
        // i > odd/2 means i > floor(odd/2)
        int half = odd / 2;
        for (int i = half + 1; i <= odd; i++) {
            ans = mod_add(ans, comb.binom(odd, i));
        }
        // multiply by 2^even
        ans = mod_mul(ans, mod_pow(2, even));
        cout << ans << "\n";
        return 0;
    }

    // When parity of x and y differ
    // Categorize bags into ta, ao, fi, se as per original logic
    int ta = 0, ao = 0, fi = 0, se = 0;
    for (int i = 0; i < n; i++) {
        if (A[i] == 0) {
            if ((B[i] & 1) == 1) fi++;
            else se++;
        } else if (A[i] == 1) {
            // For A[i] == 1, check parity of B[i] and parity of x,y
            if ((B[i] & 1) == 0) {
                if ((x & 1) == 0) ta++;
                if ((y & 1) == 0) ao++;
            } else {
                fi++;
            }
        } else {
            // A[i] >= 2
            if ((x & 1) == 0) ta++;
            if ((y & 1) == 0) ao++;
        }
    }

    // We want to compute:
    // (1 + z)^{ao + ta} * (1 + z^2)^{fi}
    // Then sum coefficients with degree > ao + fi
    // Multiply by 2^{se}

    // Precompute powers using fast exponentiation and NTT convolution

    // Base polynomials:
    // x1 = (1 + z)
    // x2 = (1 + z^2)

    // We'll implement fast exponentiation of polynomials with NTT

    // To speed up, we can use binary exponentiation with NTT

    // Polynomial exponentiation by squaring
    auto poly_pow = [&](const vector<ll> &base, int exp) -> vector<ll> {
        vector<ll> res = {1};
        vector<ll> cur = base;
        while (exp > 0) {
            if (exp & 1) {
                res = NTT::multiply(res, cur);
                if ((int)res.size() > 200000) res.resize(200000); // limit size to avoid TLE
            }
            cur = NTT::multiply(cur, cur);
            if ((int)cur.size() > 200000) cur.resize(200000);
            exp >>= 1;
        }
        return res;
    };

    vector<ll> x1 = {1, 1};
    vector<ll> x2 = {1, 0, 1};

    vector<ll> p1 = poly_pow(x1, ao + ta);
    vector<ll> p2 = poly_pow(x2, fi);

    vector<ll> p = NTT::multiply(p1, p2);

    // sum coefficients with degree > ao + fi
    ll ans = 0;
    int start = ao + fi + 1;
    for (int i = start; i < (int)p.size(); i++) {
        ans = mod_add(ans, p[i]);
    }

    ans = mod_mul(ans, mod_pow(2, se));

    cout << ans << "\n";

    return 0;
}