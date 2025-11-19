#include<bits/stdc++.h>
using namespace std;

#define int long long

int n;
vector<int> a;

void solve() {
    cin >> n;
    a.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    // Use set to store the unique results of the XOR calculations.
    set<int> results;
    int totalXOR = 0;

    // Calculate the overall XOR of all the elements.
    for (int value : a) {
        totalXOR ^= value;
    }

    // To find the number of unique XOR results, we can form the subsets
    // This can be done with the usage of a bit mask that reflects the use of
    // each element. The maximum possible number of subsets would be 2^N where N <= 12.
    
    results.insert(0); // Adding 0 for the case where no stones are chosen from any bag

    // Iterate through all possible subsets
    for (int mask = 1; mask < (1 << n); mask++) {
        int currentXOR = 0;
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) {
                currentXOR ^= a[i];
            }
        }
        results.insert(currentXOR);
    }

    cout << results.size() << '\n';
}

signed main() {
    ios::sync_with_stdio(false);
    int T = 1;
    while (T--) {
        solve();
    }
}