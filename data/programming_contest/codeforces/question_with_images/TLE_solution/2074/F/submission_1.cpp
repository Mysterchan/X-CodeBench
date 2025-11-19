#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

#define square array<int, 4>

const int M = 3e3+5, MOD = 1e9+7;

bool inside(square a, square b) { // a in b
    return (b[0] <= a[0] && a[1] <= b[1]) && (b[2] <= a[2] && a[3] <= b[3]);
}
bool outside(square a, square b) { // a in b
    return (b[1] <= a[0] || a[1] <= b[0]) || (b[3] <= a[2] || a[3] <= b[2]);
}
 
int find(square a, square x) {
    if (inside(a, x)) {
        return 1;
    }
    if (outside(a, x)) return 0;
    square a1 = square({a[0], (a[0]+a[1])/2, a[2], (a[2]+a[3])/2});
    square a2 = square({a[0], (a[0]+a[1])/2, (a[2]+a[3])/2, a[3]});

    square a3 = square({(a[0]+a[1])/2, a[1], a[2], (a[2]+a[3])/2});
    square a4 = square({(a[0]+a[1])/2, a[1], (a[2]+a[3])/2, a[3]});

    return find(a1, x) + find(a2, x) + find(a3, x) + find(a4, x);
}

signed main() {
    cin.tie(0)->sync_with_stdio(0);

    int t;
    cin >> t;

    while (t--) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;

        int x = max((1 << (int)ceil(log2(b))), (1 << (int)ceil(log2(d))));
        square A = {0, x, 0, x};
        square X = {a, b, c, d};

        cout << find(A, X) << endl;
    }

    return 0;
}
 
