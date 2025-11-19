#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
const int N=103;
ll n,m,K,b[N*2],a[N][N];
int main()
{
	cin>>n>>K;a[1][1]=K-1;
	for(ll i=1;i<=n;i++)for(ll j=1;j+i<=n;j++)if(a[i][j])
	{
		if(i+j==n){a[i+1][j]=a[i][j];continue;}
		ll x=a[i][j]/(i+j),y=a[i][j]%(i+j);
		ll v=x*i+min(y,i);
		a[i+1][j]+=v;a[i][j+1]+=a[i][j]-v;
	}
	ll x=1,y=1;
	while(x+y<=n)
	{
		if(a[x+1][y]<=a[x][y+1])b[++m]=1,x++;
		else b[++m]=0,y++;
	}
	for(int i=1;i<=m;i++)b[2*m+1-i]=b[i]^1;
	for(int i=1;i<=2*m;i++)cout<<(b[i]?'D':'R');
}