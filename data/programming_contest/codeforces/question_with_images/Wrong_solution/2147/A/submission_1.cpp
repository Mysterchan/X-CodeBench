#include <bits/stdc++.h>
using namespace std;
using int64 = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    if(!(cin >> T)) return 0;
    while(T--){
        int64 x,y;
        cin >> x >> y;

        if(y == 0){
            if(x >= 1) cout << 1 << '\n';
            else cout << -1 << '\n';
            continue;
        }

        long double tmp = sqrt((long double)1 + 4.0L * (long double)y);
        int64 qmax = (int64) floor((tmp - 1.0L) / 2.0L);

        int ans = -1;
        for(int64 q = 1; q <= qmax; ++q){
            int64 minY = q * (q + 1);
            if(minY > y) break;
            if(q * q <= x){
                ans = (int)(2 * q);
                break;
            }
            if((q + 1) * (q + 1) <= x){
                ans = (int)(2 * q + 1);
                break;
            }
        }

        cout << ans << '\n';
    }
    return 0;
}
