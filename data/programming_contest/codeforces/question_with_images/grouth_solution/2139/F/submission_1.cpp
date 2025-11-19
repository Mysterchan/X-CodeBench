#include<bits/stdc++.h>
using namespace std;
const long long mod=1000000007;
long long a[5000],ans[5000],tt[5001],inv[5001];
struct apos{
	long long id;
	long long x;
	friend bool operator<(apos a,apos b){
		return a.x<b.x;
	}
}ap[5000];
int main(){
	ios::sync_with_stdio(false),cin.tie(0);
	int T,flag;
	long long n,m,p,q,x,i,j,cl,cr;
	tt[0]=1;
	for(i=1;i<=5000;i++)tt[i]=tt[i-1]*i%mod;
	inv[1]=1;
	for(i=2;i<=5000;i++)inv[i]=(mod-mod/i)*inv[mod%i]%mod;
	for(cin>>T;T>0;T--)
	{
		cin>>n>>m>>p;
		for(i=0;i<n;i++)
		{
			cin>>a[i];
			a[i]-=i;
		}
		for(i=0;i<p;i++)
		{
			cin>>ap[i].id>>ap[i].x;
			ap[i].id--;
			ap[i].x-=ap[i].id;
		}
		sort(ap,ap+p);
		for(i=0;i<n;i++)
		{
			flag=0;
			for(j=0;j<p;j++)
			{
				if(ap[j].id<=i&&ap[j].x>=a[i])flag=1;
				if(ap[j].id>=i&&ap[j].x<a[i])flag=1;
			}
			if(!flag)
			{
				ans[i]=a[i]+i;
				continue;
			}
			ans[i]=0;
			cl=0;
			cr=0;
			for(j=0;j<p;j++)
			{
				if(ap[j].id<=i)cr++;
			}
			for(j=0;j<p;j++)
			{
				if(ap[j].id<=i)cr--;
				if(ap[j].id==i)ans[i]=(ans[i]+(ap[j].x+i)*inv[cl+cr+1])%mod;
				if(ap[j].id<i)
				{
					if(cl==0&&cr==0&&a[i]<=ap[j].x)ans[i]=(ans[i]+ap[j].x+i)%mod;
					else ans[i]=(ans[i]+(ap[j].x+i)*inv[cl+cr+1]%mod*inv[cl+cr]%mod*cl)%mod;
				}
				if(ap[j].id>i)
				{
					if(cl==0&&cr==0&&a[i]>ap[j].x)ans[i]=(ans[i]+ap[j].x+i)%mod;
					else ans[i]=(ans[i]+(ap[j].x+i)*inv[cl+cr+1]%mod*inv[cl+cr]%mod*cr)%mod;
				}
				if(ap[j].id>=i)cl++;
			}
		}
		for(int x = 0;x < n;x ++)
		{
			cout<<ans[x]*tt[p]%mod<<' ';
		}
		cout<<'\n';
	}
	return 0;
}