#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while(T--){
        long long N, M;
        cin >> N >> M;
        long long q = (M - 1) / 2;
        long long r = M - 2 * q;
        long long ans = q * N + r;
        cout << ans << '\n';
    }
    return 0;
}