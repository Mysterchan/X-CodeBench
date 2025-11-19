#include <bits/stdc++.h>
using namespace std;
const int MN=1e6+116;
int n, a[MN], b[MN];
void Read(){
	cin>>n;
	for(int i=1; i<=n; ++i) cin>>a[i];
	for(int i=1; i<=n; ++i) cin>>b[i];
	return;
}
void Solve(){
	Read(); int suma=0, sumb=0;
	for(int i=1; i<=n; ++i) suma+=a[i];
	for(int i=1; i<=n; ++i) sumb+=b[i];
	if(suma==sumb){
		if(a[1]!=b[1]&&a[n]!=b[n]) cout<<"No\n";
		else cout<<"Yes\n";
	}else{
		cout<<"No\n";
	}
	return;
}
int main(){
	ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	int T; cin>>T; while(T--) Solve();
	return 0;
}