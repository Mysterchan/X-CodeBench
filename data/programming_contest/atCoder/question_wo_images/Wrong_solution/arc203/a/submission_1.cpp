#include <bits/stdc++.h>
using namespace std;
void Solve(){
	int n, m; cin>>n>>m;
	cout<<n*(m/2)+(m%2)<<'\n';
	return;
}
int main(){
	ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	int T; cin>>T; while(T--) Solve();
	return 0;
}