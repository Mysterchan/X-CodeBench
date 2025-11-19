// LUOGU_RID: 199177742
#include<bits/stdc++.h>
#define int long long
using namespace std;
const int N=1e6+10;
const int p=998244353,y=3,ny=332748118;
int n;
int r[N],a[N],ans[N],f[N],g[N];
int ksm(int a,int b=p-2){
	int ans=1;
	for(;b;b>>=1,a=a*a%p) if(b&1) ans=ans*a%p;
	return ans;
}
void NTT(int *a,int len,int type){
	for(int i=1;i<len;i++) if(i<r[i]) swap(a[i],a[r[i]]);
	for(int mid=1;mid<len;mid<<=1){
		const int wn=ksm((type?y:ny),(p-1)/(mid<<1));
		for(int R=mid<<1,j=0;j<len;j+=R){
			int w(1);
			for(int k=0;k<mid;k++,w=w*wn%p){
				int x=a[j+k],y=a[j+k+mid]*w%p;
				a[j+k]=(x+y)%p;
				a[j+k+mid]=(x+p-y)%p;
			}
		}
	}
	if(type) return;
	int inv=ksm(len);
	for(int i=0;i<len;i++) a[i]=a[i]*inv%p;
}
void inv(int *a,int *b,int len){
	if(len==1) {b[0]=ksm(a[0]);return;}
	inv(a,b,(len+1)>>1);
	int m=len<<1;
	int limit,l;
	for(limit=1,l=0;limit<m;limit<<=1,l++);
	for(int i=1;i<limit;i++) r[i]=(r[i>>1]>>1)|((i&1)<<(l-1));
	for(int i=0;i<len;i++) f[i]=a[i];
	for(int i=len;i<limit;i++) f[i]=0;
	NTT(f,limit,1),NTT(b,limit,1);
	for(int i=0;i<limit;i++) b[i]=b[i]*((2+p-f[i]*b[i]%p)%p)%p;
	NTT(b,limit,0);
	for(int i=len;i<limit;i++) b[i]=0;
}
void mul(int*f,int *g,int l1,int l2){
	int limit,l;
	for(limit=1,l=0;limit<=l1+l2;limit<<=1,l++);
	for(int i=1;i<limit;i++) r[i]=(r[i>>1]>>1)|((i&1)<<(l-1));
	NTT(f,limit,1),NTT(g,limit,1);
	for(int i=0;i<limit;i++) f[i]=f[i]*g[i]%p;
	NTT(f,limit,0);
	for(int i=limit-1;i>=1;i--) f[i]=f[i-1]*ksm(i,p-2)%p;
}
int h[N];
void ln(int *a,int *b,int len){
	for(int i=1;i<len;i++) h[i-1]=a[i]*i%p;
	inv(a,b,len);
	mul(b,h,len,len-1);
	b[0]=0;
}
void expp(int *a,int *b,int len){
	if(len==1) {b[0]=1;return;}
	expp(a,b,(len+1)>>1);
	int m=len<<1,limit,l;
	for(limit=1,l=0;limit<m;limit<<=1,l++);
	for(int i=0;i<limit;i++) g[i]=0;
	ln(b,g,len);
	for(int i=len;i<limit;i++) g[i]=0;
	for(int i=0;i<len;i++) f[i]=a[i];
	for(int i=len;i<limit;i++) f[i]=0;
	for(int i=1;i<limit;i++) r[i]=(r[i>>1]>>1)|((i&1)<<(l-1));
	NTT(f,limit,1),NTT(g,limit,1),NTT(b,limit,1);
	for(int i=0;i<limit;i++) b[i]=((1-g[i]+p)%p+f[i])%p*b[i]%p;
	NTT(b,limit,0);
	for(int i=len;i<limit;i++) b[i]=0;
}
int pr[N],vis[N],cnt;
signed main(){
	cin>>n;
	for(int i=2;i<=3e5;i++){
		if(!vis[i]) pr[++cnt]=i;
		for(int j=1;j<=cnt&&pr[j]*i<=3e5;j++){
			vis[i*pr[j]]=1;
			if(!(i%pr[j])) break;
		}
	}
	a[1]=n;
	for(int i=2;i<=cnt;i++) a[pr[i]]=n*((p+1)/2)%p;
	expp(a,ans,n+10);
	int an=ans[n];
	for(int i=1;i<=n;i++) an=an*i%p;
	cout<<an*ksm(n*n%p,p-2)%p;
	return 0;
}
