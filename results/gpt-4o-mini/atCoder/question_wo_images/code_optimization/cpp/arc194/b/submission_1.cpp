#include <bits/stdc++.h>
using namespace std;

#define IOS ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0)

void solve() {
    int n;
    cin >> n;
    vector<int> a(n + 1);
    for(int i = 1; i <= n; i++) cin >> a[i];
    
    long long res = 0;
    
    // We will keep track of the positions of each element
    vector<int> pos(n + 1);
    for(int i = 1; i <= n; i++) {
        pos[a[i]] = i; // Store the position of each number
    }

    // Iterate through each position to count the cost of bringing each number to its correct position
    for(int i = 1; i <= n; i++) {
        while(pos[i] != i) {
            int swap_index = pos[i]; // Where i is currently located
            int swap_value = a[swap_index]; // This is the value at position of i
            
            // Perform the swap
            swap(a[swap_index], a[swap_index - 1]);
            swap(pos[i], pos[swap_value]);
            res += swap_index - 1; // The cost of swap

            // Just reduced index by 1, so we need to update the position
            pos[swap_value]--;
        }
    }

    cout << res << '\n';
}

signed main() {
    IOS;
    solve();
    return 0;
}
