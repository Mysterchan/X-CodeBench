#include<bits/stdc++.h>
using namespace std;
using i64 = long long;
using u64 = unsigned long long;

constexpr i64 inf = 1e9;
constexpr i64 INF = LLONG_MAX;
constexpr int N = 5e5 + 10;
constexpr int P = 676767677;
constexpr int K = 0;
constexpr double eps = 1e-6;

struct info {
    int tag, min, max;
    info() : tag(0), min(0), max(0) {}
    info(int v) : tag(0), min(v), max(v) {}
};

info operator+(info a, info b){
    a.tag = 0;
    a.min = min(a.min, b.min);
    a.max = max(a.max, b.max);
    return a;
}

vector<int> l, r;
vector<info> Info;

void resize(int n) {
    l.resize(n), r.resize(n), Info.resize(n);
    return;
}

void push(int x) {
    if(Info[x].tag == 0) return;
    int a = x << 1, b = x << 1 | 1;
    Info[a].min += Info[x].tag, Info[a].max += Info[x].tag, Info[a].tag += Info[x].tag;
    Info[b].min += Info[x].tag, Info[b].max += Info[x].tag, Info[b].tag += Info[x].tag;
    Info[x].tag = 0;
    return;
}

void pull(int x) {
    Info[x] = Info[x << 1] + Info[x << 1 | 1];
    return;
}

void build(int ll, int rr, int x = 1) {
    l[x] = ll, r[x] = rr, Info[x] = info();
    if(ll == rr) {
        Info[x] = info(ll);
        return;
    }
    push(x);
    int mid = (l[x] + r[x]) >> 1;
    build(l[x], mid, x << 1);
    build(mid + 1, r[x], x << 1 | 1);
    pull(x);
    return;
}

void add(int ll, int rr, int x = 1) {
    if(ll <= l[x] && r[x] <= rr) {
        Info[x].tag++, Info[x].min++, Info[x].max++;
        return;
    }
    push(x);
    int mid = (l[x] + r[x]) >> 1;
    if(ll <= mid) add(ll, rr, x << 1);
    if(rr > mid) add(ll, rr, x << 1 | 1);
    pull(x);
    return;
}

int findfirst(int ll, int rr, int v, int x = 1) {
    if(r[x] < ll || l[x] > rr) return -1;
    if(Info[x].max < v) return -1;
    if(ll <= l[x] && r[x] <= rr && Info[x].min >= v) return l[x];
    push(x);
    int mid = (l[x] + r[x]) >> 1;
    int res = -1;
    if(ll <= mid && res == -1) res = findfirst(ll, rr, v, x << 1);
    if(rr > mid && res == -1)  res = findfirst(ll, rr, v, x << 1 | 1);
    pull(x);
    return res;
}

info getval(int p, int x = 1) {
    if(l[x] == r[x]) return Info[x];
    info ans;
    push(x);
    int mid = (l[x] + r[x]) >> 1;
    if(p <= mid) ans = getval(p, x << 1);
    else ans = getval(p, x << 1 | 1);
    pull(x);
    return ans;
}

int get(int p) {
    return getval(p).min;
}

void solve() {
    int n;
    cin >> n;

    vector<int> l(n), r(n);
    for(int i = 0; i < n; ++i) cin >> l[i] >> r[i];

    resize(N << 2 | 1);
    build(0, N - 1);

    for(int i = 0; i < n; ++i) {
        int ll = findfirst(0, N - 1, l[i]), rr = findfirst(0, N - 1, r[i] + 1);
        if(ll == -1) continue;
        if(rr == -1) rr = N - 1;
        else --rr;
        if(ll <= rr) add(ll, rr);
    }

    int q;
    cin >> q;

    for(int i = 0; i < q; ++i) {
        int x;
        cin >> x;

        cout << get(x) << "\n";
    }
    
    return;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    while(t--) solve();
    return 0;
}