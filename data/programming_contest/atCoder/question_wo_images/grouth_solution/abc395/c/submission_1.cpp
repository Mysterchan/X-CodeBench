#include<bits/stdc++.h>
using namespace std;
#define int long long
typedef pair<int,int>PII;

void solve(){
	int n,ans=1e18;
	cin>>n;
	vector<int>a(1e6+10,-1);
	for(int i=1,x;i<=n;i++){
		cin>>x;
		if(a[x]!=-1){
			ans=min(ans,i-a[x]+1);
		}
		a[x]=i;
	}
	if(ans==1e18)cout<<-1<<endl;
	else cout<<ans<<endl;
}

signed main(){
	int t=1;ios::sync_with_stdio(false),cin.tie(0),cout.tie(0);
	while(t--)solve();
	return 0;
}