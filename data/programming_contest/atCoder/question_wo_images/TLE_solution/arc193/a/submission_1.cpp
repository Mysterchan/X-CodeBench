#include <bits/stdc++.h>
using namespace std;
using ll=long long;
using edge=pair<int, ll>;
            using cur=pair<ll, int>;
            
void update(vector<ll> &data, int n, int id, ll x){
    id+=n-1;
    data[id]=min(data[id], x);
    while(id>1){
        id/=2;
        data[id]=min(data[2*id], data[2*id+1]);
    }
}
ll query(vector<ll> data, int n, int l, int r){
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
    vector<vector<ll>> cost(Q, vector<ll> (5, 1e18));
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
        for(pair<int, int> x:T[i]){
            int r=x.first;
            int id=x.second;
            update(data, 2*N, r, W[id]);
        }
        for(pair<int, pair<int, int>> x:X[i]){
            int r=x.first;
            int id=x.second.first;
            int t=x.second.second;
            cost[id][t]=query(data, 2*N, i, r);
        }
    }
    for(int i=0;i<Q;i++){
        if(ans[i]<0){
            vector<vector<edge>> G(7);
            G[5].push_back({0, cost[i][0]});
            G[5].push_back({3, cost[i][3]});
            G[5].push_back({4, cost[i][4]});
            G[0].push_back({6, W[U[i]]});
            G[1].push_back({6, W[U[i]]});
            G[4].push_back({6, W[U[i]]});
            for(int k=0;k<5;k++){
                for(int j=0;j<5;j++){
                    if(k==j){
                        continue;
                    }
                    G[k].push_back({j, cost[i][j]});
                }
            }
            vector<ll> dist(7, 1e18);
            vector<bool> seen(7, false);
            priority_queue<cur, vector<cur>, greater<cur>> q;
            dist[5]=W[S[i]];
            q.push({dist[5], 5});
            while(!q.empty()){
                int p=q.top().second;
                q.pop();
                if(seen[p]){
                    continue;
                }
                seen[p]=true;
                for(edge e:G[p]){
                    int n=e.first;
                    ll c=e.second;
                    if(seen[n]){
                        continue;
                    }
                    if(dist[n]>dist[p]+c){
                        dist[n]=dist[p]+c;
                        q.push({dist[n], n});
                    }
                }
            }
            if(dist[6]>=1e18){
                ans[i]=-1;
            }else{
                ans[i]=dist[6];
            }
        }
    }
    for(int i=0;i<Q;i++){
        cout << ans[i] << '\n';
    }
}
