#include <bits/stdc++.h>

using namespace std;

void dbg_out() { cerr << endl; }
template<typename Head, typename... Tail>
void dbg_out(Head H, Tail... T) { cerr << ' ' << H; dbg_out(T...); }
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)

using ll = long long;

template<typename S, typename T> void smax(S &a, const T &b) { if (a < b) a = b; }
template<typename S, typename T> void smin(S &a, const T &b) { if (a > b) a = b; }

#define rng_init mt19937 rng(chrono::steady_clock::now().time_since_epoch().count())
#define rng_seed(x) mt19937 rng(x)
#define all(x) (x).begin(), (x).end()
#define sz(x) (int) (x).size()

const int MXN = 1e5 + 5, INF = 1e9 + 5;

const string PLAYER1{"Fennec"};
const string PLAYER2{"Snuke"};

void solve() {
    int N;
    cin >> N;
    
    vector<int> A(N);
    int odd_cnt = 0;
    for (auto &x : A) {
        cin >> x;
        odd_cnt += x & 1;
    }
        
    if (N == 3 && odd_cnt > 0) {
        cout << PLAYER1 << "\n";
        return;
    }

    if (N <= 2 || odd_cnt % 2 == 0) {
        cout << PLAYER2 << "\n";
        return;
    }
    
    cout << PLAYER1 << "\n";
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int TC = 1;
    while (TC--) solve();
}