#include <bits/stdc++.h>

using namespace std;

#define fastIO                   \
    ios::sync_with_stdio(false); \
    cin.tie(NULL);               \
    cout.tie(NULL);              \
    cout.precision(numeric_limits<double>::max_digits10);

vector<vector<int>> adj;
vector<int> res, arr;
int odd, even;

void dfs(int node, int parent, int level){
    int pre_odd = odd;
    int pre_even = even;

    if(level & 1){
        odd += arr[node];
        even = max(0, even - arr[node]);
        res[node] = odd;
    }
    else{
        odd = max(0, odd - arr[node]);
        even += arr[node];
        res[node] = even;
    }

    for(auto child : adj[node]){
        if(child != parent){
            dfs(child, node, level + 1);
        }
    }

    odd = pre_odd;
    even = pre_even;
}

int main()
{
int t;
cin >> t;
while(t--){
    int n;
    cin >> n;
    arr.resize(n);
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }

    odd = 0, even = 0;
    adj.assign(n, {});
    res.resize(n);
    for(int i = 0; i < n - 1; i++){
        int u, v;
        cin >> u >> v;
        u--, v--;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(0, -1, 0);

    for(auto it : res){
        cout << it << " ";
    }
    cout << endl;

}
    return 0;
}