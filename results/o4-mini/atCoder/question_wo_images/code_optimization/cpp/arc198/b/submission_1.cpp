#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    while(T--){
        long long X, Y, Z;
        cin >> X >> Y >> Z;
        bool ok;
        if (Y < 2LL * Z) {
            ok = (X >= Z);
        } else {
            ok = (2LL * X >= Y);
        }
        cout << (ok ? "Yes\n" : "No\n");
    }
    return 0;
}