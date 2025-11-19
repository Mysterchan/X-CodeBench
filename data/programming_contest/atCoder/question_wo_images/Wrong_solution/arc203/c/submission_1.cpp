#include <bits/stdc++.h>
#define int long long

using namespace std;

const int N = 500010,mod= 998244353;

typedef long long ll;

int fa[N],inf[N]; 

int qmi(int a,int b)
{
    int ans=1;
    while(b){
        if(b&1) ans=ans*a%mod;
        a=a*a%mod;
        b>>=1;
    }
    return ans;
}

void intt()
{
    fa[0]=1;
    for(int i=1;i<N;i++) fa[i]=fa[i-1]*i%mod;
    inf[N-1]=qmi(fa[N-1],mod-2);
    for(int i=N-2;i>=1;i--) inf[i]=(i+1)*inf[i+1]%mod;
    inf[0]=1;
}

int C(int a,int b)
{
    return fa[a]*inf[b]%mod*inf[a-b]%mod;
}

void solve()
{
    int n,m,k;

    cin>>n>>m>>k;

    int x=(n-1)*m+(m-1)*n-(n+m-2);
    x%=mod;
    if(k<n+m-2){
        cout<<0<<"\n";
    }else if(k==n+m-2){
        cout<<C(n+m-2,n-1)<<"\n";
    }else if(k==n+m-1){
        cout<<x*C(n+m-2,n-1)%mod<<"\n";
    }else{
        x=x*(x-1)%mod*qmi(2,mod-2)%mod;
        int y=qmi(2,mod-2);
        cout<<((x*C(n+m-2,n-1)%mod-C(n+m-4,n-2)*(n+m-3)%mod)%mod+mod+C(n+m-2,n)%mod*(n)%mod+C(n+m-2,m)%mod*(m)%mod)%mod<<"\n";
    }
}

signed main()
{
    int t=1;
    intt();
    cin>>t;
    while(t--){
        solve();
    }
}