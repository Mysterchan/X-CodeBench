#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define N (int)1e5+10
int n,x,sum,minup=1e18,mindown=1e18;
int a,b,h=1e18;
signed main(){
	cin>>n>>x;
	for(int i=1;i<=n;i++){
		cin>>a>>b;
		sum+=a+b;
		minup=min(minup +x,a);
		mindown=min(mindown+x,b);
		h=min(h,minup+mindown);
	}
	cout<<sum-n*h;
}
