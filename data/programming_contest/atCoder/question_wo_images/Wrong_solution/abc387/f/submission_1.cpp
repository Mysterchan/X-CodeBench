#include<bits/stdc++.h>
#define int long long
using namespace std;

const int M=1e6,mod=998244353;
int n,m,fac[M];

int qmi(int a,int b)
{
	int res=1;
	while(b)
	{
		if(b&1) res=(res*a)%mod;
		a=(a*a)%mod;
		b>>=1;
	}
	return res;
}

int C(int n,int m)
{
	if(n<m) return 0;
	return fac[n]*qmi(fac[n-m],mod-2)%mod*qmi(fac[m],mod-2)%mod;
}

void init()
{
	fac[0]=1;
	for(int i=1;i<M;i++)
		fac[i]=(fac[i-1]*i)%mod;
}

signed main()
{
	init();
	cin>>n>>m;
	if(n<=2||m<n-1)
	{
		cout<<0<<endl;
		return 0;
	}
	
	cout<<qmi(2,n-3)*C(m,n-1)%mod*(n-2)%mod<<endl;
	
	return 0;
}