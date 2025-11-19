#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'
const int N = 2e5 + 5;
vector <int> g[N];
int used[N];
int n,m,k;
int X[] = {1,-1,0,0,1,-1,1,-1};
int Y[] = {0,0,1,-1,1,-1,-1,1};
int num(int x,int y)
{
    return (x - 1) * m + y;
}
signed main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin>>n>>m>>k;
    vector <int> r(k+1);
    vector <int> c(k+1);
    unordered_map <int,int> mp;
    for(int i=1;i<=k;i++)
    {
        cin>>r[i]>>c[i];
        mp[num(r[i],c[i])] = i;
    }
    for(int i=1;i<=k;i++)
    {
        for(int o=0;o<8;o++)
        {
            int tox = r[i] + X[o];
            int toy = c[i] + Y[o];
            int val = mp[num(tox,toy)];
            if(1<= tox && tox<=n && 1<=toy && toy <= m && val)
            {
                g[i].push_back(val);
            }
        }
    }
    queue <int> q;
    for(int i = 2;i <= n;i++)
    {
        int ix = mp[num(i,1)];
        if(ix)
        {
            q.push(ix);
            used[ix] = 1;
        }
    }
    for(int j = 2;j <=m;j++)
    {
        int ix = mp[num(n,j)];
        if(ix)
        {
            q.push(ix);
            used[ix] = 1;
        }
    }
    while(q.size())
    {
        int v = q.front();
        q.pop();
        for(auto u : g[v])
        {
            if(used[u])continue;
            used[u] = 1;
            q.push(u);
        }
    }
    for(int j = 2;j <= m;j++)
    {
        int ix = mp[num(1,j)];
        if(ix && used[ix])
        {
            cout<<"No";
            return 0;
        }
    }
    for(int i = 2;i < n;i++)
    {
        int ix = mp[num(i,m)];
        if(ix && used[ix])
        {
            cout<<"No";
            return 0;
        }
    }
    cout<<"Yes";
}
