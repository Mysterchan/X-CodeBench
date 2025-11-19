#include<bits/stdc++.h>
using namespace std;
#define int long long
#define N 10000005
int n,a,b,mod=998244353,q;
inline int read(){
	int a=0,f=1;
	char c=getchar();
	while(c<'0'||c>'9'){
		if(c=='-')f=-1;
		c=getchar();
	}
	while(c>='0'&&c<='9'){
		a=a*10+c-'0';
		c=getchar();
	}
	return a*f;
}
int f[N][2],g[N][2];
int ksm(int a,int b){
	if(b<=0)return 1;
	int s=1;
	while(b){
		if(b%2)s=(s*a)%mod;
		a=(a*a)%mod,b/=2;
	}
	return s;
}
int jc[N];
int C(int a,int b){
	if(a<0||b<0)return 0;
	return jc[a]*ksm(jc[b],mod-2)%mod*ksm(jc[a-b],mod-2)%mod;
}
main(){
	n=read(),a=read(),b=read(),q=read();
	jc[0]=1;
	for(int i=1;i<=n;i++)
		jc[i]=jc[i-1]*i%mod;
	f[0][0]=1,g[0][0]=1;
	for(int i=1;i<=n;i++){
		if(i>=a)f[i][1]+=C(i-1,a-1),f[i][1]%=mod;
		if(i>=n-a+1&&i!=n)f[i][1]+=C(i-1,n-a),f[i][1]%=mod;
		if(i!=n)f[i][0]=(f[i-1][0]*2-f[i][1]+mod)%mod;
	}
	for(int i=1;i<=n;i++){
		if(i>=b)g[i][1]+=C(i-1,b-1),g[i][1]%=mod;
		if(i>=n-b+1&&i!=n)g[i][1]+=C(i-1,n-b),g[i][1]%=mod;
		if(i!=n)g[i][0]=(g[i-1][0]*2-g[i][1]+mod)%mod;
	}
	while(q--){
		int ls=read(),k=n-ls+1;
		printf("%lld\n",(f[k][0]*g[k][1]%mod+f[k][1]*g[k][0]%mod+f[k][1]*g[k][1]%mod)%mod*ksm(4,ls-2)%mod);
	}
	return 0;
}
