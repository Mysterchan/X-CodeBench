#include<bits/stdc++.h>
#define int long long
using namespace std;
const int N=3e5+5;
int n,m,x,y,ans=1e18,f[N],cnt[N];
char a[N];
void XOR(int n,int *a,bool p){
	for(int i=1;i<n;i<<=1){
		for(int j=0;j<n;j+=i<<1){
			for(int k=0;k<i;k++){
				x=a[j+k];
				y=a[i+j+k];
				a[j+k]=x+y;
				a[i+j+k]=x-y;
				if(p){
					a[j+k]/=2;
					a[i+j+k]/=2;
				}
			}
		}
	}
}
signed main(){
	scanf("%lld%lld",&n,&m);
	for(int i=1;i<=n;i++){
		scanf("%s",a+1);
		x=0;
		for(int j=1;j<=m;j++) x=(x<<1)|(a[j]-'0');
		cnt[x]++;
	}
	for(int i=0;i<1<<m;i++) f[i]=min(__builtin_popcountll(i),__builtin_popcountll(i^((1<<m)-1)));
	XOR(1<<m,cnt,0);
	XOR(1<<m,f,0);
	for(int i=0;i<1<<m;i++) f[i]*=cnt[i];
	XOR(1<<m,f,1);
	for(int i=0;i<1<<m;i++) ans=min(ans,f[i]);
	printf("%lld",ans);
	return 0;
}