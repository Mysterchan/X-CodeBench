#include <bits/stdc++.h>
using namespace std;
#define int long long
signed main() {
	int t;
	cin>>t;
	while(t--){
	    int n,m;
	    cin>>n>>m;
	    int arr[m][3];
	    for(int i=0;i<m;i++){
	        for(int j=0;j<3;j++){
	            cin>>arr[i][j];
	    }
	    }
	    vector <int> brr(n+1);
	    brr[0]=1;
	    brr[1]=2;
	    for(int i=2;i<n+1;i++){
	        brr[i]=brr[i-1]+brr[i-2];
	    }
	    int count=0;
	    for(int i=0;i<m;i++){
	        if(arr[i][0]>=brr[n]&&arr[i][1]>=brr[n-1]&&arr[i][2]>=brr[i-1])cout<<1<<" ";
	        else if(arr[i][0]>=brr[n-1]&&arr[i][1]>=brr[n]&&arr[i][2]>=brr[n-1])cout<<1<<" ";
	        else if (arr[i][0]>=brr[n-1]&&arr[i][1]>=brr[n-1]&&arr[i][2]>=brr[n])cout<<1<<" ";
	        else cout<<0<<" ";
	    }
	    cout<<endl;
	}

}
