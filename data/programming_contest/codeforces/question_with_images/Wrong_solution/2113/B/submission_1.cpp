#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int w, h, a, b;
    cin >> w >> h >> a >> b;
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    x1+=a;
    y1+=b;
    x1 = max(x1, 0LL);
    y1 = max(y1, 0LL);
    x2 = max(x2, 0LL);
    y2 = max(y2, 0LL);
    if(x2 > x1) {
        if((x2 - x1) % a == 0) {
            cout << "YES" << endl;
            return;
        }
        else {
            if(y2 > y1) {
                if((y2 - y1) % b == 0) {
                    cout << "YES" << endl;
                    return;
                }
            }
        }
    }  
    else {
        if((y2 - y1) % b == 0) {
            cout << "YES" << endl;
            return;
        }
    }
    cout << "NO" << endl;
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) solve();
}
