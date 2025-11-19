#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;
    string A;
    cin >> A;
    int L = 1;
    for(int i = 0; i < N; i++) L *= 3;
    // A should have length L
    vector<int> dp0(L), dp1(L);
    for(int i = 0; i < L; i++){
        char c = A[i];
        dp0[i] = (c == '0' ? 0 : 1);
        dp1[i] = (c == '1' ? 0 : 1);
    }
    // Build levels bottom-up
    for(int level = N; level > 0; level--){
        int prevL = L;
        L /= 3;
        vector<int> ndp0(L), ndp1(L);
        int idx = 0;
        for(int i = 0; i < prevL; i += 3){
            // children at i, i+1, i+2
            int c0_0 = dp0[i],   c0_1 = dp1[i];
            int c1_0 = dp0[i+1], c1_1 = dp1[i+1];
            int c2_0 = dp0[i+2], c2_1 = dp1[i+2];
            // compute dp1 for this node
            int sum1 = c0_1 + c1_1 + c2_1;
            int d0 = c0_1 - c0_0;
            int d1 = c1_1 - c1_0;
            int d2 = c2_1 - c2_0;
            int maxd = d0;
            if(d1 > maxd) maxd = d1;
            if(d2 > maxd) maxd = d2;
            if(maxd < 0) maxd = 0;
            ndp1[idx] = sum1 - maxd;
            // compute dp0 for this node
            int sum0 = c0_0 + c1_0 + c2_0;
            int e0 = c0_0 - c0_1;
            int e1 = c1_0 - c1_1;
            int e2 = c2_0 - c2_1;
            int maxe = e0;
            if(e1 > maxe) maxe = e1;
            if(e2 > maxe) maxe = e2;
            if(maxe < 0) maxe = 0;
            ndp0[idx] = sum0 - maxe;
            idx++;
        }
        dp0.swap(ndp0);
        dp1.swap(ndp1);
    }
    // At root
    int cost0 = dp0[0], cost1 = dp1[0];
    // original output is the one with zero cost
    int ans = (cost0 == 0 ? cost1 : cost0);
    cout << ans;
    return 0;
}