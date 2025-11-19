#include<cstdio>
#define TY ll
#define FOR(i,a,b) for(TY i=(a);i<=(b);i++)
#define fOR(i,a,b) for(TY i=(a);i<(b);i++)
using namespace std;
typedef long long ll;
const TY M=998244353;
TY _abs(TY a){return a<0?-a:a;}
TY maxn(TY a,TY b){return a>b?a:b;}
TY minn(TY a,TY b){return a<b?a:b;}
inline void add(TY &x,TY y){if((x+=y)>=M)x-=M;}
TY qp(TY a,TY b){TY ans=1;do{if(1&b)ans=ans*a%M;a=a*a%M;}while(b>>=1);return ans;}
TY qr(){
	char ch=getchar();TY s=0,x=1;
	for(;ch<'0'||ch>'9';ch=getchar())if(ch=='-')x=-1;
	for(;ch>='0'&&ch<='9';ch=getchar())s=s*10+ch-'0';return x*s;
}
void qw(TY a,char ch=0){
	if(a<0){a=-a;putchar('-');}
	if(a>9)qw(a/10);putchar(a%10+'0');if(ch)putchar(ch);
}

TY *fc, *dv, x[6], y[6], ans;

TY C(TY n,TY m){
    if(n<0||m<0)return 0;
    return fc[n+m]*dv[n]%M*dv[m]%M;
}

TY F(TY a,TY b){
	TY p=C(a-x[0],b-y[1]);add(p,C(a-x[1],b-y[0]));p=M-p;
	add(p,C(a-x[0],b-y[0]));add(p,C(a-x[1],b-y[1]));return p;
}

TY G(TY a,TY b){
	TY q=C(x[4]-a,y[5]-b);add(q,C(x[5]-a,y[4]-b));q=M-q;
	add(q,C(x[4]-a,y[4]-b));add(q,C(x[5]-a,y[5]-b));return q;
}

int main(){
    TY W=qr(),H=qr(),L=qr(),R=qr(),D=qr(),U=qr();
    x[0]=L-1;x[1]=L;x[2]=L;x[3]=R;x[4]=R;x[5]=R+1;
    y[0]=D-1;y[1]=D;y[2]=D;y[3]=U;y[4]=U;y[5]=U+1;
    
    TY sz=W+H+2;
    fc=new TY[sz+1];
    dv=new TY[sz+1];
    
    fc[0]=1;
    fOR(i,1,sz+1)fc[i]=fc[i-1]*i%M;
    
    dv[sz]=qp(fc[sz],M-2);
    for(TY i=sz-1;i>=0;i--)dv[i]=dv[i+1]*(i+1)%M;
    
    FOR(i,x[2],x[3])add(ans,M-F(i,y[2]-1)*G(i,y[2])%M*(y[2]+i)%M);
    FOR(i,y[2],y[3])add(ans,M-F(x[2]-1,i)*G(x[2],i)%M*(x[2]+i)%M);
    FOR(i,x[2],x[3])add(ans,F(i,y[3])*G(i,y[3]+1)%M*(y[3]+i+1)%M);
    FOR(i,y[2],y[3])add(ans,F(x[3],i)*G(x[3]+1,i)%M*(x[3]+i+1)%M);
    
    qw(ans);
    delete[] fc;
    delete[] dv;
    return 0;
}