#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ull = unsigned long long;
using pii = pair<int,int>;
using pli = pair<ll,int>;
using pil = pair<int,ll>;
using pll = pair<ll,ll>;
using vi = vector<int>;
#define endl '\n'
#define pb push_back
#define eb emplace_back
#define fi first
#define se second
#define sz(v) ((int)(v).size())
#define all(v) v.begin(), v.end()

const ll mod=998244353;
ll fact[200001],h,w,t;
ll inv(ll x)
{
    ll d[60];
    d[0]=x;
    for(int i=1;i<60;i++)
        d[i]=d[i-1]*d[i-1]%mod;
    ll ret=1;
    for(int i=0;i<60;i++)
    {
        if((mod-2)>>i&1)
            ret=ret*d[i]%mod;
    }
    return ret;
}
ll gcd(ll a,ll b)
{
    if(a<b)
        swap(a,b);
    if(b==0)
        return a;
    else
        return gcd(b,a%b);
}
ll comb(int n,int r)
{
    return fact[n]*inv(fact[r])%mod*inv(fact[n-r])%mod;
}
int main()
{
    fact[0]=1;
    for(int i=1;i<=200000;i++)
        fact[i]=fact[i-1]*i%mod;
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    t=1;
    while(t--)
    {
        cin>>h>>w;
        if(h%2==0||w%2==0)
        {
            if(w%2==0)
            {
                int a;
                while(1)
                    a++;
            }
            cout<<0<<'\n';
            continue;
        }
        ll ans=0;
        for(int i=1;i<=h;i+=2)
        {
            if(gcd(i,w)==1)
            {
                ans+=comb(h,(i+h)/2);
                ans%=mod;
            }
        }
        cout<<ans*2%mod<<'\n';
    }
}
