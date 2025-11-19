#include <bits/stdc++.h>
using namespace std;

static const int MOD = 998244353;
static const int G   = 3;

// fast exponentiation mod
int modpow(int x, int e){
    long long res = 1, base = x;
    while(e){
        if(e & 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        e >>= 1;
    }
    return int(res);
}

// in-place iterative NTT
void ntt(vector<int> & a, bool invert){
    int n = (int)a.size();
    static vector<int> rev;
    static vector<int> roots{0,1};
    if((int)rev.size() != n){
        int k = __builtin_ctz(n);
        rev.assign(n,0);
        for(int i = 0; i < n; i++){
            rev[i] = (rev[i>>1] >> 1) | ((i&1) << (k-1));
        }
    }
    if((int)roots.size() < n){
        // compute roots of unity 
        roots.resize(n);
        for(int len = roots.size()/2; len < n; len <<= 1){
            int e = modpow(G, (MOD-1) / (len<<1));
            for(int i = len; i < (len<<1); i++){
                if(i & 1) roots[i] = int((1LL * roots[i-1] * e) % MOD);
                else       roots[i] = roots[i>>1];
            }
        }
    }
    for(int i = 0; i < n; i++){
        if(i < rev[i]) swap(a[i], a[rev[i]]);
    }
    for(int len = 1; len < n; len <<= 1){
        for(int i = 0; i < n; i += (len << 1)){
            for(int j = 0; j < len; j++){
                int u = a[i+j];
                int v = int((1LL * a[i+j+len] * roots[len+j]) % MOD);
                int x = u + v;
                if(x >= MOD) x -= MOD;
                int y = u - v;
                if(y < 0) y += MOD;
                a[i+j]     = x;
                a[i+j+len] = y;
            }
        }
    }
    if(invert){
        int inv_n = modpow(n, MOD-2);
        for(int & x: a) x = int((1LL * x * inv_n) % MOD);
        reverse(a.begin()+1, a.end());
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if(!(cin >> N)){
        cout << 0 << "\n";
        return 0;
    }
    vector<int> S(N);
    int mx = 0;
    for(int i = 0; i < N; i++){
        cin >> S[i];
        if(S[i] > mx) mx = S[i];
    }
    if(N < 3){
        cout << 0 << "\n";
        return 0;
    }
    int lim = 1;
    while(lim <= 2 * mx) lim <<= 1;

    vector<int> a(lim, 0);
    for(int x: S){
        a[x] = 1;
    }

    ntt(a, false);
    for(int i = 0; i < lim; i++){
        a[i] = int((1LL * a[i] * a[i]) % MOD);
    }
    ntt(a, true);

    long long total = 0;
    for(int b: S){
        int k = 2 * b;
        if(k < lim){
            // a[k] = number of ordered pairs (A,C) with A+C = 2b
            // subtract the (b,b) pair, then divide by 2
            int cnt = (a[k] + MOD - 1) % MOD;
            total += cnt / 2;
        }
    }
    cout << total << "\n";
    return 0;
}