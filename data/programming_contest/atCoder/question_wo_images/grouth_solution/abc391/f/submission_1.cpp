#include<bits/stdc++.h>
#define int long long
using namespace std;
inline int read(){
	int f=1,x=0;
	char s=getchar();
	while(s<'0'||s>'9'){
		if(s=='-') f=-1;
		s=getchar();
	}
	while(s>='0'&&s<='9'){
		x=(x<<1)+(x<<3)+(s^48);
		s=getchar();
	}
	return x*f;
}
const int N=2e5+5;
int n,K;
int a[N],b[N],c[N];
priority_queue<int>q;
void Solve(){
	n=read(); K=read();
	for(int i=1;i<=n;i++) a[i]=read();
	for(int i=1;i<=n;i++) b[i]=read();
	for(int i=1;i<=n;i++) c[i]=read();
	sort(a+1,a+n+1,greater<int>());
	sort(b+1,b+n+1,greater<int>());
	sort(c+1,c+n+1,greater<int>());	
	for(int i=1;i<=K&&i<=n;i++)
		for(int j=1;i*j<=K&&j<=n;j++)
			for(int k=1;i*j*k<=K&&k<=n;k++)
				q.push(a[i]*b[j]+b[j]*c[k]+c[k]*a[i]);
	K--;
	while(K--){
		q.pop();
	}
	cout<<q.top();
}
signed main(){
	int T=1;
	while(T--) Solve();
	return 0;
}
