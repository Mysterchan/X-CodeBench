#include<bits/stdc++.h>
using namespace std;
const int N=1e6+10;
int c[N],cnt[N],ans;
int main(){
	ios::sync_with_stdio(0),cin.tie(0),cout.tie(0);
	int n,q;
	cin>>n>>q;
	for(int i=1;i<=n;i++) c[i]=i,cnt[i]=1;
	while(q--){
		int opt;
		cin>>opt;
		if(opt==1){
			int p,h;
			cin>>p>>h;
			if(cnt[h]==1){
				ans++;
			}
			if(cnt[c[p]]==2){
				ans--;
			}
			cnt[h]++;
			cnt[c[p]]--;
			c[p]=h;
		}else{
			cout<<ans<<"\n";
		}
	}	
	return 0;
}
