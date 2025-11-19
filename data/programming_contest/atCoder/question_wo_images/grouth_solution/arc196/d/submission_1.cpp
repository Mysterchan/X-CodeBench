#include<bits/stdc++.h>
using ull=unsigned long long;
using namespace std;
const int N=4e5+5;
mt19937_64 rnd(time(0));

int n,m,q;
int s[N],t[N],op[N];
int cntL[N],cntR[N],L[N];
ull val[N];

struct BIT
{
	int c[N];
	void add(int i,ull x){for(;i<=n;i+=(i&(-i))) c[i]^=x;}
	ull ask(int i,ull s=0){for(;i>0;i-=(i&(-i))) s^=c[i];return s;}
}T[2];

signed main()
{
	cin>>n>>m>>q;
	for(int i=1;i<=m;i++)
	{
		cin>>s[i]>>t[i];
		op[i]=s[i]>t[i];
		if(s[i]>t[i]) swap(s[i],t[i]);
		val[i]=rnd();
	}
	for(int i=1,j=1;i<=m;i++)
	{
		cntL[s[i]]++,cntR[t[i]]++;
		T[op[i]].add(s[i],val[i]),T[op[i]].add(t[i],val[i]);
		while(cntL[s[i]]>1||cntR[t[i]]>1||T[op[i]].ask(t[i]-1)!=T[op[i]].ask(s[i]))
		{
			cntL[s[j]]--,cntR[t[j]]--;
			T[op[j]].add(s[j],val[j]),T[op[j]].add(t[j],val[j]);
			j++;
		}
		L[i]=j;
	}
	while(q--)
	{
		int l,r;cin>>l>>r;
		if(l<L[r]) cout<<"No\n";
		else cout<<"Yes\n";
	}
	return 0;
}