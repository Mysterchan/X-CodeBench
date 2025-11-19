#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000001;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n, q;
    cin >> n >> q;

    vector<int> last(n + 1, 0);
    vector<bool> drawn(n + 1, false);
    
    while (q--) {
        int a, b;
        cin >> a >> b;

        if (a > b) swap(a, b);

        bool intersects = false;
        for (int i = a + 1; i < b; ++i) {
            if (drawn[i]) {
                intersects = true;
                break;
            }
        }

        if (!intersects) {
            cout << "Yes\n";
            drawn[a] = drawn[b] = true; // Mark endpoints as drawn
            for (int i = a + 1; i < b; ++i) {
                drawn[i] = true; // Mark the space in between as drawn
            }
        } else {
            cout << "No\n";
        }
    }

    return 0;
}