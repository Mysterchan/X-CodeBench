#include <bits/stdc++.h>
#define int long long
#define pii pair<int,int>
#define x first
#define y second
#define all(x) (x).begin(),(x).end()

using namespace std;

const int N=2010,mod=998244353;
char ar[N][N];
int n,m,len[2];
int f[2][2][N];

void get(int op,int id){
    int l=1-2*len[op^1],r=1;
    int tmp=0;
    while(1){
        int mid=l+r>>1;

        if(r>=1 and r<=m)tmp=(tmp+f[op][op^1][r])%mod;

        if(mid>=1 and mid<=m){
            if(ar[id][mid]=='X')f[1][op][mid]=tmp;
            else f[1][op][mid]=0;
        }else if(mid>m)break;

        if(l>=1 and l<=m)tmp=((tmp-f[op][op^1][l])%mod+mod)%mod;
        l++;r++;
    }
}

signed main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin>>T;
    while(T--){
        cin>>n>>m>>len[0];
        len[1]=(int)sqrt(len[0]*len[0]-1);
        for(int i=n;i>=1;i--){
            for(int j=1;j<=m;j++){
                char c;
                cin>>c;
                ar[i][j]=c;
            }
        }
        for(int i=1;i<=m;i++){
            if(ar[1][i]=='X')f[1][0][i]=1;
            else f[1][0][i]=0;
        }
        get(1,1);
        for(int i=2;i<=n;i++){
            for(int j=1;j<=m;j++){
                f[0][0][j]=f[1][0][j];
                f[0][1][j]=f[1][1][j];
            }
            get(0,i);
            get(1,i);
        }
        int ans=0;
        for(int i=1;i<=m;i++){
            ans=(ans+f[1][1][i])%mod;
        }
        cout<<ans<<'\n';
    }
    return 0;
}

