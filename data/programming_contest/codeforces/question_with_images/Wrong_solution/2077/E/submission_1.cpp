
#include <bits/stdc++.h>
#define pb push_back
#define fi first
#define se second
#define endl '\n'

using namespace std;
using ll = long long;
using ii = pair <int, int>;
using vi = vector <int>;

const int N = 2e5 + 5;
const int mod = 1e9 + 7;

void maxl(auto &a, auto b) {a = max(a, b);}
void minl(auto &a, auto b) {a = min(a, b);}

int n, a[N], len[N << 2];
long long st[N << 2][2], lzs[N << 2][2];
int lza[N << 2][2];

void up(int s){
    for (int t : {0, 1}){
        st[s][t] = 0;
        for (int c : {s << 1, s << 1 | 1})
            st[s][t] += st[c][t];
    }
}

void build(int s, int l, int r){
    for (int t : {0, 1})
        st[s][t] = 0, lza[s][t] = 0, lzs[s][t] = 0;

    len[s] = r - l + 1;

    if (l == r) return;

    int mid = l + r >> 1;
    build(s << 1, l, mid);
    build(s << 1 | 1, mid + 1, r);

    up(s);
}

void ass_n(int s, int t){
    st[s][t] = 0;
    lza[s][t] = 1;
    lzs[s][t] = 0;
}

void add_n(int s, int t, int val){
    st[s][t] += 1ll * val * len[s];
    lzs[s][t] += val;
    lza[s][t] = 0;
}

void down(int s){
    for (int t : {0, 1}){
        for (int c : {s << 1, s << 1 | 1}){
            if (lza[s][t]) ass_n(c, t);
            else add_n(c, t, lzs[s][t]);
        }
        lza[s][t] = 0;
        lzs[s][t] = 0;
    }
}

void add(int t, int u, int v, int val, int s = 1, int l = 1, int r = n){
    if (u <= l && r <= v){
        add_n(s, t, val);
        return;
    }

    down(s);
    int mid = l + r >> 1;

    if (mid >= u) add(t, u, v, val, s << 1, l, mid);
    if (mid < v) add(t, u, v, val, s << 1 | 1, mid + 1, r);

    up(s);
}

void ass(int t, int u, int v, int s = 1, int l = 1, int r = n){
    if (u <= l && r <= v){
        ass_n(s, t);
        return;
    }

    down(s);
    int mid = l + r >> 1;

    if (mid >= u) ass(t, u, v, s << 1, l, mid);
    if (mid < v) ass(t, u, v, s << 1 | 1, mid + 1, r);

    up(s);
}

long long get(int t, int u, int s = 1, int l = 1, int r = n){
    if (l == r) return st[s][t];

    down(s);
    int mid = l + r >> 1;

    if (mid >= u) return get(t, u, s << 1, l, mid);
    return get(t, u, s << 1 | 1, mid + 1, r);
}

void solve(){
    cin >> n;
    long long ans = 0;

    build(1, 1, n);

    for (int i = 1; i <= n; ++ i){
        cin >> a[i];
        int cur = i & 1;


        add(cur, 1, i, a[i]);


        int l = 1, r = i, ptr = 0;
        while (l <= r){
            int mid = l + r >> 1;
            if (get(!cur, mid) < a[i]) r = mid - 1;
            else ptr = mid, l = mid + 1;
        }



        if (ptr) add(!cur, 1, ptr, -a[i]);


        if (ptr < i) ass(!cur, ptr + 1, i);

        ans += st[1][0] + st[1][1];

    }

    cout << ans << "\n";
}

int main(){
    if (fopen("pqh.inp", "r")){
        freopen("pqh.inp", "r", stdin);
        freopen("pqh.out", "w", stdout);
    }
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int t = 1; cin >> t;
    while (t --) solve();
    return 0;
}
