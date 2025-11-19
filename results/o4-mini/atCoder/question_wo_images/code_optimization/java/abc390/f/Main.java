#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if(!(cin >> N)) return 0;
    vector<int> A(N+1);
    int maxA = 0;
    for(int i = 1; i <= N; i++){
        cin >> A[i];
        if(A[i] > maxA) maxA = A[i];
    }
    int maxV = maxA + 1;
    vector<vector<int>> pos(maxV+2);
    // pos[0] stays empty
    for(int i = 1; i <= N; i++){
        int v = A[i];
        pos[v].push_back(i);
    }
    ll ans = 0;
    // process v from 1 to maxV
    for(int v = 1; v <= maxV; v++){
        // skip if neither v nor v-1 appear
        if(pos[v].empty() && (v-1 >= 0 && pos[v-1].empty())) continue;
        // p = positions of v, q = positions of v-1
        const vector<int> &p = pos[v];
        const vector<int> &q = pos[v-1];
        int m = p.size();
        int ptr = 0;
        // iterate over segments defined by q
        int qsz = q.size();
        for(int j = 0; j <= qsz; j++){
            int L = (j==0 ? 1 : q[j-1] + 1);
            int R = (j==qsz ? N : q[j] - 1);
            if(L > R) continue;
            ll len = (ll)R - (ll)L + 1;
            ll segTotal = len * (len + 1) / 2;  // total subarrays in [L,R]
            // compute subarrays without any p in [L,R]
            // advance ptr to first p[ptr] >= L
            while(ptr < m && p[ptr] < L) ptr++;
            ll no_p = 0;
            int prev = L;
            // for each p in segment
            int startPtr = ptr;
            while(ptr < m && p[ptr] <= R){
                int pi = p[ptr];
                ll a = (ll)pi - prev;
                no_p += a * (a + 1) / 2;
                prev = pi + 1;
                ptr++;
            }
            // tail gap
            ll a = (ll)R - prev + 1;
            if(a > 0) no_p += a * (a + 1) / 2;
            // subarrays containing at least one p and no q
            ans += (segTotal - no_p);
        }
    }
    cout << ans << "\n";
    return 0;
}