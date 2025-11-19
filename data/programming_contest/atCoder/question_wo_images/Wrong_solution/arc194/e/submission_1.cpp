#include<bits/stdc++.h>
#define LL long long
#define P pair<int,int>
#define fi first
#define se second
#define fr(x) freopen(#x".in","r",stdin);freopen(#x".out","w",stdout);
using namespace std;
const int N=5e5+5;
int n,x,y;string S,T;P g[N];
inline string sol(string S)
{
	S+=' ';int m=0;
	for(int i=1,s=1;i<=n;i++)
	{
		if(S[i]==S[i-1]) s++;
		else
		{
			bool o=S[i-1]-'0';int w=o?y:x;
			int u=s/w*w;s%=w;
			if(o)
			{
				if(u) g[++m]={u,o};
				while(s--) g[++m]={-1,o};	
			}
			else
			{
				while(s--) g[++m]={-1,o};
				if(u) g[++m]={u,o};
			}
			s=1;
		}
	}
	int w=-1;
	auto upd=[&](int i){
		auto [x,o]=g[i];
		if(x>0&&!o) (w==-1)&&(w=i);
		else w=-1;
	};upd(1);
	for(int i=2;i<=m;i++)
	{
		auto [x,o]=g[i];
		if(x>0&&o&&(~w)) swap(g[i],g[w]),w++;
		upd(i);
	}S="";
	for(int i=1;i<=m;i++)
	{
		auto [x,o]=g[i];x=abs(x);
		while(x--) S+=o?'1':'0';
	}
	return S;
}
int main()
{
	cin.tie(0)->sync_with_stdio(0);cout.tie(0);cin>>n>>x>>y>>S>>T;
	puts("Yes");
	return 0;
}