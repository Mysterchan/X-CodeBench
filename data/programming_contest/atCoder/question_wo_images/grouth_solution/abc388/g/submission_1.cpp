#include<bits/stdc++.h>
#define int long long
using namespace std;
int a[214514];
int b[214514];
int ls(int x){return x*2;}
int rs(int x){return x*2+1;}
int t[1114514];
int n;
void build(int k,int l,int r){
	if(l==r){
		t[k]=b[l];
		return;
	}
	int mid=(l+r)/2;
	build(ls(k),l,mid);
	build(rs(k),mid+1,r);
	t[k]=max(t[ls(k)],t[rs(k)]);
}
int query(int k,int nl,int nr,int tl,int tr){
	if(nr<tl||nl>tr) return -1e18;
	if(nl>=tl&&nr<=tr){
		return t[k];
	}
	int mid=(nl+nr)/2;
	return max(query(ls(k),nl,mid,tl,tr),query(rs(k),mid+1,nr,tl,tr));
}
bool check(int l,int r,int x){
	int maxx=query(1,1,n,l,l+x);
	if(r-x-l<maxx) return 0;
	return 1;
}
signed main(){
	ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
	cin>>n;
	for(int i=1;i<=n;i++) cin>>a[i];
	for(int i=1;i<=n;i++){
		int l=i,r=n+1,mid;
		while(l<r){
			mid=(l+r)/2;
			if(a[mid]<2*a[i]) l=mid+1;
			else r=mid;
		}
		b[i]=l-i;
	}
	build(1,1,n);
	int q;
	cin>>q;
	while(q--){
		int x,y;
		cin>>x>>y;
		int l=0,r=(y-x+1)/2,mid;
		while(l<r){
			mid=(l+r)/2;
			if(check(x,y,mid)) l=mid+1;
			else r=mid;
		}
		cout<<l<<"\n";
	}
}