#include<bits/stdc++.h>
using namespace std;
#define int long long
const int N=2e5+10;
int a[N],b[N],c[N];
bool cmp(int x,int y){
	return x>y;
}
vector<int>q; 
signed main(){
	ios::sync_with_stdio(0),cin.tie(0),cout.tie(0);
	int n,K;
	cin>>n>>K;
	for(int i=1;i<=n;i++){
		cin>>a[i];
	}
	sort(a+1,a+n+1,cmp);
	for(int i=1;i<=n;i++){
		cin>>b[i];
	}
	sort(b+1,b+n+1,cmp);
	for(int i=1;i<=n;i++){
		cin>>c[i];
	}
	sort(c+1,c+n+1,cmp);
	for(int i=1;i<=K&&i<=n;i++){
		for(int j=1;i*j<=K&&j<=n;j++){
			for(int k=1;i*j*k<=K&&k<=n;k++){
				q.push_back(a[i]*b[j]+a[i]*c[k]+b[j]*c[k]);
			}
		} 
	}
	sort(q.begin(),q.begin()+K+1,cmp);
	cout<<q[K-1];
	return 0;
}
