#include <bits/stdc++.h>
using namespace std;
const int N = 3005;
const int MOD = 998244353;
int n, ec;
int head[N], to[N<<1], nxt[N<<1];
int d[N][N], pw2[N], pw3[N];
inline void adde(int u,int v){
    to[++ec]=v; nxt[ec]=head[u]; head[u]=ec;
}
struct BS {
    unsigned long long a[N/64+5];
    void clear(){
        int m=(n+63)>>6;
        for(int i=0;i<m;i++) a[i]=~0ULL;
        if(n&63) a[m-1]=(1ULL<<(n&63))-1;
    }
    void reset(){
        int m=(n+63)>>6;
        for(int i=0;i<m;i++) a[i]=0;
    }
    void set1(int i){
        a[i>>6]|=1ULL<<(i&63);
    }
    BS operator&(BS const& o) const {
        BS r; int m=(n+63)>>6;
        for(int i=0;i<m;i++) r.a[i]=a[i]&o.a[i];
        return r;
    }
    BS operator~() const {
        BS r; int m=(n+63)>>6;
        for(int i=0;i<m;i++) r.a[i]=~a[i];
        if(n&63) r.a[m-1]^=~((1ULL<<(n&63))-1);
        return r;
    }
    bool operator==(BS const& o) const {
        int m=(n+63)>>6;
        for(int i=0;i<m;i++) if(a[i]!=o.a[i]) return false;
        return true;
    }
};
struct MyHash {
    size_t operator()(BS const& b) const {
        size_t h=0; int m=(n+63)>>6;
        for(int i=0;i<m;i++)
            h^=b.a[i]+0x9e3779b97f4a7c15ULL+(h<<6)+(h>>2);
        return h;
    }
};
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    pw2[0]=pw3[0]=1;
    for(int i=1;i<N;i++){
        pw2[i]=(pw2[i-1]*2LL)%MOD;
        pw3[i]=(pw3[i-1]*3LL)%MOD;
    }

    int T; cin>>T;
    while(T--){
        cin>>n; ec=0;
        for(int i=1;i<=n;i++) head[i]=0;
        for(int i=1,u,v;i<n;i++){
            cin>>u>>v;
            adde(u,v); adde(v,u);
        }
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++) d[i][j]=-1;
            queue<int> q;
            d[i][i]=0; q.push(i);
            while(!q.empty()){
                int u=q.front(); q.pop();
                for(int e=head[u];e;e=nxt[e]){
                    int v=to[e];
                    if(d[i][v]==-1){
                        d[i][v]=d[i][u]+1;
                        q.push(v);
                    }
                }
            }
        }

        static BS ban[N];
        long long sumF=0;
        for(int k=1;k<n;k++){
            for(int u=1;u<=n;u++){
                ban[u].reset();
                ban[u].set1(u-1);    
                for(int v=1;v<=n;v++)
                    if(d[u][v]>=k) ban[u].set1(v-1);
            }
            unordered_map<BS,int,MyHash> mp, mp2;
            mp.reserve(2048);
            BS all1; all1.clear();
            mp[all1]=1;
            for(int u=1;u<=n;u++){
                mp2.clear();
                for(auto &it: mp){
                    BS s=it.first;
                    int c=it.second;
                    int &r1 = mp2[s];
                    r1=(r1+c)%MOD;
                    BS s2 = s & (~ban[u]);
                    int &r2 = mp2[s2];
                    r2=(r2+c)%MOD;
                }
                mp.swap(mp2);
            }
            long long fk=0;
            for(auto &it: mp){
                int c=it.second;
                const BS &bs=it.first;
                int cnt=0, m=(n+63)>>6;
                for(int i=0;i<m;i++) cnt+=__builtin_popcountll(bs.a[i]);
                fk=(fk + 1LL*c*pw2[cnt])%MOD;
            }
            sumF=(sumF+fk)%MOD;
        }
        long long ans = ((1LL*(n-1)*pw3[n])%MOD - sumF)%MOD;
        if(ans<0) ans+=MOD;
        cout<<ans<<"\n";
    }
    return 0;
}
