#include<bits/stdc++.h>
#define mod 998244353
#define int long long
using namespace std;
int n,q,a[200005],u,v,f[200005],g[20005],fac=1,s;
int ksm(int a,int b){
	int res=1;
	while(b){
		if(b&1)res=res*a%mod;
		a=a*a%mod,b>>=1;
	}
	return res;
}
signed main(){
	cin>>n>>q;
	for(int i=2;i<=n;i++)cin>>a[i],fac=fac*(i-1)%mod;
	for(int i=2;i<=n;i++)f[i]=(a[i]+s*ksm(i-1,mod-2))%mod,s=(s+f[i])%mod;s=0;
	for(int i=2;i<=n;i++)g[i]=(f[i]+s)*ksm(i,mod-2)%mod,s=(s+g[i])%mod;
	while(q--)cin>>u>>v,cout<<(f[u]+f[v]+mod-2*g[u]%mod)*fac%mod<<"\n";
} 