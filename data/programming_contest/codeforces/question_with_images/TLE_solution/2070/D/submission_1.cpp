#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define F(a,b ,c ) for (int a=b ;a <=c ;a++)
int n,m;
const int maxsize =3e5+10;
int cur=1 ;
int dot [maxsize];
int edge [maxsize<<1 ];
int to [maxsize<<1 ];
int  ans= 0 ;
const int mod =998244353;
int deep[maxsize];
int siz[maxsize];
int cnt [maxsize];
void addedge(int a ,int b ){edge [cur]=dot [a ];dot [a ]=cur ;to[cur++]=b ; }
void dfs(int x,int f ){
    siz [x ]=1 ;
    deep[x ]=deep[f ]+1 ;
    cnt[deep[x ]]++;
    for ( int i=dot [ x ];i;i=edge [i ]){
        int t=to[i];
        if (t!=f){
            dfs(t, x );
            siz[x ]++;
        }
    }
}
void cal(int x ,int f ){
    ans=1ll* (ans+cnt [deep[x ]+1])%mod ;
    for ( int i=dot [x ];i;i=edge [i ]){
        int t=to[i];
        if(t!=f){
            cal(t,x );
            ans--;
        }
    }

}
void dfs_2(int x ,int f){
    for ( int i=dot [x ];i;i=edge [i ]){
        int t=to[i];
        if(t!=f){
            dfs_2(t,x );
        }
    }
    dot [x ]= 0 ;
    to[x]= 0 ;
    edge [x ]= 0 ;
    cnt[deep[x ]]= 0 ;
    deep[x]=0 ;
}
void solve (){
    cin>>n;
    int a;
    cur =1 ;
    F(i,2,n){
        cin>>a;
        addedge ( a, i );
        addedge ( i,a  );
    }
    dfs (1 , 0 );
    ans=siz[1 ];
    cal(1 , 0 );
    dfs_2 (1 , 0 );
    cout<<ans<<'\n';
}
int main(){
    ios_base::sync_with_stdio (false );
    cin.tie (0);
    int t ;
    cin>>t ;
    while (t --)solve ();
}