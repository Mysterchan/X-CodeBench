#include<bits/stdc++.h>
using namespace std;
int n,a[500010],b[500010];
int main(){
	cin>>n;
	for(int i=1;i<=n;i++){
		cin>>a[i];
		b[i]=a[i]-a[i-1];
	}
	for(int i=1;i<=n;i++){
		for(int j=i+1;j<=n;j++){
			if(a[i]>0) a[i]--,a[j]++;
			else continue;
		}
		cout<<a[i]<<' ';
	}
	return 0;
}