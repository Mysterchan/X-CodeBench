#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll NEG_INF = -(1LL<<60);

int N;
vector<vector<int>> adj;
vector<int> parent_node;
vector<ll> dp3down, dp3up;

void dfs1(int u, int p){
    parent_node[u] = p;
    vector<ll> gains;
    for(int v: adj[u]){
        if(v == p) continue;
        dfs1(v, u);
        ll g = dp3down[v] >= 1 ? dp3down[v] : 1;
        gains.push_back(g);
    }
    if((int)gains.size() < 3){
        dp3down[u] = NEG_INF;
    } else {
        // get top 3
        nth_element(gains.begin(), gains.begin()+2, gains.end(), greater<ll>());
        ll sum = gains[0] + gains[1] + gains[2];
        // but ensure these are the actual top3
        // sort first three if needed
        if(gains.size() > 3){
            // to guarantee correctness, sort the first 3
            sort(gains.begin(), gains.begin()+3, greater<ll>());
        } else {
            sort(gains.begin(), gains.end(), greater<ll>());
        }
        dp3down[u] = 1 + sum;
    }
}

void dfs2(int u, int p){
    // build gains list for u from all neighbors
    int deg = adj[u].size();
    vector<pair<ll,int>> gl;
    gl.reserve(deg);
    for(int v: adj[u]){
        ll gv;
        if(v == p){
            gv = dp3up[u] >= 1 ? dp3up[u] : 1;
        } else {
            gv = dp3down[v] >= 1 ? dp3down[v] : 1;
        }
        gl.emplace_back(gv, v);
    }
    int M = gl.size();
    // sort descending by gain
    sort(gl.begin(), gl.end(), [](const pair<ll,int>& a, const pair<ll,int>& b){
        return a.first > b.first;
    });
    // precompute sum_top3 and sum_top4
    ll sum3 = 0, sum4 = 0;
    if(M >= 3){
        sum3 = gl[0].first + gl[1].first + gl[2].first;
    }
    if(M >= 4){
        sum4 = sum3 + gl[3].first;
    }
    // propagate dp3up to children
    for(int v: adj[u]){
        if(v == p) continue;
        // dp3up[v] = dp3dir[u][v]
        if(M - 1 < 3){
            dp3up[v] = NEG_INF;
        } else {
            // find if v is among top3 of gl
            bool in_top3 = false;
            ll gv = 0;
            for(int k = 0; k < 3; k++){
                if(gl[k].second == v){
                    in_top3 = true;
                    gv = gl[k].first;
                    break;
                }
            }
            if(!in_top3){
                // excluding v does not affect top3
                dp3up[v] = 1 + sum3;
            } else {
                // v is in top3; need to use 4th element
                // sum_top4 - gv
                dp3up[v] = 1 + (sum4 - gv);
            }
        }
        dfs2(v, u);
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    adj.assign(N, vector<int>());
    for(int i = 0; i < N-1; i++){
        int a, b;
        cin >> a >> b;
        --a; --b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    parent_node.assign(N, -1);
    dp3down.assign(N, NEG_INF);
    dp3up.assign(N, NEG_INF);
    // root tree at 0
    dfs1(0, -1);
    dp3up[0] = NEG_INF;
    dfs2(0, -1);
    // compute dp4 for each node
    ll ans = NEG_INF;
    for(int u = 0; u < N; u++){
        int deg = adj[u].size();
        if(deg < 4) continue;
        // find top 4 gains among neighbors
        ll best[4] = {0,0,0,0};
        for(int v: adj[u]){
            ll gv;
            if(v == parent_node[u]){
                gv = dp3up[u] >= 1 ? dp3up[u] : 1;
            } else {
                gv = dp3down[v] >= 1 ? dp3down[v] : 1;
            }
            // insert into best
            if(gv > best[0]){
                best[3] = best[2];
                best[2] = best[1];
                best[1] = best[0];
                best[0] = gv;
            } else if(gv > best[1]){
                best[3] = best[2];
                best[2] = best[1];
                best[1] = gv;
            } else if(gv > best[2]){
                best[3] = best[2];
                best[2] = gv;
            } else if(gv > best[3]){
                best[3] = gv;
            }
        }
        ll sum4 = best[0] + best[1] + best[2] + best[3];
        ll dp4 = 1 + sum4;
        ans = max(ans, dp4);
    }
    if(ans < 5) cout << -1 << "\n";
    else cout << ans << "\n";
    return 0;
}