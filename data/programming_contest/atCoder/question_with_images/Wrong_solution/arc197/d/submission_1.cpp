#include<bits/stdc++.h>
#define int long long
#define pii pair<int,int>
#define MP make_pair
#define F first
#define S second
using namespace std;
const int N=403,mod=998244353;
int n,fac[N],ans,f[N];
bitset <N> a[N];
void Main(){
    cin>>n; for (int i=1;i<=n;i++) f[i]=0; ans=1;
    for (int i=1,u;i<=n;i++) for (int j=1;j<=n;j++) cin>>u,a[i][j]=u;
    for (int i=1;i<=n;i++) if (!a[i][1] || !a[1][i]) {cout<<"0\n"; return;}
    for (int i=1;i<=n;i++){
        for (int j=i+1;j<=n;j++){
            if ((a[i]|a[j])!=a[i] && (a[i]|a[j])!=a[j] && (a[i][j] || a[j][i])){
                cout<<"0\n"; return;
            }
        }
    }
    for (int i=2;i<=n;i++){
        if (f[i]) continue; int cnt=1;
        for (int j=i+1;j<=n;j++){
            if (a[i]==a[j]){
                cnt++;
                f[j]=1;
            }
        }
        ans=ans*fac[cnt]%mod;
    }
    cout<<ans<<"\n";
}
signed main(){
    ios::sync_with_stdio(0),cin.tie(0),cout.tie(0);
    fac[0]=1; for (int i=1;i<N;i++) fac[i]=fac[i-1]*i%mod;
    int T; cin>>T; while (T--) Main();
    return 0;
}