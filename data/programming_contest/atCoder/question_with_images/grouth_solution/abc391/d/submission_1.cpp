#include<bits/stdc++.h>
using namespace std;
#define lowbit(x) (x & -x)
#define int long long

vector<vector<pair<int,int>>> G;
int INF = 1e18;
signed main(){
    ios_base::sync_with_stdio(0);cin.tie(0);
    int n,w;
    cin >> n >> w;
    G.resize(w+1);
    vector<int> tout(n+1,INF),last(w+1);
    int timer = 0;
    for (int i = 1; i <=n; i++)
    {
        int x,y;
        cin >> x >> y;
        G[x].push_back({ y,i });
    }
    for (int i = 1; i <=w; i++)
    {
        sort(G[i].begin(),G[i].end());
        G[i].insert(G[i].begin(),{1,-1});
        last[i] = 0;
    }
    int story = 1;

    int mx =  -1;
    while (true)
    {
        int ok = 0;
        for (int i = 1; i <=w; i++)
        {
            if( G[i].size()>story )++ok;
        }

        if( ok<w ){            
            break;
        }else{

            for (int i = 1; i <=w; i++)
            {
                last[i] = last[i]+ ( G[i][story].first - G[i][story-1].first);
                mx = max(last[i]+1,mx);
            }
            for (int i = 1; i <=w; i++)
            {
                tout[ G[i][story].second ] = mx;
            }
        }
        ++story;
    }
    
    int q;
    cin >> q;
    while (q--)
    {
        int t,a;
        cin >> t >> a;
        if( tout[a]>t ){
            cout<<"Yes"<<'\n';
        }else{
            cout<<"No"<<'\n';
        }
    }
    
    
    return 0;
}
