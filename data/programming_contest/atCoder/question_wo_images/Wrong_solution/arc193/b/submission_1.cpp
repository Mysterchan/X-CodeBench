#include <bits/stdc++.h>
using namespace std;

int n,s[100007],dp[100007][3];
const int mod=998244353;
signed main(){
	cin>>n;
	char ch;
	for(int i=1;i<=n;i++) cin>>ch,s[i]=ch-'0';
	int ans=0;
	for(int j=0;j<3;j++){
		dp[0][0]=dp[0][1]=dp[0][2]=0;
		dp[0][j]=1;
		for(int i=1;i<=n;i++){
			dp[i][0]=dp[i][1]=(0ll+dp[i-1][0]+dp[i-1][1]+dp[i-1][2])%mod;
			dp[i][2]=dp[i-1][2];
			if(s[i]) dp[i][2]=(dp[i][2]+dp[i][0])%mod;
		}
		ans=(ans+dp[n][j])%mod;
	}
	cout<<(ans-2+mod)%mod<<endl;
}