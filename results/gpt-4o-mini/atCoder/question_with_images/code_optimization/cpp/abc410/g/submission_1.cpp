#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define vi vector<int>
#define pii pair<int, int>
const int N = 4e5 + 5;

struct Chord {
    int l, r;
    bool operator < (const Chord &x) const { return r < x.r; }
};

int main() {
    ios::sync_with_stdio(0), cin.tie(0);
    
    int n; cin >> n;
    vector<Chord> chords(n);
    for(int i = 0; i < n; ++i) {
        int x, y; cin >> x >> y;
        if(x > y) swap(x, y);
        chords[i] = {x, y};
    }

    sort(chords.begin(), chords.end());
    vi f(n + 1, 0);
    int mx = 0;
    vector<int> dp(2 * n + 1, 0);
    
    for(int i = 0; i < n; ++i) {
        f[i] = dp[chords[i].l] + 1;
        for(int j = chords[i].l; j <= 2 * n; ++j) {
            dp[j] = max(dp[j], f[i]);
        }
    }

    for(int i = 0; i < n; ++i) {
        f[i] += dp[chords[i].r];
        mx = max(mx, f[i]);
    }
    
    cout << mx << endl;
    return 0;
}