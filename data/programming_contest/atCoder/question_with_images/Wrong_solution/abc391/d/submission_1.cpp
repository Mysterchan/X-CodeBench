#include <bits/stdc++.h>
using ll = long long;
#define  MECHAN ios::sync_with_stdio(0),cin.tie(nullptr),cout.tie(nullptr);
#define all(s) s.begin() , s.end()
#define allr(s) s.rbegin() , s.rend()
using namespace std;
const ll mod = 1e9 + 7 , N = 1e3+5 ,
INF = 1e16 , _INF = -1e16 ;

template<typename T>
using pq = priority_queue<T, vector<T>,greater<T>>;

string DIR = "DURL";
int dx[]={ 1 , 2 , -1 , -2 , 0 , 0 , 0 , 0  } , dy[] = { 0  , 0  , 0 , 0 , 1 , 2 , -1 , -2 };

vector<ll> val (5e5 , 0);
using T = int ;
class dsu {
    vector<T> s , leader ;
public:
    dsu(T n){
        s.resize(n+1 ,1);
        leader.resize(n+1 , -1 );
    }
    T get( T node ) {
        return leader[node]==-1? node : get(leader[node]);
    }
    bool equal ( T node1 , T node2){
        return get(node1)== get(node2);
    }
    T size (T node){
        return s[node];
    }
    T maxi (T node){
        ll value = get(node);
        return val[value] ;
    }
    void join(T node1 , T node2){
        T a = get(node1) , b= get(node2);
        if(a==b) return;
        if(s[a] > s[b]) swap(a,b);
        val[b]= max(maxi(a) , maxi(b));
        leader[a]=b;
        s[b]+= s[a];
    }
};

void solve() {
    ll n , w  , x , y , q , time = 1 ;
    cin >> n >> w ;

    w++ ;
    dsu d(5e5) ;
    vector<vector<int>> columns(w + 1) ;
    vector<ll> disappear (n+1 , 0) ;

    for (int i =1 ; i<=n ; i++) {
        cin >> x >> y ;

        columns[x % w].push_back(i) ;
        val[i] = max <ll>(val[i] , columns[x % w].size() - y ) ;
        d.join( columns[x % w].size() + 2e5 + 1 , i ) ;
        if (d.size(d.get(i)) == w ) disappear[d.get(i)] = time , time ++ ;

    }

    cin>>q ;
    while (q--) {
        cin >> x >> y ;
        int res = d.get(y) ;
        if (disappear[res] && disappear[res] + val[res] < x ) cout<<"No" ;
        else cout<<"Yes" ;
        cout<<"\n" ;
    }
}

int main() {
    MECHAN

    ll test = 1 ;
    for (int i = 1 ; i<= test ; i++) {
        solve();
        cout<<"\n";
    }

}