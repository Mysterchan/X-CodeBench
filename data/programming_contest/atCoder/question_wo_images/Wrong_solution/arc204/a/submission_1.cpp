#include <bits/stdc++.h>
#define int long long
#define pb push_back
#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
using namespace std;
const int Nmax=5005,mod=998244353;
int a[Nmax],b[Nmax],mat[Nmax][Nmax],dp[Nmax][Nmax];
int power(int a,int b)
{
    int sol=1;
    while(b)
    {
        if(b%2==1)
        {
            sol=sol*a%mod;
        }
        a=a*a%mod;
        b=b/2;
    }
    return sol;
}
void read(int n)
{
    for(int i=1;i<=n;i++)
    {
        cin>>a[i];
    }
}
int n;
int solve(int mini)
{
    for(int i=0;i<=n;i++)
    {
        if(mat[0][i]<=mini) dp[0][i]=1;
        else dp[0][i]=0;
    }
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            if(i>j)
            {
                dp[i][j]=0;
                continue;
            }
            if(mat[i][j]<=mini) dp[i][j]=(dp[i-1][j]+dp[i][j-1])%mod;
            else dp[i][j]=0;
        }
    }
    return dp[n][n];
}
void solve()
{
    int l,r;
    cin>>n>>l>>r;
    for(int i=1;i<=n;i++)
    {
        cin>>a[i];
        mat[0][i]=mat[0][i-1]+a[i];
    }
    for(int j=1;j<=n;j++) cin>>b[j];
    for(int i=1;i<=n;i++)
    {
        for(int j=0;j<=n;j++)
        {
            mat[i][j]=mat[i-1][j]-b[i];
        }
    }
    cout<<solve(r+mat[n][n])-solve(mat[n][n]+l-1)<<'\n';
}
signed main()
{
    int t=1;
    while(t--)
    {
        solve();
    }
    return 0;
}
