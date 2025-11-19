#include <bits/stdc++.h>
using namespace std;
const int N=5e5+1;
int n,a[N],ans;
int main(){
	cin>>n;
	for(int i=1;i<=n;i++)cin>>a[i];
	sort(a+1,a+n+1);
	for(int i=1;i<=n;i++){
		int l=i+1,r=n+1;
		while(l<r){
			int mid=l+(r-l)/2;
			if(2LL*a[i]<=a[mid])l=mid+1;
			else r=mid;
		}ans+=l-i-1;
	}cout<<ans;
	return 0;
}