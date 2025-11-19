#include<bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i,n) for(ll i=0;i<ll(n);i++)
#define rep2(i,m,n) for(ll i=ll(m);i<ll(n);i++)
using vl = vector<ll>;
using vvl = vector<vl>;
using vvvl = vector<vvl>;
using pl = pair<ll,ll>;
using vpl = vector<pl>;
using vvpl = vector<vpl>;
#define pb push_back

const long double EPS = 0.0000000001;
const ll INF = 1000000000000000000;
const double pi = std::acos(-1.0);

__int128 read_int128(){
    string S;
    cin >> S;
    int N = S.size();
    int st = 0;
    bool minus = false;
    if(S[0] == '-'){
        minus = true;
        st = 1;
    }
    __int128 res = 0;
    rep2(i,st,N) res = res*10+int(S[i]-'0');
    if(minus) res *= -1;
    return res;
}

std::ostream &operator<<(std::ostream &dest, __int128_t value) {
    std::ostream::sentry s(dest);
    if (s) {
      __uint128_t tmp = value < 0 ? -value : value;
      char buffer[128];
      char *d = std::end(buffer);
      do {
          --d;
          *d = "0123456789"[tmp % 10];
          tmp /= 10;
      } while (tmp != 0);
      if (value < 0) {
          --d;
          *d = '-';
      }
      int len = std::end(buffer) - d;
      if (dest.rdbuf()->sputn(d, len) != len) {
          dest.setstate(std::ios_base::badbit);
      }
    }
    return dest;
}

void Yes(){ cout << "Yes" << endl; }
void No(){ cout << "No" << endl; }

template<class T> bool chmin(T& a,T b){
    if(a > b){
        a = b;
        return true;
    }
    else return false;
}

template<class T> bool chmax(T& a,T b){
    if(a < b){
        a = b;
        return true;
    }
    else return false;
}

template<class T> size_t HashCombine(const size_t seed,const T &v){
    return seed^(std::hash<T>()(v)+0x9e3779b9+(seed<<6)+(seed>>2));
    }

template<class T,class S> struct std::hash<std::pair<T,S>>{
    size_t operator()(const std::pair<T,S> &keyval) const noexcept {
        return HashCombine(std::hash<T>()(keyval.first), keyval.second);
    }
};

template<class T> struct std::hash<std::vector<T>>{
    size_t operator()(const std::vector<T> &keyval) const noexcept {
        size_t s=0;
        for (auto&& v: keyval) s=HashCombine(s,v);
        return s;
    }
};

int main(){
    ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    ll N,M,X;
    cin >> N >> M >> X;
    vvl G(N),RG(N);
    rep(i,M){
        int u,v;
        cin >> u >> v;
        u--;
        v--;
        G[u].emplace_back(v);
        RG[v].emplace_back(u);
    }
    vvl dist(N,vl(2,INF));
    dist[0][0] = 0;
    priority_queue<pair<ll,pl>,vector<pair<ll,pl>>,greater<pair<ll,pl>>> que;
    que.push(make_pair(0,make_pair(0,0)));
    while(!que.empty()){
        ll d = que.top().first;
        int v = que.top().second.first;
        int f = que.top().second.second;
        que.pop();
        if(d > dist[v][f]) continue;
        for(auto nv:G[v]){
            if(f == 0){
                if(chmin(dist[nv][0],d+1)){
                    que.push(make_pair(d+1,make_pair(nv,0)));
                }
            }
            else{
                if(chmin(dist[nv][0],d+1+X)){
                    que.push(make_pair(d+1+X,make_pair(nv,0)));
                }
            }
        }
        for(auto nv:RG[v]){
            if(f == 0){
                if(chmin(dist[nv][1],d+1+X)){
                    que.push(make_pair(d+1+X,make_pair(nv,1)));
                }
            }
            else{
                if(chmin(dist[nv][1],d+1)){
                    que.push(make_pair(d+1,make_pair(nv,1)));
                }
            }
        }
    }
    cout << min(dist[N-1][0],dist[N-1][1]) << endl;
}