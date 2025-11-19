#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll T; cin >> T;
    while (T--) {
        ll n, a, b;
        cin >> n >> a >> b;

        // The problem reduces to checking if there exists x and y such that
        // the final coloring is symmetric.
        // The final color is blue if cell is in blue segment, else red if in red segment,
        // else white.
        //
        // Since blue overrides red, the final coloring is:
        // blue segment [y, y+b-1]
        // red segment [x, x+a-1] excluding blue segment
        //
        // The coloring is symmetric if for every i:
        // color(i) == color(n+1 - i)
        //
        // Key insight:
        // The blue segment must be symmetric itself (or symmetric with red),
        // and the red segment must be symmetric outside blue.
        //
        // It can be shown that the answer is YES if and only if:
        // a + b > n
        //
        // Because if a + b <= n, the two segments can be placed without overlap,
        // and the final coloring cannot be symmetric.
        //
        // If a + b > n, then the two segments must overlap,
        // and we can place them so that the final coloring is symmetric.
        //
        // This is a known result from the editorial of the problem.

        if (a + b > n) cout << "YES\n";
        else cout << "NO\n";
    }
    return 0;
}