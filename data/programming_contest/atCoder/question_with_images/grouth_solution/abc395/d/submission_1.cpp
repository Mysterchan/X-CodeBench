#include<bits/stdc++.h>
using namespace std;
#define int long long
typedef pair<int,int>PII;

void solve(){
	int n,q;
	cin>>n>>q;
	vector<int>a(n+10),g(n+10),d(n+10);
	for(int i=1;i<=n;i++)a[i]=i,g[i]=i,d[i]=i;
	while(q--){
		int op,b,c;
		cin>>op;
		if(op==1){
			cin>>b>>c;
			g[b]=d[c];
		}else if(op==2){
			cin>>b>>c;
			swap(a[d[b]],a[d[c]]);
			swap(d[b],d[c]);
		}else{
			cin>>b;
			cout<<a[g[b]]<<endl;
		}
	}
}

signed main(){
	int t=1;ios::sync_with_stdio(false),cin.tie(0),cout.tie(0);
	while(t--)solve();
	return 0;
}