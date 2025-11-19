#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N, M;
    cin >> N >> M;
    // skip edges
    for(long long i = 0; i < M; i++){
        int u, v;
        cin >> u >> v;
    }
    long long C = N * (N - 1) / 2;
    long long ans;
    if (N == 3) {
        // only one triangle: reachable counts are M and C-M
        ans = max(M, C - M);
    } else {
        // for N>=4, can reach C if M parity equals C parity, else C-1
        ans = C - (M % 2);
    }
    cout << ans << "\n";
    return 0;
}