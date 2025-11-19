#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<vector>
using namespace std;
const int M=2000000,N=500000;
struct sgt
{
	int val[M];
	int ask(int x,int l,int r,int ll,int rr)
	{
		int mid;
		if (l>=ll&&r<=rr) return val[x];
		mid=l+r>>1;
		if (ll<=mid&&rr>mid) return max(ask(x<<1,l,mid,ll,rr),ask(x<<1^1,mid+1,r,ll,rr));
		if (ll<=mid) return ask(x<<1,l,mid,ll,rr);
		return ask(x<<1^1,mid+1,r,ll,rr);
	}
	void modify(int x,int l,int r,int p,int y)
	{
		int mid;
		if (l==r)
		{
			val[x]=y;
			return;
		}
		mid=l+r>>1;
		if (p<=mid) modify(x<<1,l,mid,p,y);
		else modify(x<<1^1,mid+1,r,p,y);
		val[x]=max(val[x<<1],val[x<<1^1]);
	}
}
sgt1,sgt2,sgt3,sgt4;
int s[M],t[M],p[M];
pair<int,int>a[M];
bool vis1[N],vis2[N];
int main()
{
	int n,m,q,i,k,j,pos1,pos2,pos3,pos4,l,r;
	scanf("%d%d%d",&n,&m,&q);
	for (i=1;i<=m;i++) scanf("%d%d",&s[i],&t[i]);
	k=0;
	for (i=1;i<=m;i++) if (s[i]<t[i])
	{
		a[k++]=make_pair(s[i],i);
		a[k++]=make_pair(t[i],-i);
	}
	else
	{
		a[k++]=make_pair(s[i],-i);
		a[k++]=make_pair(t[i],i);
	}
	sort(a,a+k);
	for (i=j=1;i<=m;i++)
	{
		if (s[i]<t[i])
		{
			pos1=lower_bound(a,a+k,make_pair(s[i],i))-a;
			pos2=lower_bound(a,a+k,make_pair(t[i],-i))-a;
		}
		else
		{
			pos1=lower_bound(a,a+k,make_pair(s[i],-i))-a;
			pos2=lower_bound(a,a+k,make_pair(t[i],i))-a;
		}
		for (;j<=m;j++)
		{
			if (!(vis1[min(s[i],t[i])]||vis2[max(s[i],t[i])])) if (s[i]<t[i])
			{
				if (sgt1.ask(1,0,k-1,pos1,pos2)<t[i]&&sgt2.ask(1,0,k-1,pos1,pos2)<n-s[i]+1) break;
			}
			else if (sgt3.ask(1,0,k-1,pos2,pos1)<s[i]&&sgt4.ask(1,0,k-1,pos2,pos1)<n-t[i]+1) break;
			vis1[min(s[j],t[j])]=vis2[max(s[j],t[j])]=0;
			if (s[j]<t[j])
			{
				pos3=lower_bound(a,a+k,make_pair(s[j],j))-a;
				pos4=lower_bound(a,a+k,make_pair(t[j],-j))-a;
				sgt1.modify(1,0,k-1,pos3,0);
				sgt2.modify(1,0,k-1,pos4,0);
			}
			else
			{
				pos3=lower_bound(a,a+k,make_pair(s[j],-j))-a;
				pos4=lower_bound(a,a+k,make_pair(t[j],j))-a;
				sgt3.modify(1,0,k-1,pos4,0);
				sgt4.modify(1,0,k-1,pos3,0);
			}
		}
		vis1[min(s[i],t[i])]=vis2[max(s[i],t[i])]=0;
		if (s[i]<t[i])
		{
			sgt1.modify(1,0,k-1,pos1,t[i]);
			sgt2.modify(1,0,k-1,pos2,n-s[i]+1);
		}
		else
		{
			sgt3.modify(1,0,k-1,pos2,s[i]);
			sgt4.modify(1,0,k-1,pos1,n-t[i]+1);
		}
		p[i]=j;
	}
	for (;q;q--)
	{
		scanf("%d%d",&l,&r);
		if (l<p[r]) printf("No\n");
		else printf("Yes\n");
	}
	return 0;
}