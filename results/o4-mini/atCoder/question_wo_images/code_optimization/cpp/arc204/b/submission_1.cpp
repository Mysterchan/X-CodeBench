#include <bits/stdc++.h>
using namespace std;
using short_t = short;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N,K;
    cin>>N>>K;
    int NK = N*K;
    vector<int> P(NK);
    for(int i=0;i<NK;i++){
        cin>>P[i];
        --P[i];
    }
    vector<bool> seen(NK,false);
    long long ans = 0;
    vector<int> cycle;
    vector<vector<int>> pos(N); // will reuse for residues in cycle
    for(int i=0;i<NK;i++){
        if(seen[i]) continue;
        // build cycle starting at i
        cycle.clear();
        int j=i;
        while(!seen[j]){
            seen[j]=true;
            cycle.push_back(j);
            j = P[j];
        }
        int M = cycle.size();
        if(M<=1) continue;
        // build residue sequence and positions per residue
        vector<int> res(M);
        for(int idx=0;idx<M;idx++){
            int r = cycle[idx] % N;
            res[idx]=r;
        }
        // build pos lists
        for(int idx=0;idx<M;idx++){
            pos[res[idx]].push_back(idx);
        }
        // dp[l*M + r] stores dp[l][r] for 0<=l<=r<M
        int MM = M;
        // allocate dp flat
        vector<short_t> dp((size_t)MM*(size_t)MM, 0);
        // dp[r][r] = 0 already
        for(int r=0;r<MM;r++){
            // for l=r-1 down to 0
            int rr = r;
            for(int l=r-1;l>=0;l--){
                short_t best = dp[l*MM + (rr-1)]; // dp[l][r-1]
                int rres = res[rr];
                // iterate k in pos[rres] where l<=k<r
                auto &vec = pos[rres];
                for(int t=0,ts=vec.size();t<ts;t++){
                    int k = vec[t];
                    if(k<l || k>=rr) continue;
                    // match (k, r)
                    short_t cur = 1;
                    if(k-1 >= l){
                        cur += dp[l*MM + (k-1)];
                    }
                    if(k+1 <= rr-1){
                        cur += dp[(k+1)*MM + (rr-1)];
                    }
                    if(cur>best) best=cur;
                }
                dp[l*MM + rr] = best;
            }
        }
        short_t cyc_best = dp[0*MM + (MM-1)];
        // handle circular match across boundary: pair (0,k)
        int r0 = res[0];
        auto &v0 = pos[r0];
        for(int t=0,ts=v0.size();t<ts;t++){
            int k = v0[t];
            if(k<=0 || k>=MM) continue;
            // consider matching (0,k)
            short_t cur = 1;
            if(1 <= k-1){
                cur += dp[1*MM + (k-1)];
            }
            if(k+1 <= MM-1){
                cur += dp[(k+1)*MM + (MM-1)];
            }
            if(cur>cyc_best) cyc_best=cur;
        }
        ans += cyc_best;
        // clear pos lists
        for(int idx=0;idx<M;idx++){
            pos[res[idx]].clear();
        }
    }
    cout<<ans<<"\n";
    return 0;
}