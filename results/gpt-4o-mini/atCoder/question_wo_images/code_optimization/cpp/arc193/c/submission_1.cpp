#include <bits/stdc++.h>
using namespace std;
#define MOD 998244353

int main() {
    int H, W;
    long long C;
    cin >> H >> W >> C;

    if (H == 1 || W == 1) {
        cout << C % MOD << endl;
        return 0;
    }

    long long totalWays = (C * C) % MOD;  // Each cell can be colored independently
    long long rowsAndCols = (H + W - 1) % MOD;  // Each cell affects its row and column

    long long answer = (totalWays * rowsAndCols) % MOD;  // Total configurations of rows and columns mod the number
    cout << answer << endl;

    return 0;
}
