#include<bits/stdc++.h>
using namespace std;

#define ll long long

const int mxN=2e5;

int st[21][mxN];

int main() {
	ios::sync_with_stdio(0); cin.tie(0);
	int n; cin>>n;
	vector<int> a(n);
	for(int i=0; i<n; i++) cin>>a[i];
	for(int i=0; i<n; i++) {
		st[0][i]=lower_bound(a.begin(), a.end(), 2*a[i])-a.begin()-i;
	}
	for(int i=1; i<=20; i++) {
		for(int j=0; j+(1<<i)-1<n; j++) {
			st[i][j]=max(st[i-1][j], st[i-1][j+(1<<i-1)]);
		}
	}
	auto qry=[&](int l, int r) {
		int h=__lg(r-l+1);
		return max(st[h][l], st[h][r-(1<<h)+1]);
	};
	int q; cin>>q;
	while(q--) {	
		int l, r; cin>>l>>r;
		l--, r--;
		int ans=0;
		for(int i=20; ~i; i--) {
			if((1<<i)+ans>n/2) continue;
			if(qry(l, l+ans+(1<<i)-1)<=r-ans-(1<<i)-l+1) {
				ans+=(1<<i);	
			}
		}
		cout<<ans<<"\n";
	}
	return 0;
}

