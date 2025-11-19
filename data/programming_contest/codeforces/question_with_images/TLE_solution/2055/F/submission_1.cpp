#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return true; } return false; }
template<class T>bool chmin(T &a, const T &b) { if (b<a) { a=b; return true; } return false; }
#define vi vector<int>
#define vl vector<ll>
#define vii vector<pair<int,int>>
#define vll vector<pair<ll,ll>>
#define vvi vector<vector<int>>
#define vvl vector<vector<ll>>
#define vvii vector<vector<pair<int,int>>>
#define vvll vector<vector<pair<ll,ll>>>
#define vst vector<string>
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define mkunique(x) sort(all(x));(x).erase(unique(all(x)),(x).end())
#define fi first
#define se second
#define mp make_pair
#define si(x) int(x.size())
const int mod=998244353,MAX=300005,INF=15<<26;

bool ren(vll S){
    int N=si(S);
    for(int i=1;i<N;i++){
        ll l=max(S[i-1].fi,S[i].fi),r=min(S[i-1].se,S[i].se);
        if(l>r) return false;
    }
    return true;
}

bool goudou(vll A,vll B){
    int N=si(A);
    ll a=A[0].fi,b=B[0].fi;
    for(int i=1;i<N;i++){
        A[i].fi-=a;
        A[i].se-=a;
        B[i].fi-=b;
        B[i].se-=b;
    }
    A[0]=mp(0,A[0].se-a);
    B[0]=mp(0,B[0].se-b);
    return A==B;
}

bool solve(vll S){
    ll N=si(S);
    {
        vll A,B;
        bool ok=true;
        for(auto [a,b]:S){
            if((b-a+1)&1){
                ok=false;
            }
            A.pb(mp(a,(a+(b-a+1)/2-1)));
            B.pb(mp(b-(b-a+1)/2+1,b));
        }
        if(ok) ok&=ren(A);
        if(ok) ok&=ren(B);
        if(ok) ok&=goudou(A,B);
        if(ok) return true;
    }
    
    ll sum=0;
    for(auto [a,b]:S) sum+=b-a+1;
    
    ll sum2=0;
    for(int i=0;i<N;i++){
        auto [a,b]=S[i];
        
        if(i&1) sum2-=(b-a+1);
        else sum2+=(b-a+1);
    }
    
    for(ll dh=1;dh<N;dh++){
        if(dh+dh>N) break;
        if((dh&1)&&sum2) continue;
        vll A,B;
        bool ok=true;
        
        for(int i=0;i<N;i++){
            if(i<dh){
                A.pb(S[i]);
            }else if(i<N-dh){
                ll len=A[i-dh].se-A[i-dh].fi+1;
                
                B.pb(mp(S[i].fi,S[i].fi+len-1));
                A.pb(mp(B.back().se+1,S[i].se));
                if(A.back().fi>A.back().se){
                    ok=false;
                    break;
                }
            }else{
                ll len=A[i-dh].se-A[i-dh].fi+1;
                B.pb(mp(S[i].fi,S[i].fi+len-1));
                
                if(B.back().se!=S[i].se){
                    ok=false;
                    break;
                }
            }
        }
        
        if(ok&&ren(A)&&ren(B)&&goudou(A,B)) return true;
    }
    
    return false;
}

int main(){
    
    std::ifstream in("text.txt");
    std::cin.rdbuf(in.rdbuf());
    cin.tie(0);
    ios::sync_with_stdio(false);
    
    int Q;cin>>Q;
    while(Q--){
        ll N;cin>>N;
        vll S(N);
        for(int i=0;i<N;i++){
            ll l,r;cin>>l>>r;
            S[i]=mp(l,r);
        }
        bool ans=false;
        
        for(int q=0;q<2;q++){
            if(solve(S)) ans=true;
            if(ans) break;
            for(int i=0;i<N;i++){
                swap(S[i].fi,S[i].se);
                S[i].fi=1000000001-S[i].fi;
                S[i].se=1000000001-S[i].se;
            }
        }
        
        if(ans) cout<<"YES\n";
        else cout<<"NO\n";
    }
}


