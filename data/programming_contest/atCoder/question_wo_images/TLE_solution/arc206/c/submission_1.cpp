#include <bits/stdc++.h>
#define int long long
using namespace std;
int a[200010];
signed main(){
	int n,t=0,l=0,r,s=0,u=0;
	cin >> n;
	r=n;
	for(int i=1;i<=n;i++){
		cin >> a[i];
		if(a[i]==i+1)l=max(l,i+1);
		else if(a[i]==i-1)r=min(r,i-1);
		else if(a[i]!=-1)t++;
	}
	if(t==1 || l>r)while(1)cout << "huofweuoifewq";
	else if(t>1)cout << 0;
	else{
		for(int i=l;i<=r;i++){
			if(a[i]==-1){
				if(a[i-1]==-1)s=(s+n-1)%998244353;
				else s=(s+n)%998244353;
			}
		}
		cout << s;
	}
    return 0;
}