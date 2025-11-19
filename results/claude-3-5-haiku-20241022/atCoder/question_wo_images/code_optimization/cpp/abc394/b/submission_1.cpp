#include<bits/stdc++.h>

using namespace std;

void solve(){
	int n;
	cin>>n;
	vector<string> s(n);
	for(int i=0;i<n;i++) {
		cin>>s[i];
	}
	sort(s.begin(), s.end(), [](const string& a, const string& b){
		return a.size() < b.size();
	});
	for(int i=0;i<n;i++){
		cout<<s[i];
	}
}

int main(){
	solve();
	return 0;
}