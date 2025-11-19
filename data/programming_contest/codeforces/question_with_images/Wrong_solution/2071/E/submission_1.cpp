#include <bits/stdc++.h>
using namespace std;

static const int MOD = 998244353;


inline int add(int a, int b) {
    int s = a + b;
    return (s >= MOD ? s - MOD : s);
}
inline int subb(int a, int b) {
    int s = a - b;
    return (s < 0 ? s + MOD : s);
}
inline int mul(int a, int b) {
    return int(1LL * a * b % MOD);
}
int modExp(int base, int exp) {
    int result = 1;
    while(exp > 0) {
        if(exp & 1) result = mul(result, base);
        base = mul(base, base);
        exp >>= 1;
    }
    return result;
}
inline int inv(int a) {
    return modExp(a, MOD - 2);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    const int HALF = (MOD + 1) / 2;

    int t;
    cin >> t;
    while(t--){
        int n;  
        cin >> n;

        vector<int> p(n), q(n);
        for(int i = 0; i < n; i++){
            cin >> p[i] >> q[i];
        }

        vector<vector<int>> adj(n);
        for(int i = 0; i < n-1; i++){
            int u,v; 
            cin >> u >> v; 
            --u; 
            --v;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        if(n == 1){
            cout << 0 << "\n";
            continue;
        }

        vector<int> remain(n), fall(n);
        for(int i = 0; i < n; i++){
            int invQ = inv(q[i]);
            int r = subb(q[i], p[i]);
            r = mul(r, invQ);
            remain[i] = r;
            fall[i]   = subb(1, r);
        }

        vector<int> leafProb(n, 0);
        {
            for(int v=0; v<n; v++){
                int d = (int)adj[v].size();
                if(d == 0){
                    leafProb[v] = 0;
                    continue;
                }
                vector<int> prefix(d+1, 1), suffix(d+1, 1);
                for(int i=0; i<d; i++){
                    int nei = adj[v][i];
                    prefix[i+1] = mul(prefix[i], fall[nei]);
                }
                for(int i=d-1; i>=0; i--){
                    int nei = adj[v][i];
                    suffix[i] = mul(suffix[i+1], fall[nei]);
                }
                int sumOne = 0;
                for(int i=0; i<d; i++){
                    int nei = adj[v][i];
                    int val = mul(remain[nei], prefix[i]);
                    val = mul(val, suffix[i+1]);
                    sumOne = add(sumOne, val);
                }
                leafProb[v] = mul(remain[v], sumOne);
            }
        }

        long long Lll = 0, Sll = 0;  // to avoid accidental overflow
        for(int v=0; v<n; v++){
            Lll = (Lll + leafProb[v]) % MOD;
            Sll = (Sll + 1LL*leafProb[v]*leafProb[v]) % MOD;
        }
        int L = int(Lll), S = int(Sll);

        {
            long long L2 = (1LL*L*L) % MOD;
            long long diff = (L2 - S) % MOD;
            if(diff < 0) diff += MOD;
            long long tmp = (diff * HALF) % MOD;  // multiply by 1/2
            L = int(tmp);
        }
        int baseSum = L;  // reuse L as an int

        long long sumCorrections = 0;

        vector<int> prodFall(n, 1);
        {
            for(int v=0; v<n; v++){
                long long pr = 1;
                for(int nei: adj[v]){
                    pr = (pr * fall[nei]) % MOD;
                }
                prodFall[v] = (int)pr;
            }
        }

        for(int u=0; u<n; u++){
            for(int v: adj[u]){
                if(v < u) continue;  // handle each edge once
                long long pBoth = 1LL*remain[u]*remain[v] % MOD;
                {
                    long long x = 1LL*prodFall[u] * inv(fall[v]) % MOD;
                    pBoth = (pBoth * x) % MOD;
                }
                {
                    long long x = 1LL*prodFall[v] * inv(fall[u]) % MOD;
                    pBoth = (pBoth * x) % MOD;
                }
                long long pProd = 1LL*leafProb[u]*leafProb[v] % MOD;
                long long delta = pBoth - pProd;
                delta %= MOD; 
                if(delta < 0) delta += MOD;
                sumCorrections = (sumCorrections + delta) % MOD;
            }
        }


        vector<int> invFall(n);
        for(int i=0; i<n; i++){
            invFall[i] = inv(fall[i]);
        }


        for(int w=0; w<n; w++){
            int degw = (int)adj[w].size();
            if(degw < 2) continue; // no pairs among neighbors

            for(int i=0; i<degw; i++){
                int u = adj[w][i];
                for(int j=i+1; j<degw; j++){
                    int v = adj[w][j];
                    long long pBoth = 1LL * remain[u] * remain[v] % MOD;
                    pBoth = (pBoth * remain[w]) % MOD;
                    {
                        long long part = 1LL*prodFall[u]*prodFall[v] % MOD;
                        part = (part * 1LL*invFall[w] * invFall[w]) % MOD; // multiply by invFall[w]^2
                        pBoth = (pBoth * part) % MOD;
                    }
                    long long pProd = 1LL*leafProb[u]*leafProb[v] % MOD;
                    long long delta = pBoth - pProd;
                    delta %= MOD; 
                    if(delta < 0) delta += MOD;
                    sumCorrections = (sumCorrections + delta) % MOD;

                }
            }
        }

        long long ans = baseSum;
        ans = (ans + sumCorrections) % MOD;
        if(ans < 0) ans += MOD;
        cout << ans << "\n";
    }

    return 0;
}
