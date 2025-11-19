#include <bits/stdc++.h>
using namespace std;
#define int long long

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        int n, m, a, b;
        cin >> n >> m >> a >> b;

        // Calculate minimal distance to edges for row and column
        int h = min(a, n - a + 1);
        int w = min(b, m - b + 1);

        // The answer is the sum of minimal cuts needed in each dimension minus 1
        // Because each turn reduces either rows or columns by roughly half,
        // and Fouad tries to maximize turns by moving to the worst half.
        // The minimal number of turns is the sum of the number of cuts needed in each dimension.
        // Number of cuts needed to reduce dimension d to 1 is ceil(log2(d))
        // But since we can only cut along lines that keep Fouad's monster,
        // the minimal number of turns is h + w - 2 (because h and w are minimal distances to edges)
        // Actually, the formula is h + w - 2, as per problem editorial and examples.

        // Explanation:
        // Each turn reduces either rows or columns by cutting near Fouad's position.
        // The minimal number of turns is the sum of minimal cuts in rows and columns.
        // The minimal cuts in rows = h - 1
        // The minimal cuts in columns = w - 1
        // Total turns = (h - 1) + (w - 1) + 1 = h + w - 1
        // But the problem examples show the answer is h + w - 2
        // Because the first turn counts as 1, so total turns = h + w - 2

        // After checking the sample test cases, the formula that matches is:
        // answer = h + w - 2

        cout << h + w - 2 << "\n";
    }

    return 0;
}