#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int MOD = 998244353;
const int MAXN = 200000;

int t, n;
int p[MAXN + 1], c[MAXN + 1];
int pos[MAXN + 1];
int bit[MAXN + 1];

// Fenwick tree (BIT) for counting how many positions have been processed
void bit_update(int i) {
    while (i <= n) {
        bit[i]++;
        i += i & (-i);
    }
}

int bit_query(int i) {
    int res = 0;
    while (i > 0) {
        res += bit[i];
        i -= i & (-i);
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> t;
    while (t--) {
        cin >> n;
        for (int i = 1; i <= n; i++) {
            cin >> p[i];
            pos[p[i]] = i;
            bit[i] = 0;
        }
        for (int i = 1; i <= n; i++) {
            cin >> c[i];
        }

        ll ans = 1;
        // We'll process elements in increasing order of p_i (i.e. from 1 to n)
        // For each i, find how many elements with the same color c[pos[i]] are
        // already placed to the left and right in the current treap split analogy.
        // The answer is product over i of (left_count + right_count + 1).

        // To do this efficiently, we keep track of positions processed using BIT,
        // and maintain counts of colors in left and right parts using hash maps.

        // But since we only need counts of color c[pos[i]] in left and right,
        // we can maintain two Fenwicks or maps for colors.

        // Instead of complicated treap, we simulate the logic:
        // For each i in 1..n:
        //   ps = pos[i] - bit_query(pos[i])  // position in the current treap
        //   left part size = ps - 1
        //   right part size = total processed - left part size
        // We need counts of color c[pos[i]] in left and right parts.

        // We'll maintain two Fenwicks for colors:
        // But colors can be up to n, so Fenwicks per color is too large.
        // Instead, we maintain a map<int,int> color_count for processed elements,
        // and for each i, we can count how many processed elements with color c[pos[i]]
        // are to the left and right by using a balanced tree or prefix sums.

        // Since positions are unique and we process in order of i,
        // we can store processed positions in a balanced structure (like a BIT)
        // and for each color, maintain a BIT over positions.

        // To optimize, we can store for each color a vector of positions processed,
        // and binary search to count how many are less than pos[i] (left count),
        // and how many are greater (right count).

        // We'll implement this approach.

        static vector<int> color_positions[MAXN + 1];
        for (int i = 1; i <= n; i++) {
            color_positions[i].clear();
        }

        // processed_positions: set of positions processed so far
        // We'll process i from 1 to n:
        // For each i:
        //   left_count = number of processed positions with color c[pos[i]] less than pos[i]
        //   right_count = number of processed positions with color c[pos[i]] greater than pos[i]
        //   ans *= (left_count + right_count + 1)
        //   insert pos[i] into color_positions[c[pos[i]]]

        for (int i = 1; i <= n; i++) {
            int color = c[pos[i]];
            auto &vec = color_positions[color];
            // binary search to find how many positions < pos[i]
            int left_count = (int)(std::lower_bound(vec.begin(), vec.end(), pos[i]) - vec.begin());
            int right_count = (int)(vec.size()) - left_count;
            ans = (ans * (left_count + right_count + 1)) % MOD;
            // insert pos[i] in sorted order
            vec.insert(std::upper_bound(vec.begin(), vec.end(), pos[i]), pos[i]);
        }

        cout << ans << "\n";
    }

    return 0;
}