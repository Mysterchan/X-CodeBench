#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int MOD = 998244353;
const int PRIMITIVE_ROOT = 3;

// fast exponentiation mod
ll modexp(ll a, ll e = MOD - 2) {
    ll r = 1;
    while (e) {
        if (e & 1) r = (r * a) % MOD;
        a = (a * a) % MOD;
        e >>= 1;
    }
    return r;
}

// In-place iterative NTT
void ntt(vector<int> & a, bool invert) {
    int n = a.size();
    static vector<int> rev;
    static vector<ll> roots{0,1};
    if ((int)rev.size() != n) {
        int k = __builtin_ctz(n);
        rev.assign(n,0);
        for (int i = 0; i < n; i++) {
            rev[i] = (rev[i>>1] >> 1) | ((i&1) << (k-1));
        }
    }
    if ((int)roots.size() < n) {
        // build roots up to n
        ll root = modexp(PRIMITIVE_ROOT, (MOD-1)/n);
        int cur = roots.size();
        roots.resize(n);
        for (; cur < n; ++cur) {
            roots[cur] = roots[cur-1] * root % MOD;
        }
    }
    for (int i = 0; i < n; i++) {
        if (i < rev[i]) swap(a[i], a[rev[i]]);
    }
    for (int len = 1; len < n; len <<= 1) {
        for (int i = 0; i < n; i += 2*len) {
            for (int j = 0; j < len; j++) {
                ll u = a[i+j];
                ll v = a[i+j+len] * roots[len+j] % MOD;
                a[i+j] = (u + v < MOD ? u + v : u + v - MOD);
                a[i+j+len] = (u - v >= 0 ? u - v : u - v + MOD);
            }
        }
    }
    if (invert) {
        reverse(a.begin()+1, a.end());
        ll inv_n = modexp(n, MOD-2);
        for (int & x: a) x = (ll)x * inv_n % MOD;
    }
}

// convolution: c = a * b
vector<int> convolution(const vector<int> &a, const vector<int> &b) {
    int na = a.size(), nb = b.size();
    if (!na || !nb) return {};
    int n = 1;
    while (n < na + nb - 1) n <<= 1;
    vector<int> fa(a.begin(), a.end()), fb(b.begin(), b.end());
    fa.resize(n);
    fb.resize(n);
    ntt(fa, false);
    ntt(fb, false);
    for (int i = 0; i < n; i++) {
        fa[i] = (ll)fa[i] * fb[i] % MOD;
    }
    ntt(fa, true);
    fa.resize(na + nb - 1);
    return fa;
}

int N2;
vector<int> c0, c1;
vector<int> fac, ifac;
vector<int> q;

void cdq(int l, int r) {
    int w = r - l + 1;
    if (w == 1) return;
    int mid = l + (w/2) - 1;
    // solve left half
    cdq(l, mid);
    // build ql
    int left_len = mid - l + 1;  // w/2 + 1
    int right_len = 2*w + 1;
    vector<int> ql(left_len, 0), qr(right_len, 0);
    for (int i = l; i <= mid; i++) {
        int j = c1[i] - c1[l];
        if (j >= 0 && j < left_len) {
            ql[j] = (ql[j] + q[i]) % MOD;
        }
    }
    int d = c0[l] - c1[l];
    // fill qr[k] for k in [0..2*w], corresponding to index (k - w)
    for (int k = 0; k <= 2*w; k++) {
        int idx = k - w + d;
        if (idx >= 0 && idx <= N2) {
            qr[k] = fac[idx];
        }
    }
    // convolution
    vector<int> conv = convolution(ql, qr);
    // apply to right half
    for (int i = mid+1; i <= r; i++) {
        int j1 = c0[i] - c0[l];
        int j2 = c0[i] - c1[i];
        if (j1 >= 0 && j2 >= 0 && j2 <= N2) {
            int pos = w + j1;
            if (pos < (int)conv.size()) {
                ll val = conv[pos];
                // fb[j2] = invfac[N2 - j2]
                val = val * ifac[N2 - j2] % MOD;
                q[i] = (q[i] + MOD - val) % MOD;
            }
        }
    }
    // solve right half
    cdq(mid+1, r);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    string s;
    cin >> n >> s;
    N2 = 2*n;
    c0.assign(N2+1, 0);
    c1.assign(N2+1, 0);
    for (int i = 1; i <= N2; i++) {
        c0[i] = c0[i-1] + (s[i-1] == 'W');
        c1[i] = c1[i-1] + (s[i-1] == 'B');
    }
    // factorials
    fac.assign(N2+1, 1);
    for (int i = 1; i <= N2; i++) fac[i] = (ll)fac[i-1] * i % MOD;
    ifac.assign(N2+1, 1);
    ifac[N2] = modexp(fac[N2]);
    for (int i = N2; i > 0; i--) ifac[i-1] = (ll)ifac[i] * i % MOD;

    q.assign(N2+1, 0);
    q[0] = (MOD - 1) % MOD;  // -1 mod

    cdq(0, N2);
    cout << q[N2] << "\n";
    return 0;
}