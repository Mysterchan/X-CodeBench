#include<bits/stdc++.h>
using namespace std;
#define endl '\n'
#define yes cout << "Yes" << endl
#define no cout << "No" << endl
#define pii pair<int,int>
#define ll long long
#define pb push_back
#define ft first
#define se second
#define inf 0x3f3f3f3f
#define INF 0x3f3f3f3f3f3f3f3f
#define int long long

	


int n;int a[20];int c[20];
set<int> s;
void dfs(int step,int tot){
if(step==n+1){
	int res=0;
	for(int i=1;i<=tot;i++){
		res^=c[i];
	}s.insert(res);
	return ;
}
	
for(int i=1;i<=tot;i++){
	c[i]+=a[step];
	dfs(step+1,tot);
	c[i]-=a[step];
}
c[++tot]+=a[step];
dfs(step+1,tot);
c[tot--]-=a[step];
}
void solve(){
cin>>n;
for(int i=1;i<=n;i++)cin>>a[i];
dfs(1,0);
cout<<s.size()<<'\n';

}
signed main(){
    std::ios::sync_with_stdio(false);
    int T;T=1;
    while(T--){
        solve();
    }
}