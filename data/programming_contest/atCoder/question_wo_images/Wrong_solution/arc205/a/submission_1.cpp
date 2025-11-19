#include<bits/stdc++.h>
#define endl '\n'
using namespace std;
typedef long long ll;
const int maxn = 506;
ll i,j,p,q,n,m,k,t,Q; 
string s;
int a[maxn][maxn];
int dp[maxn][maxn];
void solve()
{
    cin>>n>>Q;
    for(i=1;i<=n;i++){
        cin>>s;
        for(j=1;j<=n;j++){
            a[i][j] = (s[j-1] == '.');
        }
    }
    for(i=2;i<=n;i++){
        for(j=2;j<=n;j++){
            int p = (a[i][j] && a[i][j-1] && a[i-1][j] && a[i-1][j-1]);
            dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + p;
            
        }
    }
    for(i=1;i<=n;i++){
        for(j=1;j<=n;j++){
            cout<<dp[i][j]<<" ";    
        }
        cout<<endl;
    }
    while(Q--){
        int x,y,x2,y2;
        cin>>x>>x2>>y>>y2;
        cout<<dp[x2][y2] - dp[x][y2] - dp[x2][y] + dp[x][y]<<endl;
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
    return 0;
}