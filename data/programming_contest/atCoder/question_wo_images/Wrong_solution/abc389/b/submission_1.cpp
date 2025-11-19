#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (n); i++)

long long kaijo(long long n) {
    if (n > 1) return n * kaijo(n - 1);
    else return 1;
}

int main() {
    long long x;
    cin >> x;

    rep (i, x) {
        long long y = kaijo(i);
        if (y > x) return 0;
        else if (kaijo(i) == x) {
            cout << i << endl;
            return 0;
        }
    }
}