#include <bits/stdc++.h>
using namespace std;
typedef __int128 LL;
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
#define debug(x) cout << "======" << x << "========" << endl;
#define ls(p) p<<1
#define rs(p) p<<1|1
#define Run_Time cerr<<(clock()-Time)*1.0/CLOCKS_PER_SEC<<"s\n"
#define Run_Memory cerr<<abs(&M2-&M1)/1024.0/1024.0<<"MB\n"
#define int long long
#define endl "\n"
const ll inf = 0x3f3f3f3f3f3f3f3f;
const int N = 1e4+30;
const long double PI = 3.141592653589793238462643383279502884L;
const long double eps = 1e-8;

bool M1;

ll fast_power(ll x,ll n,ll mod){
    ll ans = 1;x%=mod;while(n){if(n&1)ans = (ans*x)%mod;x = (x*x)%mod;n >>=1;}return (ans+mod)%mod;
}
ll mod =  998244353;


pair<int,int> getpos(int x,int y,int v,int n){
    if(n==0)return{x,y};
    int dx = (1<<(n-1))*(1<<(n-1)); //2
    int d = (1<<(n-1));
    if(v<=dx)return getpos(x,y,v,n-1);
    if(v<=2*dx)return getpos(x+d,y+d,v-dx,n-1);
    if(v<=3*dx)return getpos(x+d,y,v-2LL*dx,n-1);
    return getpos(x,y+d,v-3LL*dx,n-1);
}

int getval(int x, int y, int n) {
    if (n==0) return 1;
    int d = (1<<(n-1));
    int s = d*d;
    if (x<=d&&y<=d)return getval(x,y,n-1);
    else if (x>d&&y>d)return s + getval(x-d,y-d, n-1);
    else if (x>d)return 2LL*s+getval(x-d,y, n-1);
    else return 3LL*s + getval(x,y-d, n-1);
}


void solve() {
    int n,q;
    cin>>n>>q;
    while(q--){
        string op;cin>>op;
        int x,y;
        if(op=="->"){
            cin>>x>>y;
            cout<<getval(x,y,n)<<endl;
        }else{
            cin>>x;
            auto [a,b] = getpos(1,1,x,n);
            cout<<a<<" "<<b<<endl;
        }
    }
}


bool M2;

signed main(){
    ios::sync_with_stdio(false);
    cin.tie(0);cout.tie(0);
    int Time=clock();
    int test=1;
    cin>>test;
    while(test--) solve();
    Run_Memory; Run_Time;
    return 0;
}