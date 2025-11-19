#include <bits/stdc++.h>
using namespace std;

const uint32_t MOD = 998244353;
const uint32_t G   = 3;

uint32_t mod_pow(uint32_t a, uint32_t e){
    uint64_t r=1, x=a;
    while(e){
        if(e&1) r=r*x%MOD;
        x=x*x%MOD;
        e>>=1;
    }
    return (uint32_t)r;
}

namespace NTT {
    void ntt(vector<uint32_t>& a, bool invert){
        int n = (int)a.size();
        static vector<int> rev;
        static vector<uint32_t> roots{0,1};
        if((int)rev.size()!=n){
            int k = __builtin_ctz(n);
            rev.assign(n,0);
            for(int i=0;i<n;i++){
                rev[i]=(rev[i>>1]>>1)|((i&1)<<(k-1));
            }
        }
        if((int)roots.size()<n){
            int k = __builtin_ctz(roots.size());
            roots.resize(n);
            while((1<<k)<n){
                uint32_t z = mod_pow(G,(MOD-1)>>(k+1));
                for(int i=1<<(k-1); i<(1<<k); ++i){
                    roots[2*i]=roots[i];
                    roots[2*i+1]=(uint64_t)roots[i]*z%MOD;
                }
                ++k;
            }
        }
        for(int i=0;i<n;i++){
            if(i<rev[i]) swap(a[i],a[rev[i]]);
        }
        for(int len=1; len<n; len<<=1){
            for(int i=0;i<n;i+=2*len){
                for(int j=0;j<len;j++){
                    uint32_t u=a[i+j];
                    uint32_t v=(uint64_t)a[i+j+len]*roots[len+j]%MOD;
                    uint32_t x=u+v; if(x>=MOD) x-=MOD;
                    uint32_t y=u+MOD-v; if(y>=MOD) y-=MOD;
                    a[i+j]=x; a[i+j+len]=y;
                }
            }
        }
        if(invert){
            reverse(a.begin()+1,a.end());
            uint32_t inv_n = mod_pow(n, MOD-2);
            for(uint32_t &x:a) x=(uint64_t)x*inv_n%MOD;
        }
    }

    vector<uint32_t> multiply(vector<uint32_t> a, vector<uint32_t> b){
        int n=1;
        while(n < (int)a.size()+(int)b.size()-1) n<<=1;
        a.resize(n); b.resize(n);
        ntt(a,false); ntt(b,false);
        for(int i=0;i<n;i++) a[i]=(uint64_t)a[i]*b[i]%MOD;
        ntt(a,true);
        a.resize(min(n, (int)a.size()));
        while(!a.empty() && a.back()==0) a.pop_back();
        return a;
    }
}

vector<uint32_t> binom_poly(int cnt, uint32_t t, const vector<uint32_t>& fact, const vector<uint32_t>& invfact){
    vector<uint32_t> p(cnt+1);
    for(int r=0;r<=cnt;r++){
        uint32_t comb = (uint64_t)fact[cnt]*invfact[r]%MOD * invfact[cnt-r]%MOD;
        uint32_t powt = mod_pow(t, r);
        p[r] = (uint64_t)comb * powt % MOD;
    }
    return p;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N; 
    if(!(cin>>N)) return 0;

    auto digits = [](int x){ int d=0; while(x){ d++; x/=10; } return max(1,d); };
    const int DMAX = digits(N);
    vector<long long> cnt(DMAX+1,0);
    vector<uint32_t> sum_by_len(DMAX+1,0);

    for(int d=1; d<=DMAX; ++d){
        long long lo = (d==1?1: (long long)pow(10,d-1));
        long long hi = min<long long>(N, (long long)pow(10,d)-1);
        if(lo>hi) continue;
        long long c = hi - lo + 1;
        cnt[d]=c;
        long long s = ( (__int128)(lo+hi) % MOD ) * ( ( (__int128)c % MOD ) ) % MOD;
        s = s * ((MOD+1)/2) % MOD;
        sum_by_len[d] = (uint32_t)s;
    }

    vector<uint32_t> fact(N+1,1), invfact(N+1,1);
    for(int i=1;i<=N;i++) fact[i]=(uint64_t)fact[i-1]*i%MOD;
    invfact[N]=mod_pow(fact[N], MOD-2);
    for(int i=N;i>0;i--) invfact[i-1]=(uint64_t)invfact[i]*i%MOD;

    vector<uint32_t> t(DMAX+1,1);
    for(int d=1; d<=DMAX; ++d) t[d]=mod_pow(10,d);

    vector<uint32_t> G = {1};
    for(int d=1; d<=DMAX; ++d){
        if(cnt[d]==0) continue;
        auto poly = binom_poly((int)cnt[d], t[d], fact, invfact); // degree cnt[d]
        G = NTT::multiply(G, poly);
        if((int)G.size() > N) G.resize(N+1); // degree at most N
    }
    if((int)G.size() < N) G.resize(N+1, 0);

    vector<uint32_t> w(N,0);
    for(int k=0; k<=N-1; ++k){
        uint32_t wk = (uint64_t)fact[k] * fact[N-1-k] % MOD;
        w[k]=wk;
    }

    uint64_t answer = 0;

    for(int L=1; L<=DMAX; ++L){
        if(cnt[L]==0) continue;
        vector<uint32_t> F(N,0);
        F[0] = G[0];
        for(int k=1; k<=N-1; ++k){
            uint32_t val = G[k];
            uint32_t sub = (uint64_t)t[L] * F[k-1] % MOD;
            uint32_t fk = val >= sub ? val - sub : val + MOD - sub;
            F[k]=fk;
        }

        uint64_t ML = 0;
        for(int k=0; k<=N-1; ++k){
            ML += (uint64_t)w[k] * F[k] % MOD;
            if(ML >= (uint64_t)MOD) ML -= MOD;
        }

        answer += ML * sum_by_len[L] % MOD;
        if(answer >= MOD) answer -= MOD;
    }

    cout << (uint32_t)answer << "\n";
    return 0;
}
