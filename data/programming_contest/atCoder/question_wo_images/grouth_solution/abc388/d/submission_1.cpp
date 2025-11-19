#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);

    int n; cin >> n;
    vector<int> a(n); for(auto &x: a) cin >> x;
    vector<int> delta(n + 2, 0);

    for(int i = 0;i < n; ++i){
        if(i > 0) delta[i] += delta[i-1];
        a[i] += delta[i];
        int r = a[i] - (n - i - 1);
        delta[min(n, i + a[i] + 1)]--;
        a[i] = max(0, r);
        delta[i+1]++;
    }

    for(auto &x: a) cout << x << " ";
    cout << "\n";
    return 0;
}

