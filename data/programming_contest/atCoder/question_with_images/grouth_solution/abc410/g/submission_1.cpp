#include <bits/stdc++.h>
using namespace std;
using pii = pair<int,int>;
#define mkp make_pair 
#define fs first 
#define sc second

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
    vector<pii> v;
    int n;
    cin >> n;
    for (int i = 1, a, b; i <= n; i++) {
        cin >> a >> b;
        if (a > b) swap(a, b);
        v.emplace_back(a,b);
        v.emplace_back(b,a+n*2);
    }

    sort(v.begin(), v.end()); reverse(v.begin(), v.end());
    vector<int> v2;
    for (auto [_,x] : v) {
        if (v2.empty() or x > v2.back()) v2.push_back(x);
        else {
            auto it = lower_bound(v2.begin(), v2.end(), x);
            *it=x;
        }
    }
    cout << v2.size() << '\n';
}