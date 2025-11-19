#include <bits/stdc++.h>
using namespace std;

#ifdef LOCAL
#include "debug.hpp"
#define dbg(x...) cerr << "[" << #x << "]=["; _print(x)
#else
#define dbg(x...) 
#endif

#define inf (long long)1e18
#define endl "\n"
#define int long long
#define x first
#define y second
#define all(x) (x).begin(),(x).end() 

void solve(int tc)
{   
    int n,w;
    cin>>n>>w;
    int BIT=60;
    vector<vector<int>>v(BIT);
    vector<int>pf(BIT);
    for(int i=0;i<n;i++)
    {
        int x,y;
        cin>>x>>y;
        pf[x]++;
        v[x].push_back(y);
    }
    for(int i=0;i<BIT;i++)
    {
        sort(all(v[i]),greater<int>());
        if(i)
            pf[i]+=pf[i-1];
    }
    
    vector<vector<vector<int>>>dp(BIT,vector<vector<int>>(n+1,vector<int>(2,-1)));
    auto cc=[&](int i, int x, int free, auto &&cc)->int
    {
        if(i<0 || x<0)
            return 0;
        x=min(x,pf[i]);
        if(dp[i][x][free]!=-1)
            return dp[i][x][free];
        
        int X=x;
        if(x>pf[i])
            x=pf[i],X=pf[i];
        if(((1LL<<i) & (w))) x++;
        else if(free) x++;
        int sm=0,cur=0;
        for(int y=0;y<=v[i].size();y++)
        {   
            if(y)
            {
                sm+=v[i][y-1];
            }
            if(x-y<0)
                break;
            cur=max(cur,cc(i-1,(x-y)*2,0,cc)+sm);
        }
        if(x==0 && ((1LL<<i) & (w)))
            cur=max(cur,cc(i-1,0,1,cc));
        return dp[i][X][free]=cur;
    };  
    cout<<cc(BIT-1,0,0,cc)<<endl;
}   
int32_t main()      
{   
    #ifdef LOCAL1
        auto begin = std::chrono::high_resolution_clock::now();
    #endif
    ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    int t=1;
    cin>>t;
    int tc=1;
    while (t--)
    {
        solve(tc),tc++;
    }
    #ifdef LOCAL1
        auto end = std::chrono::high_resolution_clock::now();
        cerr << setprecision(4) << fixed;
        cerr << "-> " << std::chrono::duration_cast<std::chrono::duration<double>>(end - begin).count() << " sec" << endl;
    #endif
    return 0;
}