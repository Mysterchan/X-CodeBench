#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int MAXN = 200000 + 5;
ll a[MAXN];
int Lf[MAXN], Rt[MAXN];
bool alive[MAXN];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    // total sum of N <= 2e5
    while(T--){
        int N;
        cin >> N;
        for(int i = 1; i <= N; i++){
            cin >> a[i];
            alive[i] = true;
            Lf[i] = (i == 1 ? 0 : i - 1);
            Rt[i] = (i == N ? 0 : i + 1);
        }
        if(N <= 1){
            cout << 0 << "\n";
            continue;
        }
        // min-heap of (value, index)
        priority_queue<pair<ll,int>, vector<pair<ll,int>>, greater<pair<ll,int>>> pq;
        for(int i = 1; i <= N; i++){
            pq.push({a[i], i});
        }
        ll ans = 0;
        int alive_cnt = N;
        while(alive_cnt > 1){
            auto cur = pq.top();
            pq.pop();
            ll val = cur.first;
            int idx = cur.second;
            if(!alive[idx] || a[idx] != val) continue;
            int r = Rt[idx];
            // if can merge with right neighbor
            if(r != 0 && alive[r] && a[idx] == a[r]){
                // merge idx and r
                a[idx] = a[idx] + 1;
                // remove r
                alive[r] = false;
                int rr = Rt[r];
                Rt[idx] = rr;
                if(rr != 0) Lf[rr] = idx;
                alive_cnt--;
                // reinsert updated idx
                pq.push({a[idx], idx});
            } else {
                // cannot merge, raise to min neighbor
                ll mn = LLONG_MAX;
                int l = Lf[idx];
                if(l != 0 && alive[l]) mn = min(mn, a[l]);
                if(r != 0 && alive[r]) mn = min(mn, a[r]);
                // it's guaranteed at least one neighbor exists since alive_cnt>1
                if(mn > a[idx]){
                    ans += (mn - a[idx]);
                    a[idx] = mn;
                }
                // reinsert updated
                pq.push({a[idx], idx});
            }
        }
        cout << ans << "\n";
        // no need to clear arrays beyond N, as next test will reset needed parts
    }
    return 0;
}