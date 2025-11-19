#include<bits/stdc++.h>
using namespace std;
const int N=2e6+10;
char a[N];
int dfs(int x,int len){
	if(len==3){
		int cnt=0;
		for(int i=x;i<=x+len-1;i++){
			if(a[i]=='1') cnt++;
		}
		if(cnt>=2) return 1;
		else return 0; 
	} 
	int sum=dfs(x,len/3)+dfs(x+len/3,len/3)+dfs(x+len/3*2,len/3);
	if(sum>=2) return 1;
	else return 0; 
} 
int solve(int x,int len,int col){
	if(len==3){
		int cnt=0;
		for(int i=x;i<=x+len-1;i++){
			if(a[i]=='1') cnt++;
		}
		if(col) return max(0,2-cnt);
		else return max(0,cnt-1);
	}
	int x1=solve(x,len/3,col);
	int x2=solve(x+len/3,len/3,col);
	int x3=solve(x+len/3*2,len/3,col);
	int sum=min(min(x1+x2,x1+x3),x2+x3);
	return sum;
}
int main(){
	ios::sync_with_stdio(0),cin.tie(0),cout.tie(0);
	int n;
	cin>>n;
	for(int i=1;i<=pow(3,n);i++){
		cin>>a[i];
	}
	int e=dfs(1,pow(3,n));
	cout<<solve(1,pow(3,n),e^1);
	return 0;
}
