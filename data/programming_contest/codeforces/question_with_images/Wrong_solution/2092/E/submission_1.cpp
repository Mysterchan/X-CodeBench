
#include<bits/stdc++.h>
using namespace std;

#define int long long
const int MOD=1e9+7;
const int INF=1e18;

int bin_pow(int a, int b){
	int ans=1;
	while(b){
		if(b&1){
			ans*=a;
			ans%=MOD;
		}
		a*=a;
		a%=MOD;
		b>>=1;
	}
	return ans;
}

bool cust(vector<int>&a, vector<int>&b){
	int d1=a[0]+a[1];
	int d2=b[0]+b[1];
	return d1<d2;
}

signed main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t;
	cin>>t;
	while(t--){
		int n, m, k;
		cin>>n>>m>>k;
		vector<vector<int>> v(k,vector<int>(3));
		int cnt=0;
		for(int i=0; i<k; i++){
			cin>>v[i][0]>>v[i][1]>>v[i][2];
		}
		sort(v.begin(),v.end(),cust);
		for(int i=0; i<k-1; i++){
			for(int j=i+1; j<=min(k-1,i+4); j++){
				int rm=abs(v[i][0]-v[j][0])+abs(v[i][1]-v[j][1]);
				if(rm==1 && v[i][2]!=v[j][2]) cnt++;
			}
		}
		int rm=n*m;
		rm%=MOD;
		rm-=k;
		rm%=MOD;
		rm+=MOD;
		rm%=MOD;
		int ans=(rm<=1?bin_pow(2,rm):bin_pow(2,rm-1));
		if(rm==0){
			if(cnt%2==0) cout<<1<<'\n';
			else cout<<0<<'\n';
		}
		else cout<<ans<<'\n';
	}
}