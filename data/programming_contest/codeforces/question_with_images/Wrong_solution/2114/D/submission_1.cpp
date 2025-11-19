#include <bits/stdc++.h>
using namespace std;

const int N = 2e6;
#define ll long long
#define all(x) (x).begin(), (x).end()

ll size(int x1, int x2, int y1, int y2){
    return (x1 - x2 + 1) * (y1 - y2 + 1);
}
ll min_ops(int x1, int x2, int y1, int y2){
    return min(x1 - x2 + 1, y1 - y2 + 1);
}

void solve(){
    int n;
    cin >> n;

    vector<pair<int,int>> a(n);
    for(int i = 0; i < n; ++i){
        cin >> a[i].first >> a[i].second;
    }

    if(n == 1){
        cout << 1 << "\n"; return;
    }

    multiset<int> px, py;
    for(int i = 0; i < n; ++i){
        px.insert(a[i].first);
        py.insert(a[i].second);
    }

    ll mn = 1e18, count = px.count(*px.begin());
    if(count == 1){
        int x2 = *next(px.begin()), x1 = *px.rbegin();
        int y1 = *py.rbegin(), y2 = *py.begin();
        ll sz = size(x1, x2, y1, y2);
        if(sz >= n) mn = min(mn, sz);
        else mn = min(mn, sz + min_ops(x1, x2, y1, y2));
    }
    
    count = px.count(*px.rbegin());
    if(count == 1){
        int x1 = *prev(px.rbegin()), x2 = *px.begin();
        int y1 = *py.rbegin(), y2 = *py.begin();
        ll sz = size(x1, x2, y1, y2);
        if(sz >= n) mn = min(mn, sz);
        else mn = min(mn, sz + min_ops(x1, x2, y1, y2));
    }

    count = py.count(*py.begin());
    if(count == 1){
        int x1 = *px.rbegin(), x2 = *px.begin();
        int y2 = *next(py.begin()), y1 = *py.rbegin();
        ll sz = size(x1, x2, y1, y2);
        if(sz >= n) mn = min(mn, sz);
        else mn = min(mn, sz + min_ops(x1, x2, y1, y2));
    }

    count = py.count(*py.rbegin());
    if(count == 1){
        int x1 = *px.rbegin(), x2 = *px.begin();
        int y1 = *prev(py.rbegin()), y2 = *py.begin();
        ll sz = size(x1, x2, y1, y2);
        if(sz >= n) mn = min(mn, sz);
        else mn = min(mn, sz + min_ops(x1, x2, y1, y2));
    }

    cout << mn << "\n";
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int tc;
    cin >> tc;

    while(tc--){
        solve();
    }

    return 0;
}