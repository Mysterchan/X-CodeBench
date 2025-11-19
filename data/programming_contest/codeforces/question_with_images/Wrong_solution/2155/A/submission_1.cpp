#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ld = long double;
#define dbg(x) cout << #x << " = " << x << endl;
#define all(v) v.begin(), v.end()

mt19937 rng((int) chrono::steady_clock::now().time_since_epoch().count());

void test(){
    int w;
    cin>>w;
    int l=0;
    int ans=0;
    while(w > 1){
        ans++;
        l += w/2;
        w = (w+1)/2;
    }

    while(l > 1){
        ans++;
        l = (l+1)/2;
    }

    assert(w <= 1);
    assert(l <= 1);
    if(w && l) ans++;

    cout<<ans<<"\n";
}

int32_t main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    cin >> t;
    while(t--){
        test();
    }

    return 0;
}