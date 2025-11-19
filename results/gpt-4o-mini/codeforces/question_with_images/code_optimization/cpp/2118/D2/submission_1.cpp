#include<bits/stdc++.h>
using namespace std;
#define int long long

signed main() {
    ios::sync_with_stdio(0); // Faster I/O
    cin.tie(0);
    
    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        vector<int> p(n), d(n);
        for (int i = 0; i < n; i++) cin >> p[i];
        for (int i = 0; i < n; i++) cin >> d[i];

        int q;
        cin >> q;

        for (int i = 0; i < q; i++) {
            int x;
            cin >> x;

            int pos = lower_bound(p.begin(), p.end(), x) - p.begin();
            if (pos < n && p[pos] == x) pos++; // Ensure pos is on the right side of the traffic light if exactly equal

            // Check left and right traffic lights
            bool ok = false, direction = true; // direction = true -> right, false -> left
            set<pair<int, bool>> visited; // Use pair to track position and direction
            
            while (true) {
                if (pos < 0 || pos >= n) {
                    ok = true; 
                    break; 
                }
                int delay_time = t % k;
                if (delay_time == d[pos]) {
                    direction = !direction; // Change direction
                }

                // Record the state to detect loops
                auto state = make_pair(pos, direction);
                if (!visited.insert(state).second) break; // Found a loop
                
                // Move to the next position
                if (direction) {
                    x = p[pos] + 1; // Move right
                    pos++; // Increment position
                } else {
                    x = p[pos] - 1; // Move left
                    pos--; // Decrement position
                }
                t++;
            }

            cout << (ok ? "YES" : "NO") << '\n';
        }
    }
}