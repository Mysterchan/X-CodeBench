#include <bits/stdc++.h>
#define int long long
using namespace std;

signed main() {
	int n,m; cin>>n>>m;
	vector<string> s(n),t(m);
	for(int i=0; i<n; i++) cin>>s[i];
	for(int j=0; j<m; j++) cin>>t[j];
	for(int a=0; a<=n-m; a++) {
		for(int b=0; b<=n-m; b++) {
			bool ok=true;
			for(int i=0; i<m; i++) {
				for(int j=0; j<m; j++) {
					if(s[a+i][b+j]!=t[i][j]) {
						ok=false;
						break;
					}
				}
				if(!ok) break;
			}
			if(ok) {
				cout<<a+1<<" "<<b+1<<"\n";
				return 0;
			}
		}
	}
	
	return 0;
}
