#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if(!(cin>>N))return 0;
    string A;
    cin>>A;
    int M = 1;
    for(int i=0;i<N;i++) M *= 3;
    // dp0[i]: cost to make subtree at i collapse to 0
    // dp1[i]: cost to make subtree at i collapse to 1
    vector<int> dp0(M), dp1(M);
    for(int i=0;i<M;i++){
        if(A[i]=='0'){
            dp0[i]=0; dp1[i]=1;
        } else {
            dp0[i]=1; dp1[i]=0;
        }
    }
    int size = M;
    vector<int> nxt0, nxt1;
    for(int level=1; level<=N; level++){
        int newSize = size/3;
        nxt0.assign(newSize, 0);
        nxt1.assign(newSize, 0);
        for(int i=0; i<newSize; i++){
            int j = i*3;
            // sum costs for s=0 and s=1
            int sum0 = dp0[j] + dp0[j+1] + dp0[j+2];
            int sum1 = dp1[j] + dp1[j+1] + dp1[j+2];
            // compute deltas for s=0: cost_ns - cost_s => dp1 - dp0
            int d0 = dp1[j]   - dp0[j];
            int d1 = dp1[j+1] - dp0[j+1];
            int d2 = dp1[j+2] - dp0[j+2];
            int minD0 = d0;
            if(d1 < minD0) minD0 = d1;
            if(d2 < minD0) minD0 = d2;
            // new cost for 0: sum0 + min(0, minD0)
            nxt0[i] = sum0 + (minD0 < 0 ? minD0 : 0);
            // deltas for s=1: cost_ns - cost_s => dp0 - dp1
            d0 = dp0[j]   - dp1[j];
            d1 = dp0[j+1] - dp1[j+1];
            d2 = dp0[j+2] - dp1[j+2];
            int minD1 = d0;
            if(d1 < minD1) minD1 = d1;
            if(d2 < minD1) minD1 = d2;
            nxt1[i] = sum1 + (minD1 < 0 ? minD1 : 0);
        }
        // swap dp and nxt
        dp0.swap(nxt0);
        dp1.swap(nxt1);
        size = newSize;
    }
    // root at index 0
    // original final bit is the one with cost 0
    int orig_bit = (dp0[0]==0 ? 0 : 1);
    int ans = (orig_bit==0 ? dp1[0] : dp0[0]);
    cout<<ans<<"\n";
    return 0;
}