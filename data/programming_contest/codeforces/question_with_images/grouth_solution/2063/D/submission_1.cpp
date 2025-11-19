#include "bits/stdc++.h"
#pragma GCC optimize ("O3")
#pragma GCC target ("sse4")
 
using namespace std;
 
typedef long long ll;
typedef long double ld;
typedef complex<ld> cd;
 
typedef pair<int, int> pi;
typedef pair<ll,ll> pl;
typedef pair<ld,ld> pd;
 
typedef vector<int> vi;
typedef vector<ld> vd;
typedef vector<ll> vl;
typedef vector<pi> vpi;
typedef vector<pl> vpl;
typedef vector<cd> vcd;

template<class T> using pq = priority_queue<T>;
template<class T> using pqg = priority_queue<T, vector<T>, greater<T>>;
 
#define FOR(i, a, b) for (int i=a; i<(b); i++)
#define F0R(i, a) for (int i=0; i<(a); i++)
#define FORd(i,a,b) for (int i = (b)-1; i >= a; i--)
#define F0Rd(i,a) for (int i = (a)-1; i >= 0; i--)
#define trav(a,x) for (auto& a : x)
#define uid(a, b) uniform_int_distribution<int>(a, b)(rng)
 
#define sz(x) (int)(x).size()
#define mp make_pair
#define pb push_back
#define f first
#define s second
#define lb lower_bound
#define ub upper_bound
#define all(x) x.begin(), x.end()
#define ins insert

 
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

#ifdef DEBUG
#define dbg(x...) cerr << "\e[91m"<<__func__<<":"<<__LINE__<<" [" << #x << "] = ["; _print(x); cerr << "\e[39m" << endl;
#else
#define dbg(x...)
#endif


const int MOD = 1000000007;
const char nl = '\n';
const int MX = 100001; 

void solve() {
    int N, M; cin >> N >> M;
    vl A(N), B(M);
    F0R(i, N) {
        cin >> A[i];
    }
    F0R(i, M) cin >> B[i];
    sort(all(A)); sort(all(B));
    vl Xs, Ys;
    F0R(i, N/2) {
        Xs.pb(A[N-i-1]-A[i]);
    }
    F0R(i, M/2) {
        Ys.pb(B[M-i-1]-B[i]);
    }
    ll cur = 0;
    vl ans;
    int px = 0, py = 0;
    while (true) {
        if (px < sz(Xs) && (py >= sz(Ys) || Xs[px] >= Ys[py])) {
            cur += Xs[px];
            px++;
        } else if (py < sz(Ys)) {
            cur += Ys[py];
            py++;
        } else break;
        while (2*px+py > N) {
            if (px == 0) goto done;
            px--;
            cur -= Xs[px];
            if (py == sz(Ys)) goto done;
            cur += Ys[py];
            py++;
        }
        while (2*py+px > M) {
            if (py == 0) goto done;
            py--;
            cur -= Ys[py];
            if (px == sz(Xs)) goto done;
            cur += Xs[px];
            px++;
        }
        if (2*px+py > N) goto done;
        ans.pb(cur);
    }
    done:
    ;
    cout << sz(ans) << nl;
    trav(a, ans) {
        cout << a << " ";
    }
    cout << nl;

}
 
int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);

    int T = 1;
    cin >> T;
    while(T--) {
        solve();
    }

	return 0;
}

