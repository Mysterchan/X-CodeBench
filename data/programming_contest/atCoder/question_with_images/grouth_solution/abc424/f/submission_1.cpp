#include<bits/stdc++.h>
using namespace std;
const int N=1e6+10;
int n,xyq;
struct node{
	int l,r,mn,mx,mxtag,mntag;
}tr[N<<2];
bool check(int x,int y,int c){
	return x<c&&c<=n||1<=c&&c<y;
}
void pushup(int u){
	tr[u].mn=min(tr[u<<1].mn,tr[u<<1|1].mn);
	tr[u].mx=max(tr[u<<1].mx,tr[u<<1|1].mx);
}
void pushdown(int u){
	int ls=u<<1,rs=u<<1|1;
	tr[ls].mn=min(tr[ls].mn,tr[u].mntag);
	tr[rs].mn=min(tr[rs].mn,tr[u].mntag);
	tr[ls].mntag=min(tr[ls].mntag,tr[u].mntag);
	tr[rs].mntag=min(tr[rs].mntag,tr[u].mntag);
	tr[ls].mx=max(tr[ls].mx,tr[u].mxtag);
	tr[rs].mx=max(tr[rs].mx,tr[u].mxtag);
	tr[ls].mxtag=max(tr[ls].mxtag,tr[u].mxtag);
	tr[rs].mxtag=max(tr[rs].mxtag,tr[u].mxtag);
}
void build(int u,int l,int r){
	tr[u].l=l,tr[u].r=r;
	tr[u].mntag=n+1;
	if(l==r){
		tr[u].mn=n+1;
		return ;
	}
	int mid=l+r>>1;
	build(u<<1,l,mid);
	build(u<<1|1,mid+1,r);
	pushup(u);
}
void update(int u,int x,int k){
	if(tr[u].l==tr[u].r){
		tr[u].mn=min(tr[u].mn,k);
		tr[u].mntag=min(tr[u].mntag,k);
		tr[u].mx=max(tr[u].mx,k);
		tr[u].mxtag=max(tr[u].mxtag,k);
		return ;
	}
	pushdown(u);
	int mid=tr[u].l+tr[u].r>>1;
	if(x<=mid){
		update(u<<1,x,k);
	}
	else{
		update(u<<1|1,x,k);
	}
	pushup(u);
}
int qmn(int u,int l,int r){
	if(l<=tr[u].l&&tr[u].r<=r){
		return tr[u].mn;
	}
	pushdown(u);
	int ans=n+1,mid=tr[u].l+tr[u].r>>1;
	if(l<=mid){
		ans=qmn(u<<1,l,r);
	}
	if(r>mid){
		ans=min(ans,qmn(u<<1|1,l,r));
	}
	return ans;
}
int qmx(int u,int l,int r){
	if(l<=tr[u].l&&tr[u].r<=r){
		return tr[u].mx;
	}
	pushdown(u);
	int ans=0,mid=tr[u].l+tr[u].r>>1;
	if(l<=mid){
		ans=qmx(u<<1,l,r);
	}
	if(r>mid){
		ans=max(ans,qmx(u<<1|1,l,r));
	}
	return ans;
}
int main(){
	cin>>n>>xyq;
	build(1,1,n);
	while(xyq--){
		int x,y;
		cin>>x>>y;
		if(!((x<qmn(1,x,y)||qmn(1,x,y)==n+1)&&(qmx(1,x,y)<y||qmx(1,x,y)==0)&&(check(x,y,min(qmn(1,y,n),qmn(1,1,x)))||min(qmn(1,y,n),qmn(1,1,x))==n+1)&&(check(x,y,max(qmx(1,y,n),qmx(1,1,x)))||max(qmx(1,y,n),qmx(1,1,x))==0))){
			printf("No\n");
			continue;
		}
		printf("Yes\n");
		update(1,x,y),update(1,y,x);
	}
}