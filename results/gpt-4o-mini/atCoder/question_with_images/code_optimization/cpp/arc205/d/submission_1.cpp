#include <bits/stdc++.h>
using namespace std;

const int MAXN = 500000;
vector<int> children[MAXN + 1];
int T;

void solve() {
    int n;
    cin >> n;

    // Clear children array for the new test case
    for (int i = 1; i <= n; i++) {
        children[i].clear();
    }

    for (int i = 2; i <= n; i++) {
        int p;
        cin >> p;
        children[p].push_back(i);
    }

    // Calculate the maximum number of operations from the leaves upwards
    int ans = 0;
    vector<int> count;

    function<void(int)> dfs = [&](int node) {
        if (children[node].empty()) {
            count.push_back(0); // This is a leaf
            return;
        }

        int totalLeaves = 0;
        for (int child : children[node]) {
            dfs(child);
            totalLeaves += count.back() + 1; // Count the leaves from children
            count.pop_back(); // Remove the count we added from the children
        }
        count.push_back(totalLeaves); // Store the current total for this node
    };

    dfs(1);
    sort(count.begin(), count.end(), greater<int>()); // Sort the counts in descending order

    // Calculate maximum pairs we can make
    for (int i = 0; i + 1 < count.size(); i += 2) {
        ans++;
    }

    cout << ans << endl;
}

int main() {
    cin >> T;
    while (T--) {
        solve();
    }
    return 0;
}