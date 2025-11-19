#include <iostream>
#include <cstdio>
#include <vector>
#include<map>
#include<set>
#include<cstring>
#include<cmath>
#include<queue>
#include<algorithm>
using namespace std;
 
 

using namespace std;
 
#define double long double
#define PII pair<int, int>
 
const double pi = acos(-1);
const double eps=1e-6;
const int inf = 2e18;
const int mod = 998244353;
const int N = 2e6 + 10;
int res[N];
void solve(){
    int n,m;
    cin>>n>>m;
    string s;
    string t;
    cin>>s;
    cin>>t;
    s='?'+s;
    t='?'+t;
    priority_queue<pair<int,int>>q;
    for(int i=1;i<=m;i++)
    {
        q.push({t[i]-'0',i});
    }
    for(int i=1;i<=n-1;i++)
    {
        int val=s[i]-'0';
        auto temp=q.top();

        if(q.top().first>val)
        {
            res[i]=temp.first;
            q.pop();
        }
        else
        {
            res[i]=val;
        }
        
    }
    
    res[n]=s[n]-'0';
    while(!q.empty())
    {
        res[n]=max(res[n],q.top().first);
        q.pop();
    }
    int ok=0;
    for(int i=1;i<=n;i++)if(res[i]==t[m]-'0')ok=1;
    if(!ok)res[n]=t[m]-'0';
    string r;
    for(int i=1;i<=n;i++)r+=res[i]+'0';
    cout<<r;
    
}
 
signed main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
 
    int t = 1;
    
    while(t--){
        solve();
    }
 
    return 0;
}

 


