#include<cstdio>
#define TY ll
#define MAXN 2000004
#define FOR(i,a,b) for(TY i=(a);i<=(b);i=-~i)
#define fOR(i,a,b) for(TY i=(a);i<(b);i=-~i)
#define ROF(i,a,b) for(TY i=(a);i>=(b);i=~-i)
#define rOF(i,a,b) for(TY i=(a);i>(b);i=~-i)
#define EDG(i,u) for(TY i=hed[u];i;i=nxt[i])
using namespace std;
typedef long long ll;
const TY M=1e9+7;
typedef unsigned long long ull;
TY _abs(TY a){return a<0?-a:a;}
TY maxn(TY a,TY b){return a>b?a:b;}
TY minn(TY a,TY b){return a<b?a:b;}
inline void updmx(TY &x,TY y){if(x<y)x=y;}
inline void updmn(TY &x,TY y){if(x>y)x=y;}
inline void add(TY &x,TY y){if((x+=y)>=M)x-=M;}
TY gcd(TY a,TY b){return b?gcd(b,a%b):a;}
TY qp(TY a,TY b){TY ans=1;do{if(1&b)ans=ans*a%M;a=a*a%M;}while(b>>=1);return ans;}
char getc(){char ch=getchar();while(ch==' '||ch=='\n'||ch=='\r')ch=getchar();return ch;}
TY qr(){
	char ch=getchar();TY s=0,x=1;
	for(;ch<'0'||ch>'9';ch=getchar())if(ch=='-')x=-1;
	for(;ch>='0'&&ch<='9';ch=getchar())s=s*10+ch-'0';return x*s;
}void qw(TY a){if(a>9)qw(a/10);putchar(a%10+'0');}
void qw(TY a,char ch){
	if(a<0){a=-a;putchar('-');}
	if(a>9)qw(a/10);putchar(a%10+'0');if(ch)putchar(ch);
}TY fc[MAXN],dv[MAXN],x[6],y[6],ans;
TY C(TY n,TY m){return fc[n+m]*dv[n]%M*dv[m]%M;}
TY F(TY a,TY b){
	TY p=C(a-x[0],b-y[1]);add(p,C(a-x[1],b-y[0]));p=M-p;
	add(p,C(a-x[0],b-y[0]));add(p,C(a-x[1],b-y[1]));return p;
}TY G(TY a,TY b){
	TY q=C(x[4]-a,y[5]-b);add(q,C(x[5]-a,y[4]-b));q=M-q;
	add(q,C(x[4]-a,y[4]-b));add(q,C(x[5]-a,y[5]-b));return q;
}int main(){
	fOR(i,fc[0]=dv[0]=dv[1]=1,MAXN)fc[i]=fc[i-1]*i%M;
	fOR(i,2,MAXN)dv[i]=M-M/i*dv[M%i]%M;
	fOR(i,3,MAXN)dv[i]=dv[i-1]*dv[i]%M;
	fOR(i,0,6)x[i]=qr();--x[0];++x[5];
	fOR(i,0,6)y[i]=qr();--y[0];++y[5];
	FOR(i,x[2],x[3])add(ans,M-F(i,y[2]-1)*G(i,y[2])%M*(y[2]+i)%M);
	FOR(i,y[2],y[3])add(ans,M-F(x[2]-1,i)*G(x[2],i)%M*(x[2]+i)%M);
	FOR(i,x[2],x[3])add(ans,F(i,y[3])*G(i,y[3]+1)%M*(y[3]+i+1)%M);
	FOR(i,y[2],y[3])add(ans,F(x[3],i)*G(x[3]+1,i)%M*(x[3]+i+1)%M);
	qw(ans);return 0;
}