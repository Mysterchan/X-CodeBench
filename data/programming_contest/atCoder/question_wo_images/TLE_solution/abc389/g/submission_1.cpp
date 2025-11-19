#include <bits/stdc++.h>
using namespace std;
inline long long read(){
	long long x=0; char ch; bool f=0;
	while(((ch=getchar())<'0'||ch>'9')&&ch!='-') ;
	if(ch=='-') f=1;
	else x=ch^48;
	while((ch=getchar())>='0'&&ch<='9') x=(x<<1)+(x<<3)+(ch^48);
	return f?-x:x;
}
bool st1;
const int N=35;
int n,mod;
int f[N][N*N/2][2][N+N][N];
long long C[N*N][N*N];
inline void ad(int &x,int y){
	(x+=y)>=mod?x-=mod:0;
}
long long inv[N*N],S[N][N][N*N],jc[N*N];
void re(int n){
	for(int i=0;i<=n*N;i++){
		C[i][0]=1;
		for(int j=1;j<=i;j++) C[i][j]=(C[i-1][j-1]+C[i-1][j])%mod;
	}
	inv[0]=inv[1]=jc[0]=jc[1]=1;
	for(int i=2;i<=n;i++) jc[i]=i*jc[i-1]%mod,inv[i]=(mod-mod/i)*inv[mod%i]%mod;
	for(int m=1;m<=n;m++){
		for(int d=1;d<=n-m;d++){
			if(d==1){
				for(int e=d;e<=n*(n-1)/2;e++) S[m][d][e]=C[m][e];
			}
			else{
				for(int e=d;e<=n*(n-1)/2;e++){
					for(int t=1;t<=e;t++) S[m][d][e]=S[m][d][e]+S[m][d-1][e-t]*(C[d-1+m][t]-C[d-1][t])%mod;
					S[m][d][e]=(S[m][d][e]%mod+mod)%mod;
				}
			}
		}
	}
}
bool st2;
int main(){
	n=read(),mod=read();
	re(n);
	int M=n*(n-1)/2;
	f[1][0][0][1+n][1]=1;
	int c=0;
	for(int i=1;i<n;i++){
		for(int j=0;j<=M;j++){
			for(int k=0;k<2;k++){
				for(int l=1;l<2*n;l++){
					for(int m=1;m<=i;m++){
						if(f[i][j][k][l][m]){
							c++;
							for(int d=1;d<=n-i;d++){
								for(int e=d;e<=M-j;e++){
									ad(f[i+d][j+e][k^1][l+((k&1)?1:-1)*d][d],f[i][j][k][l][m]*C[n-i][d]%mod*S[m][d][e]%mod);
								}
							}
						}
					}
				}
			}
		}
	}
	for(int m=n-1;m<=n*(n-1)/2;m++){
		int ans=0;
		for(int i=1;i<=n;i++){
			ad(ans,f[n][m][0][n][i]);
			ad(ans,f[n][m][1][n][i]);
		}
		printf("%d ",(ans%mod+mod)%mod);
	}puts("");
	return 0;
}
