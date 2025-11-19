#include<bits/stdc++.h>
#define MAXN 500005
#define look_memory cerr<<abs(&M2-&M1)/1024.0/1024<<'\n'
#define look_time cerr<<(clock()-Time)*1.0/CLOCKS_PER_SEC<<'\n'
using namespace std;

inline int read(){
    int x=0;
    int f=1;
    char c=getchar();
    while(c<'0' || c>'9'){
        if(c=='-') f=-1;
        c=getchar();
    }
    while(c>='0' && c<='9'){
        x=(x<<1)+(x<<3)+(c^48);
        c=getchar();
    }
    return x*f;
}

bool M1;
int T,n,m;
vector<int> edge[MAXN];
int dep[MAXN],cnt[MAXN];

void dfs(int x){
	cnt[dep[x]]++;
	m=max(m,dep[x]);
	for(auto y:edge[x]){
		dep[y]=dep[x]+1;
		dfs(y);
	}
}

void clear(){
	for(int i=1;i<=n;i++){
		edge[i].clear();
		cnt[i]=dep[i]=0;
	}
}

bool M2;

signed main(){
    int Time=clock();
	T=read();
	while(T--){
		n=read();
		for(int i=2;i<=n;i++){
			int fa=read();
			edge[fa].push_back(i);
		}
		dep[1]=1;
		dfs(1);
		int ans=0,tmp=0;
		for(int i=m;i>=1;i--){
			if(tmp && cnt[i]>1){
				int t=min(tmp,cnt[i]-1);
				ans+=t;
				tmp-=t;
				cnt[i]-=t;
			}
			ans+=cnt[i]/2;
			if(cnt[i]&1) tmp++;
		}
		printf("%d\n",ans);
		clear();
	}
    look_memory;
    look_time;
    return 0;
}