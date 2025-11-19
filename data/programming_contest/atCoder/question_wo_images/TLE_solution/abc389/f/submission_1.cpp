#include<bits/stdc++.h>
using namespace std;
const int M=5e5+5,N=5e5;
namespace SGT{
	#define lc nodeno<<1
	#define rc nodeno<<1|1
    struct node{
        int l,r,mx,mn,lz;
    }stree[M<<2];	
    void pushup(int nodeno)
    {
    	stree[nodeno].mx=max(stree[lc].mx,stree[rc].mx);
    	stree[nodeno].mn=min(stree[lc].mn,stree[rc].mn);
	}
	void pushdown(int nodeno)
	{
		if(stree[nodeno].lz)
		{
			stree[nodeno].mx+=stree[nodeno].lz;
			stree[nodeno].mn+=stree[nodeno].lz;
			if(stree[nodeno].l!=stree[nodeno].r)
			{
				stree[lc].lz+=stree[nodeno].lz;
				stree[rc].lz+=stree[nodeno].lz;
			}
			stree[nodeno].lz=0;
		}
	}
	
	
	void build(int nodeno,int tst,int tnd)
	{
		stree[nodeno]={tst,tnd,INT_MIN,INT_MAX,0};
		if(tst==tnd)
		{
			stree[nodeno].mn=stree[nodeno].mx=tst;
			return;
		}
		int tmid=(tst+tnd)>>1;
		build(lc,tst,tmid);
		build(rc,tmid+1,tnd);
		pushup(nodeno);
	}
	
	int ask1(int nodeno,int l,int r,int x)
	{
		pushdown(nodeno);
		if(stree[nodeno].mx<x)return 1e9;
		if(stree[nodeno].mn>x)return stree[nodeno].l;
		if(stree[nodeno].l==stree[nodeno].r)
		{
			return stree[nodeno].l;
		}
		int mid=(l+r)>>1;
		
		return min(ask1(lc,l,r,x),ask1(rc,l,r,x));
	}
	int ask2(int nodeno,int l,int r,int x)
	{
		pushdown(nodeno);
		if(stree[nodeno].mn>x)return -1e9;
		if(stree[nodeno].mx<x)return stree[nodeno].r;
		if(stree[nodeno].l==stree[nodeno].r)
		{
			return stree[nodeno].l;
		}
		int mid=(l+r)>>1;
		
		return max(ask2(lc,l,r,x),ask2(rc,l,r,x));
	}
	void add(int nodeno,int l,int r,int val)
	{
		pushdown(nodeno);
		if(stree[nodeno].l>r || l>stree[nodeno].r)return;
		if(l<=stree[nodeno].l && stree[nodeno].r<=r)
		{
			stree[nodeno].lz+=val;
			pushdown(nodeno);
			return;
		}
		add(lc,l,r,val);
		add(rc,l,r,val);
		pushup(nodeno);
	}
	int ask(int nodeno,int x)
	{
		pushdown(nodeno);
		
		if(stree[nodeno].l==stree[nodeno].r)return stree[nodeno].mn;
		int mid=(stree[nodeno].l+stree[nodeno].r)>>1;
		if(x<=mid)return ask(lc,x);
		return ask(rc,x);
	}
}using namespace SGT;

int main()
{
ios::sync_with_stdio(0);
	int n;
	long long m;
	cin>>n;
	build(1,1,N);
	for(int i=0;i<n;i++)
	{
		int l,r;
		cin>>l>>r;
		l=ask1(1,1,N,l);
		r=ask2(1,1,N,r);
		if(l<=r)add(1,l,r,1);
	}
	int q;
	cin>>q;
	while(q--)
	{
		int x;
		cin>>x;
		cout<<ask(1,x)<<"\n";
	}
}