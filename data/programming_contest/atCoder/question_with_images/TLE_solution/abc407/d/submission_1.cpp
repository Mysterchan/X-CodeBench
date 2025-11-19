#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main(){
    ll h,w; cin >> h >> w;
    vector<vector<ll>> a(h, vector<ll>(w));
    for(ll i = 0; i<h; i++){
        for(ll j = 0; j<w; j++){
            cin >> a[i][j];
        }
    }
    set<vector<vector<bool>>> v;
    queue<vector<vector<bool>>> q;
    vector<vector<bool>> s(h, vector<bool>(w, false));
    q.push(s);
    ll output = 0;
    while(!q.empty()){
        vector<vector<bool>> f = q.front();
        v.insert(f);
        q.pop();
        ll x = 0;
        for(ll i = 0; i<h; i++){
            for(ll j = 0; j<w; j++){
                if(!f[i][j]) x ^= a[i][j];
            }
        }
        output = max(output, x);
        vector<vector<bool>> nf = f;
        for(ll i = 0; i<h; i++){
            for(ll j = 0; j<w; j++){
                nf = f;
                if(i != h-1){
                    if(!f[i][j] && !f[i+1][j]){
                        nf[i][j] = true;
                        nf[i+1][j] = true;
                        if(v.find(nf) == v.end()) q.push(nf);
                    }
                }
                nf = f;
                if(j != w-1){
                    if(!f[i][j] && !f[i][j+1]){
                        nf[i][j] = true;
                        nf[i][j+1] = true;
                        if(v.find(nf) == v.end()) q.push(nf);
                    }
                }
            }
        }
    }
    cout << output << "\n";
}
