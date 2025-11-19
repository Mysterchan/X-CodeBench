#include<bits/stdc++.h>
using namespace std;
#define int long long
int n,m;
void slove(){
	cin>>n>>m;
	int ans=m,res=0;
	while(m>1){
		m-=2;
		res+=n;
		ans=max(ans,m+res);
	}
	cout<<ans<<endl;
}
signed main(){
	int T;
	cin>>T;
	while(T--)slove();
	return 0;
}