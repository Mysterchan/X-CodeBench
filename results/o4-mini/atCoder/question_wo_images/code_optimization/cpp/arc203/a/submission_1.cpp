#include <bits/stdc++.h>
using namespace std;
using int64 = long long;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    while(T--){
        int64 N, M;
        cin >> N >> M;
        int64 half = M / 2;
        int64 ans = half * N + (M % 2);
        cout << ans << "\n";
    }
    return 0;
}