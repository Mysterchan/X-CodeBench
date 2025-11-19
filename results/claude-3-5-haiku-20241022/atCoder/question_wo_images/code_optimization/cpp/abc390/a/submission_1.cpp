#include<bits/stdc++.h>
using namespace std;

int main()
{
	int a[5];
	for(int i=0;i<5;++i) cin>>a[i];
	
	int cnt=0;
	for(int i=0;i<4;++i){
		if(a[i]>a[i+1]) ++cnt;
	}
	
	if(cnt!=1){
		cout<<"No";
		return 0;
	}
	
	for(int i=0;i<4;++i){
		if(a[i]>a[i+1]){
			swap(a[i],a[i+1]);
			break;
		}
	}
	
	bool sorted=true;
	for(int i=0;i<4;++i){
		if(a[i]>a[i+1]){
			sorted=false;
			break;
		}
	}
	
	cout<<(sorted?"Yes":"No");
	return 0;
}