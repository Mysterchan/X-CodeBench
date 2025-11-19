#include<iostream>
#include<vector>
#include<set>
#include<tuple>
#include<string>
#include<set>
#include<queue>
#include<deque>
#include<map>
#include<algorithm>
#include<bitset>
#include<math.h>
#include<stack>
#include<cstring>
#include<unordered_map>
#include<unordered_set>
#include<iomanip>
#include<cstdint>
#include<chrono>
using namespace std;
#define ll long long
#define fi first
#define se second
#define pl pair<ll,ll>
#define mpl make_pair
#define pb push_back
#define vi vector<ll>
#define vvi vector<vector<ll>>
#define vpl vector<pl>
#define vvpl vector<vpl>
#define all(x) (x).begin(),(x).end()
#define all1(x) (x).begin()+1,(x).end()
#define bitcount(x) __builtin_popcount(x)
#define fast                       \
 ios_base::sync_with_stdio(0);      \
 cin.tie(0);                         \
 cout.tie(0);
ll mod=998244353;
ll binexp(ll a,ll b)
{
    a%=mod;
    ll ans=1;
    while(b>0)
    {
        if(b%2)
        {
            ans=(ans*a)%mod;
        }
        a=(a*a)%mod;
        b>>=1;
    }
    return ans;
}
ll mod_inv(ll n)
{
    return binexp(n,mod-2);
}
ll gcd(ll a, ll b)
{
    return b == 0 ? a : gcd(b, a % b);
}
struct CustomHash {
    static std::uint64_t murmur64(std::uint64_t x) {
        x ^= x >> 33;
        x *= 0xff51afd7ed558ccd;
        x ^= x >> 33;
        x *= 0xc4ceb9fe1a85ec53;
        x ^= x >> 33;
        return x;
    }

    size_t operator()(std::uint64_t x) const {
        static const std::uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return murmur64(x + FIXED_RANDOM);
    }
};
const ll N=1e6+1;
ll isprime[N];
ll spf[N];
void pcheck(ll n)
{
    for(ll i=0;i<=n;i++)
    {
        isprime[i]=1;
        spf[i]=1;
    }
    for(ll i=2;i<=n;i++)
    {
        if(isprime[i]==1)
        {
            spf[i]=i;
            for(ll j=2*i;j<=n;j+=i)
            {
                isprime[j]=0;
                if(spf[j]==1)
                {
                    spf[j]=i;
                }
            }
        }
    }
}

int main()
{
    fast;
    ll t;
    cin>>t;
    while(t--)
    {
        ll a,b,c,d;
        cin>>a>>b>>c>>d;
        if(a+b==c+d)
        {
            cout<<"Yes"<<endl;
        }
        else
        {
            cout<<"No"<<endl;
        }
    }
    return 0;
}

