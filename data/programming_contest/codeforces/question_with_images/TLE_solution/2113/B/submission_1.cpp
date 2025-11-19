#include <iostream>
using namespace std;
using ll = long long;
 
void solve() {
    ll w, h, a, b;
    cin >> w >> h >> a >> b;
 
    ll xa, ya, xb, yb;
    cin >> xa >> ya >> xb >> yb;
      for(int i=0;i<a;i++);
    bool ver = false;
bool hor = false;
        if (abs(xa - xb) % a == 0) {
            if (xa == xb) {
                if (abs(ya - yb) % b == 0)
                    ver = true;
            } else {
                ver = true;
            }
        }
     for(int i=0;i<b;i++)
    
    if (abs(ya - yb) % b == 0) {
        if (ya == yb) {
            if (abs(xa - xb) % a == 0)
                hor = true;
        } else {
            hor = true;
        }
    }
 
    
    if (hor || ver)
        cout << "Yes\n";
    else
        cout << "No\n";
}
 
signed main() {
    
    ll t;
    cin >> t;
    while (t--) {
        solve();
    }
 
    return 0;
}