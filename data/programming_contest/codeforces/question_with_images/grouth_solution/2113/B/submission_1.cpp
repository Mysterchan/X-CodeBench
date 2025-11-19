#include <bits/stdc++.h>
using namespace std;
const int c=505;
int w, h, a, b, ax, bx, ay, by;
void solve() {
    cin >> w >> h >> a >> b >> ax >> ay >> bx >> by;
    int jo1=(ax!=bx && abs(ax-bx)%a==0), jo2=(ay!=by && abs(ay-by)%b==0);
    cout << (jo1 || jo2 ? "Yes" : "No") << "\n";
    
}
int main() {
	ios_base::sync_with_stdio(false);
    int w;
    cin >> w;
    while (w--) {
        solve();
    }
}
