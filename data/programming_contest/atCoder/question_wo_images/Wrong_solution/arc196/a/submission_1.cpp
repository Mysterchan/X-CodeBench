#include<bits/stdc++.h>
#define int long long
using namespace std;
const int N=3e5+5;
int n,a[N],dp[N],p[N];
signed main(){
	ios::sync_with_stdio(0),cin.tie(0),cout.tie(0);
	cin>>n;
	if(n>3000)return 0;
	for(int i=1;i<=n;i++){
		cin>>a[i];
		p[i]+=abs(a[i]-a[i-1]);
		for(int j=1;j<i;j++){
			if(i-j%2==1){
				dp[i]=max(dp[i],dp[j]);
			} 
			else{
				dp[i]=max(dp[i],dp[j-1]+abs(a[i]-a[j])+p[i-1]-p[j]);
			}
		}
	}
	cout<<dp[n];
	return 0;
}