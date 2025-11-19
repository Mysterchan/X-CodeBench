#include<bits/stdc++.h>

using namespace std;
int a[105];
int main(){
	int n;
	cin>>n;
	for(int i=1;i<=n;i++){
		cin>>a[i]; 
	} 
	 
	for(int i=2;i<=n;i++){
		if(a[i]<=a[i-1]){
			cout<<"No";
			return 0;
		}
	}cout<<"Yes";
	return 0;
}
