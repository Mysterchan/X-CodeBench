#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int MOD = 998244353;
const int G = 3;

ll modpow(ll a, ll e = MOD-2) {
    ll r = 1;
    while (e) {
        if (e & 1) r = r * a % MOD;
        a = a * a % MOD;
        e >>= 1;
    }
    return r;
}

void ntt(vector<ll> & a, bool invert) {
    int n = a.size();
    static vector<int> rev;
    static vector<ll> roots{0,1};
    if ((int)rev.size() != n) {
        int k = __builtin_ctz(n);
        rev.assign(n,0);
        for (int i = 0; i < n; i++)
            rev[i] = (rev[i>>1]>>1) | ((i&1)<<(k-1));
    }
    for (int i = 0; i < n; i++)
        if (i < rev[i])
            swap(a[i], a[rev[i]]);
    if ((int)roots.size() < n) {
        int k = __builtin_ctz(roots.size());
        roots.resize(n);
        while ((1<<k) < n) {
            ll e = modpow(G, (MOD-1) >> (k+1));
            for (int i = 1<<(k-1); i < (1<<k); i++) {
                roots[2*i] = roots[i];
                roots[2*i+1] = roots[i] * e % MOD;
            }
            k++;
        }
    }
    for (int len = 1; len < n; len <<= 1) {
        for (int i = 0; i < n; i += 2*len) {
            for (int j = 0; j < len; j++) {
                ll u = a[i+j];
                ll v = a[i+j+len] * roots[len+j] % MOD;
                a[i+j] = u + v < MOD ? u+v : u+v-MOD;
                a[i+j+len] = u - v >= 0 ? u-v : u-v+MOD;
            }
        }
    }
    if (invert) {
        reverse(a.begin()+1, a.end());
        ll inv_n = modpow(n);
        for (int i = 0; i < n; i++)
            a[i] = a[i] * inv_n % MOD;
    }
}

vector<ll> convolution(const vector<ll>& a, const vector<ll>& b, int cap) {
    int na = a.size(), nb = b.size();
    if (!na || !nb) return {};
    int need = na + nb - 1;
    int sz = 1;
    while (sz < need) sz <<= 1;
    vector<ll> fa(sz), fb(sz);
    for (int i = 0; i < na; i++) fa[i] = a[i];
    for (int i = 0; i < nb; i++) fb[i] = b[i];
    ntt(fa, false); ntt(fb, false);
    for (int i = 0; i < sz; i++) fa[i] = fa[i] * fb[i] % MOD;
    ntt(fa, true);
    int out = min(need, cap);
    fa.resize(out);
    return fa;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    // factorials for binom up to N
    vector<ll> fact(N+1), invfact(N+1);
    fact[0] = 1;
    for (int i = 1; i <= N; i++) fact[i] = fact[i-1] * i % MOD;
    invfact[N] = modpow(fact[N]);
    for (int i = N; i > 0; i--) invfact[i-1] = invfact[i] * i % MOD;

    // sum of indices total
    ll totalIdx = (ll)N * (N+1) / 2 % MOD;
    ll inv2 = (MOD+1)/2;

    // group by digit length
    int maxLen = to_string(N).size();
    vector<int> c(maxLen+1);
    vector<ll> W(maxLen+1), S(maxLen+1);
    ll p10 = 1;
    for (int d = 1; d <= maxLen; d++) {
        p10 = p10 * 10 % MOD;
        W[d] = p10; // 10^d
        int lo = (int)pow(10, d-1);
        int hi = min((int)pow(10, d)-1, N);
        if (lo > N) { c[d] = 0; S[d] = 0; continue; }
        if (hi < lo) { c[d] = 0; S[d] = 0; continue; }
        c[d] = hi - lo + 1;
        ll cnt = c[d];
        ll sum = ( (ll)lo + hi ) % MOD * cnt % MOD * inv2 % MOD;
        S[d] = sum;
    }

    // build P_d and Q_d
    vector<vector<ll>> P(maxLen+1), Q(maxLen+1);
    for (int d = 1; d <= maxLen; d++) {
        int cd = c[d];
        if (cd == 0) {
            P[d] = {1};
            Q[d] = {0};
            continue;
        }
        vector<ll> Wp(cd+1);
        Wp[0] = 1;
        for (int i = 1; i <= cd; i++) Wp[i] = Wp[i-1] * W[d] % MOD;
        P[d].assign(cd+1,0);
        for (int s = 0; s <= cd; s++) {
            P[d][s] = fact[cd] * invfact[s] % MOD * invfact[cd-s] % MOD * Wp[s] % MOD;
        }
        Q[d].assign(cd+1,0);
        for (int s = 1; s <= cd; s++) {
            ll ways = fact[cd-1] * invfact[s-1] % MOD * invfact[cd-s] % MOD;
            Q[d][s] = Wp[s] * ways % MOD * S[d] % MOD;
        }
    }

    // prefix and suffix products of P_d
    vector<vector<ll>> pre(maxLen+1), suf(maxLen+2);
    pre[0] = {1};
    for (int d = 1; d <= maxLen; d++) {
        pre[d] = convolution(pre[d-1], P[d], N+1);
    }
    suf[maxLen+1] = {1};
    for (int d = maxLen; d >= 1; d--) {
        suf[d] = convolution(P[d], suf[d+1], N+1);
    }

    // A poly
    vector<ll> A = pre[maxLen]; // size N+1

    // B poly accumulation
    vector<ll> B(N, 0);
    for (int d = 1; d <= maxLen; d++) {
        // R_d = pre[d-1] * suf[d+1]
        vector<ll> Rd = convolution(pre[d-1], suf[d+1], N+1);
        // B_d = Q_d * R_d
        vector<ll> Bd = convolution(Q[d], Rd, N+1);
        int lim = min((int)Bd.size(), N);
        for (int i = 0; i < lim; i++) {
            B[i] = (B[i] + Bd[i]) % MOD;
        }
    }

    // final compute
    ll ans = 0;
    for (int m = 0; m <= N-1; m++) {
        ll ways = fact[m] * fact[N-1-m] % MOD;
        ll val = (A[m] * totalIdx % MOD - B[m] + MOD) % MOD;
        ans = (ans + val * ways) % MOD;
    }
    cout << ans << "\n";
    return 0;
}