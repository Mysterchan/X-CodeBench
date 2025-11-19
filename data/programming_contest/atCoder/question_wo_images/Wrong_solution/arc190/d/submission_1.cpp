#include <bits/stdc++.h>
#define int long long
using namespace std;
const int N=105;
int n,p,cnt=0,pw=1;
struct matrix{
	int a[N][N];
	void init(){
		for(int i=1;i<=n;i++)for(int j=1;j<=n;j++)a[i][j]=0;
	}
}A,B,C,res;
matrix operator*(const matrix &a,const matrix &b){
	matrix c;c.init();
	for(int k=1;k<=n;k++)for(int i=1;i<=n;i++)for(int j=1;j<=n;j++){
		c.a[i][j]=(c.a[i][j]+a.a[i][k]*b.a[k][j]%p)%p;
	}
	return c;
}
matrix ksm(matrix a,int b){
	matrix sum=res;
	while(b){
		if(b&1)sum=sum*a;
		a=a*a,b>>=1;
	}
	return sum;
}
signed main(){
	ios::sync_with_stdio(0),cin.tie(0),cout.tie(0);
	cin >>n>>p;
	for(int i=1;i<=n;i++)res.a[i][i]=1;
	for(int i=1;i<=n;i++)for(int j=1;j<=n;j++){
		cin >>A.a[i][j];
		B.a[i][j]=(!A.a[i][j]),C.a[i][j]=A.a[i][j],cnt+=B.a[i][j];
	}
	if(p==2){
		for(int i=1;i<=n;i++)for(int j=1;j<=n;j++)if(!A.a[i][j])A.a[i][j]=1;
		A=ksm(A,p);
		for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++)cout <<A.a[i][j]<<" ";
			cout <<"\n";
		}
		return 0;
	}
	for(int i=1;i<cnt;i++)pw=pw*(p-1)%p;
	A=ksm(A,p);
	for(int i=1;i<=n;i++)for(int j=1;j<=n;j++){
		A.a[i][j]=(A.a[i][j]*pw%p)*(p-1)%p;
	}
	for(int i=1;i<=n;i++)for(int j=1;j<=n;j++)if(i!=j){
		if(p==3&&B.a[i][j])A.a[i][j]=(A.a[i][j]-C.a[j][i]*pw%p+p)%p;
		if(B.a[i][i])A.a[i][j]=(A.a[i][j]-C.a[i][j]*pw%p+p)%p;
		if(B.a[j][j])A.a[i][j]=(A.a[i][j]-C.a[i][j]*pw%p+p)%p;
	}
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++)cout <<A.a[i][j]<<" ";
		cout <<"\n";
	}
	return 0;
}
