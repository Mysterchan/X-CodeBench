#include<bits/stdc++.h>
#define IOS ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
#define endl '\n' 
#define en ' '
using namespace std;
using LL=long long;
const LL mod=1e9+7;
const int N=2e5+10;
int n;
vector<int> dis(N);

pair<int, int> bfs(int root, vector<vector<int>> arr){
    queue<int> q;
    vector<int> vis(n + 1);
    for(int i = 1; i <= n; i++)
        dis[i] = 0, vis[i] = -1;
    q.push(root);
    vis[root] = 1;
    dis[root] = 0;
    int far = root;

    while(!q.empty())
    {
        int dot = q.front();
        q.pop();
        for(auto it : arr[dot])
        {
            if(vis[it] != -1)
                continue;
            vis[it] = 1;
            dis[it] = dis[dot] + 1;
            q.push(it);
            if(dis[it] > dis[far] || dis[it] == dis[far] && it > far)
                far = it;
        }
    }
    return {far, dis[far]};
}

void hxy(){
    cin >> n;
    vector<vector<int>> arr(n + 1);
    for(int i = 1; i < n; i++)
    {
        int u, v;
        cin >> u >> v;
        arr[u].push_back(v);
        arr[v].push_back(u);
    }
    int firstdot = bfs(1, arr).first;
    int distance = bfs(firstdot, arr).second;

    if(distance == 2 || distance == 1)
    {
        cout << 0 << endl;
        return;
    }
    if(distance == n - 1)
    {
        cout << 1 << endl;
        return;
    }
    int maxx = 0;
    for(int i = 1; i <= n; i++)
    {
        int len = arr[i].size();
        maxx = max(maxx, len);
    }
    cout << maxx << endl;


}

int main()
{
    int t = 1;
    cin >> t;
    while(t--)
    {
        hxy();
    }

    return 0;
}