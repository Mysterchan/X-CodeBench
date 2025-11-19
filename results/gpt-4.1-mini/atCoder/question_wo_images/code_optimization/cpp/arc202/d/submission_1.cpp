#include <bits/stdc++.h>
using namespace std;

constexpr int mod = 998244353;
using ll = long long;

inline int add(int a, int b) {
    a += b;
    if (a >= mod) a -= mod;
    return a;
}
inline int sub(int a, int b) {
    a -= b;
    if (a < 0) a += mod;
    return a;
}
inline int mul(int a, int b) {
    return (ll)a * b % mod;
}

int qpow(int a, int b) {
    int res = 1;
    while (b > 0) {
        if (b & 1) res = mul(res, a);
        a = mul(a, a);
        b >>= 1;
    }
    return res;
}

struct NTT {
    int base = 1;
    int max_base = 23; // 2^23 = 8,388,608 > max needed
    int root = 15311432; // primitive root for mod=998244353
    int inv_root = 469870224; // inverse of root
    int root_pw = 1 << max_base;

    vector<int> rev;

    void ensure_base(int nbase) {
        if (nbase <= base) return;
        rev.resize(1 << nbase);
        for (int i = 0; i < (1 << nbase); i++) {
            rev[i] = (rev[i >> 1] >> 1) | ((i & 1) << (nbase - 1));
        }
        base = nbase;
    }

    void ntt(vector<int> &a, bool invert) {
        int n = (int)a.size();
        int nbase = 0;
        while ((1 << nbase) < n) nbase++;
        ensure_base(nbase);

        for (int i = 0; i < n; i++) {
            if (i < rev[i]) swap(a[i], a[rev[i]]);
        }

        for (int len = 1; len < n; len <<= 1) {
            int wlen = invert ? inv_root : root;
            for (int i = len << 1; i < root_pw; i <<= 1) {
                wlen = (int)((ll)wlen * wlen % mod);
            }
            for (int i = 0; i < n; i += (len << 1)) {
                int w = 1;
                for (int j = 0; j < len; j++) {
                    int u = a[i + j];
                    int v = (int)((ll)a[i + j + len] * w % mod);
                    a[i + j] = u + v < mod ? u + v : u + v - mod;
                    a[i + j + len] = u - v >= 0 ? u - v : u - v + mod;
                    w = (int)((ll)w * wlen % mod);
                }
            }
        }
        if (invert) {
            int nrev = qpow(n, mod - 2);
            for (int &x : a) x = (int)((ll)x * nrev % mod);
        }
    }

    vector<int> multiply(const vector<int> &a, const vector<int> &b) {
        int need = (int)(a.size() + b.size() - 1);
        int nbase = 0;
        while ((1 << nbase) < need) nbase++;
        int n = 1 << nbase;
        vector<int> fa(a.begin(), a.end()), fb(b.begin(), b.end());
        fa.resize(n);
        fb.resize(n);

        ntt(fa, false);
        ntt(fb, false);
        for (int i = 0; i < n; i++) {
            fa[i] = (int)((ll)fa[i] * fb[i] % mod);
        }
        ntt(fa, true);
        fa.resize(need);
        return fa;
    }
} ntt;

const int MAXT = 300000;
int fact[MAXT + 1], invfact[MAXT + 1];

int comb(int n, int r) {
    if (r > n || r < 0) return 0;
    return (ll)fact[n] * invfact[r] % mod * invfact[n - r] % mod;
}

void init_fact(int n) {
    fact[0] = 1;
    for (int i = 1; i <= n; i++) fact[i] = (ll)fact[i - 1] * i % mod;
    invfact[n] = qpow(fact[n], mod - 2);
    for (int i = n - 1; i >= 0; i--) invfact[i] = (ll)invfact[i + 1] * (i + 1) % mod;
}

// The problem reduces to counting sequences of king moves on a grid.
// The king moves to one of 8 adjacent squares each step.
// The number of sequences to go from (A,B) to (C,D) in T steps is:
// sum_{i=0}^T (-1)^i * C(T, i) * f(i) * g(i)
// where f(i) and g(i) are counts of 1D moves in row and column directions respectively,
// computed by a special DP using polynomial exponentiation with truncation.

// We implement the optimized polynomial exponentiation with truncation and DP as in original code,
// but simplified and optimized for speed and clarity.

int H, W, T, A, B, C, D;

int abs_diff(int x, int y) {
    return x > y ? x - y : y - x;
}

// We implement the calc function to compute f array for one dimension.
// It uses divide and conquer and polynomial exponentiation with truncation.

void pmod(vector<int> &a, int s) {
    while ((int)a.size() > s) {
        int idx = (int)a.size() - s - 1;
        a[idx] = (a[idx] + a.back()) % mod;
        a.pop_back();
    }
}

vector<int> poly_pow(vector<int> a, int b, int s) {
    vector<int> res = {1};
    while (b > 0) {
        if (b & 1) {
            res = ntt.multiply(res, a);
            pmod(res, s);
        }
        a = ntt.multiply(a, a);
        pmod(a, s);
        b >>= 1;
    }
    return res;
}

void calc(int l, int r, int ps, int sz, vector<int> &A, int d, int *f) {
    if (l == r) {
        int x = (ps - d) % sz;
        if (x < 0) x += sz;
        f[l] = (x < (int)A.size()) ? A[x] : 0;
        return;
    }
    int m = (l + r) >> 1;
    int dl, dr;
    vector<int> B, C;

    if (2 * (m - l) + 1 >= sz) {
        B = A;
        dl = d;
    } else {
        dl = ps - (m - l);
        B.reserve(2 * (m - l) + 1);
        for (int i = ps - (m - l); i <= ps + (m - l); i++) {
            int x = (i - d) % sz;
            if (x < 0) x += sz;
            B.push_back(x < (int)A.size() ? A[x] : 0);
        }
    }
    calc(l, m, ps, sz, B, dl, f);

    vector<int> powA = poly_pow({1, 1, 1}, m - l + 1, sz);
    A = ntt.multiply(A, powA);
    pmod(A, sz);
    d -= (m - l + 1);

    if (2 * (r - m - 1) + 1 >= sz) {
        C = A;
        dr = d;
    } else {
        dr = ps - (r - m - 1);
        C.reserve(2 * (r - m - 1) + 1);
        for (int i = ps - (r - m - 1); i <= ps + (r - m - 1); i++) {
            int x = (i - d) % sz;
            if (x < 0) x += sz;
            C.push_back(x < (int)A.size() ? A[x] : 0);
        }
    }
    calc(m + 1, r, ps, sz, C, dr, f);
}

int f_arr[MAXT + 1], g_arr[MAXT + 1];

void sol(int n, int m, int s, int t, int *f) {
    vector<int> A(2 * n + 3, 0);
    A[0] = 1;
    calc(0, m, abs_diff(s, t), 2 * n + 2, A, 0, f);

    calc(0, m, abs_diff(s + t - 2 * n - 2, 0), 2 * n + 2, A, 0, g_arr);

    for (int i = 0; i <= m; i++) {
        f[i] = (f[i] - g_arr[i] + mod) % mod;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> H >> W >> T >> A >> B >> C >> D;

    init_fact(T);

    // Compute f and g arrays for rows and columns
    sol(H, T, A, C, f_arr);
    sol(W, T, B, D, g_arr);

    int ans = 0;
    for (int i = 0; i <= T; i++) {
        int sign = ((T - i) & 1) ? mod - 1 : 1;
        int val = mul(mul(f_arr[i], g_arr[i]), comb(T, i));
        ans = (ans + (ll)sign * val) % mod;
    }

    cout << ans << "\n";
    return 0;
}