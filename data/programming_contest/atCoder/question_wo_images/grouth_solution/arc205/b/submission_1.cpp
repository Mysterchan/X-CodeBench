#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

const int N = 10010;

typedef long long ll;

void solve()
{
    ll n,m;
    
    cin>>n>>m;

    vector<int> cnt(n+1,n-1);

    int flag=0;
    
    for(int i=1;i<=m;i++){
        int x,y;
        cin>>x>>y;
        cnt[x]--,cnt[y]--;
    }

    ll ans=n*(n-1)/2;
    
    int x=0;
    
    for(int i=1;i<=n;i++){
        if(cnt[i]%2){
            x++;
        }
    }

    x=x/2;
    
    cout<<ans-x<<" ";
}

int main()
{
    int t=1;
    while(t--){
        solve();
    }
}