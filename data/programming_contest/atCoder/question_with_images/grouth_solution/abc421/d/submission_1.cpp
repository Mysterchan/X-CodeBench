#include<bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'
typedef long long ll;
#define lowbit(x) ((x)&-(x))
typedef pair<int,int> PII;
typedef unsigned long long ull;
#define puf push_front
#define pub push_back
#define heap priority_queue//大根堆
#define heapi(x) priority_queue<x,vector<x>,greater<x>>
#define cer(x) cerr<<x<<'\n';
#define f1 first
#define f2 second
const int N = 2e6+9;//全局2e8,局部2e5
const int M = 1e9+7;
const int INF = 0x3f3f3f3f;

map<char,PII> mp{{'R',{0,1}},{'L',{0,-1}},{'U',{-1,0}},{'D',{1,0}}};
void mains(){
    int rt,ct,ra,ca;cin>>rt>>ct>>ra>>ca;
	int x = ra - rt,y = ca - ct;
	int n,m,l;cin>>n>>m>>l;
	PII a[m],b[l];
	int cnt[2][max(l,m)]{};
	for(int i = 0;i<m;i++){
		char c;cin>>c;
		cin>>cnt[0][i];
		a[i] = mp[c];
	}
	for(int i = 0;i<l;i++){
		char c;cin>>c;
		cin>>cnt[1][i];
		b[i] = mp[c];
	}
	int ans = 0,i = 0,j = 0;
	while(n){
		int t = min(cnt[0][i],cnt[1][j]);
		PII mv = {b[j].f1-a[i].f1,b[j].f2-a[i].f2};
		if(mv == make_pair(0ll,0ll)){
			if(!(x||y)) ans += t;
		}else if(x*mv.f2 == y * mv.f1){
			if(mv.f1){
				if(x/mv.f1 >= -t && x/mv.f1 <0 && x%mv.f1==0) ans++;
			}else if(y/mv.f2 >= -t && y/mv.f2<0 &&y%mv.f2 == 0) ans++;
		}
		x += mv.f1*t;
		y += mv.f2*t;
		cnt[0][i] -= t;
		cnt[1][j] -= t;
		n -= t;
		if(!cnt[0][i]) i++;
		if(!cnt[1][j]) j++;
	}
	cout<<ans;
}
signed main(){
	cin.tie(0)->sync_with_stdio(0);
	int T = 1;
	while(T--){
		mains();
	}
	return 0;
}