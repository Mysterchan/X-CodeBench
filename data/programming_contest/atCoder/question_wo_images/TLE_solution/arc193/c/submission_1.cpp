#include <bits/stdc++.h>
// #include <windows.h>
// #include <bits/extc++.h>
// using namespace __gnu_pbds;
using namespace std;
//#pragma GCC optimize(3)
#define DB double
#define LL long long
#define ULL unsigned long long
#define in128 __int128
#define cint const int
#define cLL const LL
#define For(z,e1,e2) for(int z=(e1);z<=(e2);z++)
#define Rof(z,e1,e2) for(int z=(e2);z>=(e1);z--)
#define For_(z,e1,e2) for(int z=(e1);z<(e2);z++)
#define Rof_(z,e1,e2) for(int z=(e2);z>(e1);z--)
#define inint(e) scanf("%d",&e)
#define inll(e) scanf("%lld",&e)
#define inpr(e1,e2) scanf("%d%d",&e1,&e2)
#define in3(e1,e2,e3) scanf("%d%d%d",&e1,&e2,&e3)
#define outint(e) printf("%d\n",e)
#define outint_(e) printf("%d%c",e," \n"[i==n])
#define outint2_(e,e1,e2) printf("%d%c",e," \n"[(e1)==(e2)])
#define outll(e) printf("%lld\n",e)
#define outll_(e) printf("%lld%c",e," \n"[i==n])
#define outll2_(e,e1,e2) printf("%lld%c",e," \n"[(e1)==(e2)])
#define exc(e) if(e) continue
#define stop(e) if(e) break
#define ret(e) if(e) return
#define ll(e) (1ll*(e))
#define pb push_back
#define ft first
#define sc second
#define pii pair<int,int>
#define pli pair<long long,int>
#define vct vector
#define clean(e) while(!e.empty()) e.pop()
#define all(ev) ev.begin(),ev.end()
#define sz(ev) ((int)ev.size())
#define debug(x) printf("%s=%d\n",#x,x)
#define x0 __xx00__
#define y0 __yy00__
#define y1 __yy11__
#define ffo fflush(stdout)
constexpr LL mod=998244353ll,G=404ll;
// cLL mod=1000000007ll;
// cLL mod[2]={1686688681ll,1666888681ll},base[2]={166686661ll,188868881ll};
template <typename Type> void get_min(Type &w1,const Type w2) { if(w2<w1) w1=w2; } template <typename Type> void get_max(Type &w1,const Type w2) { if(w2>w1) w1=w2; }
template <typename Type> Type up_div(Type w1,Type w2) { return (w1/w2+(w1%w2?1:0)); }
template <typename Type> Type gcd(Type X_,Type Y_) { Type R_=X_%Y_; while(R_) { X_=Y_; Y_=R_; R_=X_%Y_; } return Y_; } template <typename Type> Type lcm(Type X_,Type Y_) { return (X_/gcd(X_,Y_)*Y_); }
template <typename Type> Type md(Type w1,const Type w2=mod) { w1%=w2; if(w1<0) w1+=w2; return w1; } template <typename Type> Type md_(Type w1,const Type w2=mod) { w1%=w2; if(w1<=0) w1+=w2; return w1; }
void ex_gcd(LL &X_,LL &Y_,LL A_,LL B_) { if(!B_) { X_=1ll; Y_=0ll; return ; } ex_gcd(Y_,X_,B_,A_%B_); X_=md(X_,B_); Y_=(1ll-X_*A_)/B_; } LL inv(LL A_,LL B_=mod) { LL X_=0ll,Y_=0ll; ex_gcd(X_,Y_,A_,B_); return X_; }
template <typename Type> void add(Type &w1,const Type w2,const Type M_=mod) { w1=md(w1+w2,M_); } void mul(LL &w1,cLL w2,cLL M_=mod) { w1=md(w1*md(w2,M_),M_); } template <typename Type> Type pw(Type X_,Type Y_,Type M_=mod) { Type S_=1; while(Y_) { if(Y_&1) mul(S_,X_,M_); Y_>>=1; mul(X_,X_,M_); } return S_; }
template <typename Type> Type bk(vector <Type> &V_) { auto T_=V_.back(); V_.pop_back(); return T_; } template <typename Type> Type tp(stack <Type> &V_) { auto T_=V_.top(); V_.pop(); return T_; } template <typename Type> Type frt(queue <Type> &V_) { auto T_=V_.front(); V_.pop(); return T_; }
template <typename Type> Type bg(set <Type> &V_) { auto T_=*V_.begin(); V_.erase(V_.begin()); return T_; } template <typename Type> Type bk(set <Type> &V_) { auto T_=*prev(V_.end()); V_.erase(*prev(V_.end())); return T_; }
mt19937 gen(time(NULL)); int rd() { return abs((int)gen()); }
int rnd(int l,int r) { return rd()%(r-l+1)+l; }

void main_init()
{

}
cint N=410,M=410;
int n,m;
LL d;
LL C[N<<1][N<<1],z[N<<1];
LL dp[N][M];
void init(int len)
{
    For(i,0,len) C[i][0]=1ll;
    For(i,1,len) For(j,1,i) C[i][j]=(C[i-1][j-1]+C[i-1][j])%mod;
    z[0]=1ll; For(i,1,len) z[i]=z[i-1]*d%mod;
}
void main_solve()
{
    inpr(n,m); inll(d);
    if(n==1||m==1)
    {
        outll(d%mod);
        return ;
    }
    init(n+m);
    For(i,0,n) For(j,0,m)
    {
        if(min(i,j)<=1)
        {
            dp[i][j]=((i&&j)?z[(i^j^1)]:1ll);
            continue;
        }
        if(i==n&&j==m)
        {
            For(i2,1,i) For(j2,1,j)
            {
                LL w;
                if(i2&&j2) w=dp[i-i2][j-j2]*d%mod;
                else w=dp[i-i2][j-j2]*z[(i2|j2)]%mod;
                w=w*(C[i][i2]*C[j][j2]%mod);
                // if(op) printf("%d,%d:%lld(%d)\n",i2,j2,w,((i2^j2)&1)?1:-1);
                add(dp[i][j],((i2^j2)&1)?(-w):w);
            }
        }
        else
        {
            For(i2,0,i) For(j2,0,j)
            {
                LL w;
                if(i2&&j2) w=(dp[i-i2][j-j2]*d%mod)*(C[i][i2]*C[j][j2]%mod);
                else w=(dp[i-i2][j-j2]*z[(i2|j2)]%mod)*(C[i][i2]*C[j][j2]%mod);
                // if(op) printf("%d,%d:%lld(%d)\n",i2,j2,w,((i2^j2)&1)?1:-1);
                add(dp[i][j],((i2^j2)&1)?w:(-w));
            }
        }
    }
    outll(dp[n][m]);
}
int main()
{
    main_init();
	main_solve();
    return 0;
}
/*

*/
