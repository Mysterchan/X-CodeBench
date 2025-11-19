#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main() {
    int n;
    cin >> n;
    vector<ll> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    vector<ll> ans;
    vector<ll> b;
    auto f = [&](auto f, int k) {
        if (k == n) {
            ll sum = 0;
            for (ll x : b) sum ^= x;
            ans.push_back(sum);
            return;
        }
        for (int i = 0; i < (int)b.size(); i++) {
            b[i] += a[k];
            f(f, k + 1);
            b[i] -= a[k];
        }
        b.push_back(a[k]);
        f(f, k + 1);
        b.pop_back();
        return;
    };

    f(f, 0);
    sort(ans.begin(), ans.end());
    ans.erase(unique(ans.begin(), ans.end()), ans.end());
    cout << (int)ans.size() << endl;
    return 0;
}
