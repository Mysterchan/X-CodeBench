#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mid ((l+r)>>1)
const int N=5e4+5;
int t,n,a[4][N],buc[4*N],len;
struct Tree{
	int ct,tr[20*N],ls[20*N],rs[20*N],rt[N];
	void ins(int l,int r,int &u,int p){
		++ct,tr[ct]=tr[u],ls[ct]=ls[u],rs[ct]=rs[u],u=ct;
		if(l==r) {tr[u]++;return;}
		p<=mid?ins(l,mid,ls[u],p):ins(mid+1,r,rs[u],p);
		tr[u]=tr[ls[u]]+tr[rs[u]];
	}
	int query(int l,int r,int r1,int r2,int k){
		if(l==r) return l;
		if(tr[ls[r1]]-tr[ls[r2]]>=k) return query(l,mid,ls[r1],ls[r2],k);
		return query(mid+1,r,rs[r1],rs[r2],k-(tr[ls[r1]]-tr[ls[r2]]));
	}
}T[4];
int dir[2][2]={1,0,2,3};
ll get(int i,int k,int l=1,int r=n-2){
	assert(k<=r-l+1);
	return buc[T[i].query(1,len,T[i].rt[r],T[i].rt[l-1],k)];
}
int main(){
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		len=0;
		for(int i=0;i<4;i++)
			for(int j=1;j<=n-2;j++) scanf("%d",&a[i][j]),buc[++len]=a[i][j];
		sort(buc+1,buc+len+1),len=unique(buc+1,buc+len+1)-buc-1;
		for(int i=0;i<4;i++){
			T[i].ct=0;
			for(int j=1;j<=n-2;j++){
				a[i][j]=lower_bound(buc+1,buc+len+1,a[i][j])-buc;
				T[i].ins(1,len,T[i].rt[j]=T[i].rt[j-1],a[i][j]);
			}
		}
		ll ans=1e18;
		for(int tp=0;tp<2;tp++){
			ll tmp=get(dir[tp][0],1)+get(dir[tp][0],2)+get(dir[tp][1],1)+get(dir[tp][1],2);
			int u=dir[!tp][0],v=dir[!tp][1];
			for(int i=2;i<=n-2;i++){
				ll now=tmp+buc[a[u][i]]+get(u,1,1,i-1)+get(v,1,1,min(i+1,n-2));
				ans=min(ans,now+get(v,2,1,min(i+1,n-2)));
				if(i+2<=n-2) ans=min(ans,now+get(v,1,i+2,n-2));
			}
			for(int i=3;i<=n-6;i++){
				ll now=tmp+get(u,1,1,i)+get(u,2,1,i)+get(u,3,1,i)
					+get(v,1,i+2,n-2)+get(v,2,i+2,n-2)+get(v,3,i+2,n-2);
				ans=min(ans,now);
			}
		}
		printf("%lld\n",ans);
	}
	return 0;
}