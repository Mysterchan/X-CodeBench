#include<bits/stdc++.h>
using namespace std;
const int N=2e5+5;
int n,Q,a[N],Rank[N],cnt,ans[N];
struct BIT{
	int t[N];
	BIT(){memset(t,0,sizeof(t));}
	void add(int u,int k){
		for(;u<=cnt;u+=(u&-u))t[u]=max(t[u],k);
	}
	int query(int u){
		int ans=0;
		for(;u;u-=u&-u)ans=max(ans,t[u]);
		return ans;
	}
}tr;
struct qry{
	int r,x,id;
	qry(){r=x=0;}
}q[N];
bool cmp(qry x,qry y){
	if(x.r==y.r)return x.x<y.x;
	return x.r<y.r;
}
signed main(){
	cin>>n>>Q;
	for(int i=1;i<=n;i++)cin>>a[i],Rank[++cnt]=a[i];
	for(int i=1;i<=Q;i++)cin>>q[i].r>>q[i].x,q[i].id=i,Rank[++cnt]=q[i].x;
	sort(Rank+1,Rank+cnt+1);
	sort(q+1,q+Q+1,cmp);
	cnt=unique(Rank+1,Rank+cnt+1)-Rank-1;
	for(int i=1;i<=n;i++)a[i]=lower_bound(Rank+1,Rank+cnt+1,a[i])-Rank;
	for(int i=1;i<=Q;i++){
		for(int j=q[i-1].r+1;j<=q[i].r;j++){
			int o=a[j];
			int u=tr.query(o-1);
			tr.add(o,u+1);
		}
		q[i].x=lower_bound(Rank+1,Rank+cnt+1,q[i].x)-Rank;
		int p=tr.query(q[i].x);
		ans[q[i].id]=p;
	}
	for(int i=1;i<=Q;i++)cout<<ans[i]<<endl;
	return 0;
}