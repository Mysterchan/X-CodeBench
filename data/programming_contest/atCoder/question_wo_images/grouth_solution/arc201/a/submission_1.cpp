#include<bits/stdc++.h>
#define int long long 
#define MAXN 200005 
int gi(){
	char c;int x=0,f=0;
	while(!isdigit(c=getchar()))f|=(c=='-');
	while(isdigit(c))x=(x*10)+(c^48),c=getchar();
	return f?-x:x;
}
std::mt19937 rnd(std::random_device{}());
#define pr std::pair<int,int>
#define all(x) (x).begin(),(x).end()
#define mem(x,w) memset(x,w,sizeof(x))
#define sz(x) (int)((x).size())
#define eb emplace_back
#define fi first
#define se second
template<class T>void cxk(T&a,T b){a=a>b?a:b;}
template<class T>void cnk(T&a,T b){a=a<b?a:b;}
int n,a[MAXN],b[MAXN],c[MAXN];
void work(){
	n=gi();int t1=0,t2=0,tz=0;
	for(int i=1;i<=n;i++){
		a[i]=gi(),b[i]=gi(),c[i]=gi();
		if(a[i]+c[i]<=b[i])t1+=a[i],t2+=c[i];
		else{
			int k1=std::min(b[i],a[i]),k2=std::min(b[i]-k1,c[i]);
			t1+=k1,t2+=k2,tz+=std::min(k1,c[i]-k2);
		}
	}
	if(t1<=t2)printf("%lld\n",t1);
	else{
		if(t1-tz<=t2+tz)printf("%lld\n",(t1+t2)/2);
		else printf("%lld\n",std::min(t1-tz,t2+tz));
	}
}
signed main(){
	int t=gi();while(t--)work();
	return 0;
}
