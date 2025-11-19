#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while (T--) {
        int N; cin >> N;
        vector<int> A(N);
        for (int i = 0; i < N; i++) cin >> A[i];

        // We simulate the merging process using a stack.
        // Each element in the stack is a pair {value, count}.
        // When two consecutive elements have the same value, they merge into one with value+1.
        // We also keep track of the insertions needed to make merges possible.

        // The key insight:
        // - If top of stack has value v and count c,
        //   and next element is also v, we merge pairs of v's.
        // - If count is odd, one element remains unmerged.
        // - To merge all elements into one, we may need to insert elements to make counts even.
        // - Insertions needed = sum of insertions to make counts even + insertions needed to merge resulting elements.

        // We'll implement a stack-based approach that merges as much as possible greedily,
        // and counts insertions needed to fix parity.

        struct Node {
            int val;
            ll cnt;
        };

        vector<Node> stk;
        ll insertions = 0;

        for (int x : A) {
            // Push new element with count 1
            stk.push_back({x, 1});

            // Try to merge while top two have same value
            while (stk.size() >= 2) {
                auto &top = stk.back();
                auto &prev = stk[stk.size() - 2];
                if (top.val == prev.val) {
                    // Merge pairs from prev and top
                    ll pairs = (prev.cnt + top.cnt) / 2;
                    ll rem = (prev.cnt + top.cnt) % 2;

                    // Insertions needed to make total count even if odd
                    if (rem == 1) {
                        insertions++;
                        pairs++; // after insertion, pairs increase by 1
                        rem = 0;
                    }

                    // Remove top two
                    stk.pop_back();
                    stk.pop_back();

                    // Push merged node with val+1 and count = pairs
                    stk.push_back({top.val + 1, pairs});
                } else {
                    break;
                }
            }
        }

        // After processing all elements, we may have multiple nodes in stack.
        // We need to merge them into one node by inserting elements.

        // We'll repeatedly merge from right to left:
        // If stack size > 1, try to merge last two nodes by inserting elements to equalize values.

        while (stk.size() > 1) {
            auto top = stk.back(); stk.pop_back();
            auto &prev = stk.back();

            // To merge prev and top, their values must be equal.
            // If not equal, we must insert elements to increase smaller value to larger.

            if (prev.val < top.val) {
                // Insertions to increase prev.val to top.val
                ll diff = top.val - prev.val;
                insertions += diff * prev.cnt;
                prev.val = top.val;
            } else if (top.val < prev.val) {
                // Insertions to increase top.val to prev.val
                ll diff = prev.val - top.val;
                insertions += diff * top.cnt;
                top.val = prev.val;
            }

            // Now values equal, merge counts
            ll total = prev.cnt + top.cnt;

            // If total is odd, insert one element to make even
            if (total % 2 == 1) {
                insertions++;
                total++;
            }

            // Merge into one node with val+1 and count = total/2
            prev.val++;
            prev.cnt = total / 2;
        }

        cout << insertions << "\n";
    }

    return 0;
}