#include<bits/stdc++.h>
bool Mbg;
using namespace std;
#define vec vector
#define pb push_back
#define eb emplace_back
#define siz(vec) ((int)(vec).size())
#define all(vec) (vec).begin(),(vec).end()
template<class T>
void operator +=(vec<T> &a,T b){a.push_back(b);}
template<class T>
void operator --(vec<T> &a){a.pop_back();}
#define pii pair<int,int>
#define x first
#define y second
#define mp make_pair
#define exc(exp) if(exp)continue;
#define stop(exp) if(exp)break;
#define ret(exp) if(exp)return;
#define deb(var) cerr<<#var<<'='<<(var)<<"; "
#define debl(var) cerr<<#var<<'='<<(var)<<";\n"
#define ins insert
#define era erase
#define lb lower_bound
#define ub upper_bound
#define int long long
#define inf (long long)(1e18)
template<class T>
bool Min(T &x,T y){return x>y?x=y,1:0;}
template<class T>
bool Max(T &x,T y){return x<y?x=y,1:0;}
const int mod=998244353;
void Add(int &x,int y){x=x+y<mod?x+y:x+y-mod;}
void Dec(int &x,int y){x=x>=y?x-y:x-y+mod;}
int fpm(int x,int y){
    int ans=1;for(;y;y>>=1,(x*=x)%=mod)if(y&1)(ans*=x)%=mod;return ans;
}

int n;
bool nsp[250010];
int fac[250010],inv[250010];
int C(int n,int m){
    return fac[n]*inv[m]%mod*inv[n-m]%mod;
}

int f[250010];
vec<int> prm;
void work(){
    cin>>n;
    for(int i=2;i<=n;i++){
        if(!nsp[i]){
            for(int j=i+i;j<=n;j+=i){
                nsp[j]=1;
            }
        }
    }
    for(int i=3;i<=n;i++){
        if(!nsp[i]){
            prm+=i;
        }
    }


    fac[0]=fac[1]=inv[0]=inv[1]=1;
    for(int i=2;i<=n;i++){
        fac[i]=fac[i-1]*i%mod;
        inv[i]=(mod-mod/i)*inv[mod%i]%mod;
    }
    for(int i=3;i<=n;i++){
        inv[i]=inv[i]*inv[i-1]%mod;
    }
    const int inv2=fpm(2,mod-2);

    f[0]=1;
    for(int i=1;i<=n;i++){
        f[i]=f[i-1]*n%mod;

        (f[i-1]*=inv[i-1])%=mod;

        int coe=fac[i-1]*inv2%mod*n%mod;
        
        for(int j:prm){
            stop(j>i);
            (f[i]+=f[i-j]*j%mod*coe)%=mod;
        }

    }
    cout<<f[n]*fpm(n,mod-3)%mod<<'\n';
}
bool Med;
signed main(){
    ios::sync_with_stdio(0),
    cin.tie(0),cout.tie(0);
    int T=1;while(T--)work();
}