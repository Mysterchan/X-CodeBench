#include <bits/stdc++.h>
using namespace std;
#define int long long

void solve() {
    int h, w;
    string s;
    cin >> h >> w >> s;

    int numD = count(s.begin(), s.end(), 'D');
    int numR = count(s.begin(), s.end(), 'R');
    int numQ = s.size() - numD - numR;

    // Maximum number of cells that can be painted from (1, 1) to (h, w)
    int maxCells = (h - numD - 1) + (w - numR - 1) + (h + w - 1);

    // The minimum cells will utilize all questions ('?')
    // We can use '?' to fill in the remaining Ds and Rs needed
    int remainingD = max(0LL, (h - 1) - numD);
    int remainingR = max(0LL, (w - 1) - numR);

    // Validating if we can utilize '?' for remaining paths
    if (remainingD + remainingR <= numQ) {
        // We will be able to completely paint the extra cells via '?'
        maxCells += numQ - remainingD - remainingR;
    }

    cout << maxCells << endl;
}

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        solve();
    }
}