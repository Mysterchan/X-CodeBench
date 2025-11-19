#include<iostream>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<map>
#include<set>
#include<vector>
#include<queue>
using namespace std;
#define x first
#define y second
typedef long long ll;
typedef pair<ll, ll> PII;
const int N = 2e5 + 10;
vector<PII> p[N];
ll v[N], d[N], f[N];
ll n, m, x, mi = 2e18, w;

void dfs(int u, int z)
{
    if(u == n)
    {
        mi = min(mi, w);
        return ;
    }

    for(auto &c : p[u])
        if(!v[c.x])
        {
            v[c.x] = 1;
            w ++ ;
            if(c.y != z) w += x;

            dfs(c.x, c.y);
            
            v[c.x] = 0;
            w -- ;
            if(c.y != z) w -= x;
            
        }
}

int main()
{
    cin.tie(0), cout.tie(0), ios::sync_with_stdio(false);
    
    cin >> n >> m >> x;
    while(m -- )
    {
        int u, v;
        cin >> u >> v;
        p[u].push_back({v, 0});
        p[v].push_back({u, 1});
    }

    dfs(1, 0);
    cout << mi;

    return 0;
}