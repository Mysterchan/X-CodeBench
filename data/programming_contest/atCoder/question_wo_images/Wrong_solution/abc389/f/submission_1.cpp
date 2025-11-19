#include<bits/stdc++.h>
using namespace std;
#define int long long
#define maxn 500001
int maximum[4*maxn];
int minimum[4*maxn];
int M=500000;
int n,q;
int l[maxn],r[maxn];
int lazy[4*maxn];
void pushup(int p,int l,int r){
	maximum[p]=max(maximum[p<<1],maximum[p<<1|1]);
	minimum[p]=min(minimum[p<<1],minimum[p<<1|1]);
}
void pushdown(int p,int l,int r){
	if(lazy[p]){
		lazy[p<<1]+=lazy[p];
		lazy[p<<1|1]+=lazy[p];
		maximum[p<<1]+=lazy[p];
		maximum[p<<1|1]+=lazy[p];
		minimum[p<<1|1]+=lazy[p];
		minimum[p<<1]+=lazy[p];		
		lazy[p]=0;
	}
	return;
}
void build(int l,int r,int p){
	if(l==r){
		maximum[p]=l;
		minimum[p]=l;
		return;
	}
	int mid=(l+r)>>1;
	build(l,mid,p<<1); build(mid+1,r,p<<1|1);
	pushup(p,l,r); return;
}
int resl,resr,x;
void update(int l,int r,int s,int t,int c,int p){
	if(l>t||r<s)return;
	if(l>=s&&r<=t){
		maximum[p]+=c;
		minimum[p]+=c;
		lazy[p]+=c;
		return;
	}
	pushdown(p,l,r);
	int mid=(l+r)>>1;
	if(mid>=s)update(l,mid,s,t,c,p<<1);
	if(mid<t)update(mid+1,r,s,t,c,p<<1|1);
	pushup(p,l,r);
	return; 
}
void find_l(int l,int r,int p,int x){
	if(l==r){
		resl=l;
		return;
	}
	pushdown(p,l,r);
	int mid=(l+r)>>1;
	if(maximum[p<<1]>=x)find_l(l,mid,p<<1,x);
	else if(maximum[p<<1|1]>=x)find_l(mid+1,r,p<<1|1,x);
	pushup(p,l,r);
	return;
}
void find_r(int l,int r,int p,int x){
	if(l==r){
		resr=r;
		return;
	}
	pushdown(p,l,r);
	int mid=(l+r)>>1;
	if(minimum[p<<1|1]<=x)find_r(mid+1,r,p<<1|1,x);
	else if(minimum[p<<1]<=x)find_r(l,mid,p<<1,x);
	pushup(p,l,r);
	return;
}
int query(int l,int r,int s,int t,int p){
	if(l>t||r<s)return 0;
	if(l>=s&&r<=t){
		return maximum[p];	
	}
	pushdown(p,l,r); 
	int mid=(l+r)>>1;
	int res;
	if(mid>=s)res=query(l,mid,s,t,p<<1);
	else res=query(mid+1,r,s,t,p<<1|1);
	pushup(p,l,r); return res;
}
signed main(){
	scanf("%lld",&n);
	for(int i=1;i<=n;i++)scanf("%lld%lld",&l[i],&r[i]);
	build(1,M,1); 
	for(int i=1;i<=n;i++){
		resl=-1,resr=-1;
		find_l(1,M,1,l[i]);
		find_r(1,M,1,r[i]);
		cout<<resl<<" "<<resr<<endl;
		if(resl!=-1&&resr!=-1)update(1,M,resl,resr,1,1);
	}
	scanf("%lld",&q);
	for(int i=1;i<=q;i++){
		scanf("%lld",&x);
		printf("%lld\n",query(1,M,x,x,1));
	}
	return 0;
}