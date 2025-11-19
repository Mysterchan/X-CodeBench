#include<bits/stdc++.h>
using namespace std;
#define PII pair<int,int>
#define PLII pair<long long,long long>
#define i64 long long
#define u64 unsigned long long
#define lson rt<<1
#define rson rt<<1|1
const int maxn=200205;
mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
i64 n,k;
int num0=0;
bitset<32>b;
void solve()
{
    cin>>n>>k;
    b=n;
    int p=31;
    num0=0;
    while(b[p]==0)p--;
    for(int i=p;i>=0;i--){
        if(b[i]==0)num0++;
    }
    if((1ll<<num0)<k){
        cout<<"-1\n";
        return ;
    }
    k--;
    for(int i=0;i<=p;i++){
        if(b[i]==0)b[i]=k%2,k>>=1;
    }
    i64 ans=b.to_ullong();
    cout<<ans;
    cout<<"\n";
    return ;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int T=1;
    cin>>T;
    while(T--)
    solve();
    return 0;
}