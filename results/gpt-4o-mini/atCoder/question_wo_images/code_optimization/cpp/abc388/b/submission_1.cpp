#include <iostream>
#include <algorithm>
using namespace std;

const int MAXN = 100 + 5;
int n, d;
int t[MAXN], l[MAXN];

int main() {
    cin >> n >> d;
    for (int i = 1; i <= n; ++i)
        cin >> t[i] >> l[i];

    for (int k = 1; k <= d; ++k) {
        int mx = 0;
        for (int i = 1; i <= n; ++i) {
            mx = max(mx, t[i] * (l[i] + k));
        }
        cout << mx << endl;
    }
    return 0;
}