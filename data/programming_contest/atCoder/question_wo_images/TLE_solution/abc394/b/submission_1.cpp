#include<bits/stdc++.h>

using namespace std;

void solve(){
	int n;
	cin>>n;
	string s[100];
	for(int i=0;i<=n;i++) {cin>>s[i];}
	for(int l=1;l<=50;l++){
		for(int i=0;i<=n;i++){
			if(l=s[i].size()) cout<<s[i];
		}
	}
}
int main(){
	int t=1;
	while(t--){					
		solve();
	}
} 