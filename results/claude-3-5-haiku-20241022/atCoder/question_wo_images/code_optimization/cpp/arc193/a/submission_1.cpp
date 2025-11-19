#include <bits/stdc++.h>
using namespace std;
using ll=long long;

void update(vector<ll> &data, int n, int id, ll x){
    id+=n-1;
    data[id]=min(data[id], x);
    while(id>1){
        id/=2;
        data[id]=min(data[2*id], data[2*id+1]);
    }
}

ll query(const vector<ll>& data, int n, int l, int r){
    l+=n-1;
    r+=n-1;
    ll lres=1e18;
    ll rres=1e18;
    while(r>l){
        if(l&1){
            lres=min(lres, data[l]);
            l++;
        }
        if(r&1){
            r--;
            rres=min(rres, data[r]);
        }
        l/=2;
        r/=2;
    }
    return min(lres, rres);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N;
    cin >> N;
    vector<ll> W(N+1);
    for(int i=1;i<=N;i++){
        cin >> W[i];
    }
    vector<int> L(N+1), R(N+1);
    vector<vector<pair<int, int>>> T(2*N+1);
    for(int i=1;i<=N;i++){
        cin >> L[i] >> R[i];
        T[L[i]].push_back({R[i], i});
    }
    vector<ll> data(4*N, 1e18);
    int Q;
    cin >> Q;
    vector<int> S(Q), U(Q);
    vector<ll> ans(Q, -1);
    vector<array<ll, 5>> cost(Q);
    for(int i=0;i<Q;i++){
        cost[i].fill(1e18);
    }
    vector<vector<pair<int, pair<int, int>>>> X(2*N+1);
    for(int i=0;i<Q;i++){
        cin >> S[i] >> U[i];
        if(L[S[i]]>L[U[i]]){
            swap(S[i], U[i]);
        }
        if(L[U[i]]>R[S[i]]){
            ans[i]=W[S[i]]+W[U[i]];
        }else{
            X[1].push_back({L[S[i]], {i, 0}});
            X[L[S[i]]].push_back({L[U[i]], {i, 1}});
            X[L[U[i]]].push_back({min(R[U[i]], R[S[i]])+1, {i, 2}});
            X[min(R[S[i]], R[U[i]])+1].push_back({max(R[U[i]], R[S[i]])+1, {i, 3}});
            X[max(R[S[i]], R[U[i]])+1].push_back({2*N+1, {i, 4}});
        }
    }
    for(int i=2*N;i>0;i--){
        for(auto& x:T[i]){
            update(data, 2*N, x.first, W[x.second]);
        }
        for(auto& x:X[i]){
            cost[x.second.first][x.second.second]=query(data, 2*N, i, x.first);
        }
    }
    
    for(int i=0;i<Q;i++){
        if(ans[i]<0){
            array<ll, 7> dist;
            dist.fill(1e18);
            array<bool, 7> seen = {};
            priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> q;
            dist[5]=W[S[i]];
            q.push({dist[5], 5});
            
            while(!q.empty()){
                auto [d, p] = q.top();
                q.pop();
                if(seen[p]) continue;
                seen[p]=true;
                
                if(p==5){
                    if(!seen[0] && dist[0]>d+cost[i][0]){
                        dist[0]=d+cost[i][0];
                        q.push({dist[0], 0});
                    }
                    if(!seen[3] && dist[3]>d+cost[i][3]){
                        dist[3]=d+cost[i][3];
                        q.push({dist[3], 3});
                    }
                    if(!seen[4] && dist[4]>d+cost[i][4]){
                        dist[4]=d+cost[i][4];
                        q.push({dist[4], 4});
                    }
                }
                if(p==0 || p==1 || p==4){
                    if(!seen[6] && dist[6]>d+W[U[i]]){
                        dist[6]=d+W[U[i]];
                        q.push({dist[6], 6});
                    }
                }
                if(p<5){
                    for(int j=0;j<5;j++){
                        if(p!=j && !seen[j] && dist[j]>d+cost[i][j]){
                            dist[j]=d+cost[i][j];
                            q.push({dist[j], j});
                        }
                    }
                }
            }
            ans[i] = (dist[6]>=1e18) ? -1 : dist[6];
        }
    }
    for(int i=0;i<Q;i++){
        cout << ans[i] << '\n';
    }
}