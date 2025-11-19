#include<bits/stdc++.h>
using namespace std;

int main() {
    int t; cin >> t;
    while (t--) {
        int n, rk, ck, rd, cd, max_val = -1;
        cin >> n >> rk >> ck >> rd >> cd;
        if (rd > rk) max_val = max(max_val, rd);
        else max_val = max(max_val, n - rd);
        if (cd > ck) max_val = max(max_val, cd);
        else max_val = max(max_val, n - cd);
        cout << max_val << endl;
    }
    return 0;
}