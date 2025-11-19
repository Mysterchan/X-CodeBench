#include <bits/stdc++.h>
using namespace std;
using ull = unsigned long long;
using i128 = __int128_t;

i128 count_snake_upto(ull x) {
    if (x < 10) return 0;
    string s = to_string(x);
    int L = s.size();
    // precompute powers: powd[d][k] = d^k
    static ull powd[10][20];
    for (int d = 0; d <= 9; d++) {
        powd[d][0] = 1;
        for (int k = 1; k < L; k++) {
            powd[d][k] = powd[d][k-1] * (ull)d;
        }
    }
    i128 ans = 0;
    // lengths less than L
    for (int n = 2; n < L; n++) {
        for (int d = 1; d <= 9; d++) {
            ans += powd[d][n-1];
        }
    }
    int x0 = s[0] - '0';
    // same length, msd < x0
    for (int d = 1; d < x0; d++) {
        ans += powd[d][L-1];
    }
    // msd == x0, digit DP for positions 1..L-1
    for (int i = 1; i < L; i++) {
        int di = s[i] - '0';
        int rem = L - 1 - i;
        int max_t = min(x0 - 1, di - 1);
        if (max_t >= 0) {
            // choices t in [0..max_t]
            i128 cnt = (i128)(max_t + 1) * (i128)powd[x0][rem];
            ans += cnt;
        }
        // check if we can continue tight (t == di)
        if (di > x0 - 1) {
            // cannot match di, path ends
            return ans;
        }
        // else continue with t == di
    }
    // if we completed all positions, x itself is a snake
    ans += 1;
    return ans;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    ull L, R;
    cin >> L >> R;
    i128 res = count_snake_upto(R);
    if (L > 0) res -= count_snake_upto(L - 1);
    // output res
    ull out = (ull)res;
    cout << out << "\n";
    return 0;
}