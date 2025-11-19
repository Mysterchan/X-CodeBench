#include<bits/stdc++.h>
using namespace std;
#define int long long
const int N=(1<<20),M=(1<<10)-1,mod=998244353;
int a[N+6];
signed main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int i,j,k;
    int n,m;
    int T=1;
    for(i=0;i<=N-1;i++)
    {
        a[i]=1;
    }
    cin>>n;
    for(i=1;i<=n;i++)
    {    
        int temp,ans=1;
        cin>>temp;  
        int x=temp>>10,y=temp&M;
        for(j=0;j<=M;++j)
        {
            if((y|j)==j)
            {
                a[x<<10|j]=temp*a[x<<10|j]%mod;
            }
        }
        for(j=0;j<=M;++j)
        {
            if((x|j)==x)
            {
                ans=ans*a[j<<10|y]%mod;
            }
        }
        cout<<ans<<"\n";
    }
    return 0;
}