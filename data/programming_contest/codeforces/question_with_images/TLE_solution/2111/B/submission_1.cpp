#include<iostream> 
#include<cstdio> 
#include<algorithm> 
#include<string>
#include<cstring>
#include<vector> 
#include<queue> 
#include<set>
#include<list>
#include<map>
#include<unordered_set>
#include<unordered_map>
#include<deque>
#include<stack>
#include<cmath>
using namespace std;

#define int int
#define inf 0x3f3f3f3f
#define HH cout<<"\n";
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> PII;

struct Node
{
	int x,y,z;
};

const int N=155;
int fi[15];
vector<Node> va;
int biao[N][N][N];
int ok=0;

void dfs(int k,int a,int b,int c)
{
	if(ok) return;
	if(k==0)
	{
		ok=1;
	}
	else
	{
		for(int i=0;i<va.size();++i)
		{
			Node t=va[i];
			int r=fi[k];
			int x=t.x;
			int y=t.y;
			int z=t.z;
			if(!biao[x][y][z])
			{
				if(!(x+r<=a && y+r<=b && z+r<=c )) continue;
				biao[x][y][z]=1;
				if(y+r<b) va.push_back({x,y+r,z});
				if(z+r<c) va.push_back({x,y,z+r});
				if(x+r<a) va.push_back({x+r,y,z});
				dfs(k-1,a,b,c);
				if(ok) return;
				if(y+r<b) va.pop_back();
				if(z+r<c) va.pop_back();
				if(x+r<a) va.pop_back();
				biao[x][y][z]=0;
			}
		}
	}
}

signed main()
{
	int t;
	cin>>t;
	fi[1]=1;
	fi[2]=2;
	for(int i=3;i<=10;++i) fi[i]=fi[i-1]+fi[i-2];
	while(t--)
	{
		
		int n,m;
		cin>>n>>m;
		for(int i=0;i<m;++i)
		{
			int a,b,c;
			cin>>a>>b>>c;
			
			ok=0;
			if(fi[n]<=min(a,min(b,c)))
			{
				va.clear();
				va.push_back({0,0,0});
				memset(biao,0,sizeof biao);
				dfs(n,a,b,c);
			}
			
			cout<<ok;
		}
		cout<<'\n';
	}
	return 0;
}