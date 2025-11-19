#pragma GCC optimize("Ofast")
#include<bits/stdc++.h>
#define int long long
#define ok cout<<"ok\n"
using namespace std;
typedef pair<int,int> PII;
#define ft first
#define sd second
const int N=4e5+10;
const int mod=998244353;
const int inf=0x3f3f3f3f3f3f3f3f;
int n,m;
int a[N],b[N];
int ans[N];

void solve(){
	
	cin>>n>>m;
	
	for(int i=1;i<=n+m;i++)ans[i]=0;
	
	for(int i=1;i<=n;i++)cin>>a[i];
	for(int i=1;i<=m;i++)cin>>b[i];
	
	sort(a+1,a+n+1);
	sort(b+1,b+m+1);
	
	vector<int>c,d;
	
	c.push_back(0);
	for(int i=1,j=n-i+1;i<j;i++,j--)c.push_back(a[j]-a[i]);
	for(int i=1;i<c.size();i++)c[i]+=c[i-1];
	
	d.push_back(0);
	for(int i=1,j=m-i+1;i<j;i++,j--)d.push_back(b[j]-b[i]);
	for(int i=1;i<d.size();i++)d[i]+=d[i-1];
	
	int t1=n,t2=m;
	
	int len;
	if(n>=m*2)len=m;
	else if(m>=n*2)len=n;
	else if(n>=m){
		len+=n-m;
		n-=len*2;
		m-=len;
		
		len+=n/3*2;
		n%=3;
		
		if(n==2)len++;
	}
	else{
		len+=m-n;
		m-=len*2;
		n-=len;
		
		len+=m/3*2;
		m%=3;
		
		if(m==2)len++;
	}
	
	n=t1,m=t2;
	
	int u=c.size()-1;
	int v=d.size()-1;
	
	
	for(int i=1;i<=len;i++){
		int x=max(0ll,i-v);
		int y=min(u,i);
		
		
		int l=x,r=y;
		
		while(l+30<=r){
			int lmid=(l+r)/3;
			int rmid=(l+r)/3*2;
			
			if(c[lmid]+d[i-lmid]>=c[rmid]+d[i-rmid])l=lmid;
			else r=rmid;
		}
		for(int j=l;j<=r;j++){
			if(j+(i-j)*2<=m&&j*2+(i-j)<=n){
				ans[i]=max(ans[i],c[j]+d[i-j]);
			}
		}
	}
	
	
	cout<<len<<'\n';
	for(int i=1;i<=len;i++)cout<<ans[i]<<' ';
	cout<<'\n';
	
}
signed main(){
	ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
	int Case=1;
	cin>>Case;
	while(Case--)solve();
}