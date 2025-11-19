#include <bits/stdc++.h>
using namespace std;
using int64 = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    while(T--){
        int64 N, K;
        cin >> N >> K;
        // Find highest bit position b (0-based)
        int b = 0;
        if(N > 0){
            b = 63 - __builtin_clzll(N);
        }
        // Collect zero-bit positions below b
        int zero_cnt = 0;
        int zero_pos[64];
        for(int i = 0; i < b; ++i){
            if(((N >> i) & 1LL) == 0){
                zero_pos[zero_cnt++] = i;
            }
        }
        // Total compatible r's is 2^zero_cnt
        // Check overflow: zero_cnt <= 63 so safe
        int64 total = 1LL << zero_cnt;
        if(K > total){
            cout << "-1\n";
            continue;
        }
        // Compute the (K-1)-th r by mapping bits of K-1 to zero_pos
        int64 r = 0;
        int64 k0 = K - 1;
        for(int i = 0; i < zero_cnt; ++i){
            if((k0 >> i) & 1LL){
                r |= (1LL << zero_pos[i]);
            }
        }
        // X = N + r
        int64 X = N + r;
        cout << X << "\n";
    }
    return 0;
}