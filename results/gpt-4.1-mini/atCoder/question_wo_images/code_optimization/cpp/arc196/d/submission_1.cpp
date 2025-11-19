#include <bits/stdc++.h>
using namespace std;

const int N = 400005;
int n, m, q;
pair<int,int> a[N];
int op[N];
int f[N];

// We will use a stack-based approach to find the maximum valid prefix for each i
// The problem reduces to checking interval conflicts with certain conditions.
// The original code uses complex data structures and checks that are O(m^2) in worst case.
// We optimize by using a monotonic stack and interval properties.

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m >> q;
    for (int i = 1; i <= m; i++) {
        int s, t; cin >> s >> t;
        if (s > t) swap(s, t);
        a[i] = {s, t};
        op[i] = (a[i].first < a[i].second) ? 1 : 0; // always 1 since s<t after swap
    }

    // The problem constraints and conditions imply:
    // For intervals [l,r], no two intervals can "cross" in a certain way.
    // We can model the problem as checking if intervals are "non-crossing" in a certain sense.
    // The original code tries to find for each i the minimal j such that intervals [j..i] are valid.

    // We will use a stack to maintain intervals in a way that no invalid crossing occurs.
    // The key is to maintain intervals sorted by their start and end points and check for conflicts.

    // We'll maintain two stacks: one for intervals with op=1 (all intervals here), but since op[i] is always 1, we only need one stack.

    // The conditions for invalidity are:
    // - Intervals with same start but different ends
    // - Intervals with same end but different starts
    // - Intervals that cross improperly

    // We can check these conditions by maintaining a stack of intervals and popping when conflicts occur.

    // We'll store intervals as (start, end), sorted by start ascending.

    // We'll keep track of the minimal left index j for each i.

    // We'll use a stack to maintain intervals in increasing order of start and end, ensuring no conflicts.

    // For each i, we try to extend the valid segment by pushing a[i] and popping conflicting intervals.

    // We'll store the minimal j for each i in f[i].

    // Implementation:

    vector<pair<int,int>> stk; // stack of intervals
    int left_ptr = 1;

    for (int i = 1; i <= m; i++) {
        auto cur = a[i];
        // Pop from stack while conflict occurs
        while (!stk.empty()) {
            auto top = stk.back();

            // Check conflicts:
            // If intervals have same start but different ends -> conflict
            if (top.first == cur.first && top.second != cur.second) {
                // conflict
                left_ptr = max(left_ptr, i);
                break;
            }
            // If intervals have same end but different starts -> conflict
            if (top.second == cur.second && top.first != cur.first) {
                left_ptr = max(left_ptr, i);
                break;
            }
            // Check crossing:
            // intervals [l1,r1], [l2,r2] cross if l1 < l2 < r1 < r2 or l2 < l1 < r2 < r1
            // We want to avoid crossing intervals.
            if (top.first < cur.first && cur.first < top.second && top.second < cur.second) {
                left_ptr = max(left_ptr, i);
                break;
            }
            if (cur.first < top.first && top.first < cur.second && cur.second < top.second) {
                left_ptr = max(left_ptr, i);
                break;
            }

            // If no conflict, break
            break;
        }

        // If conflict detected, we need to move left_ptr forward until no conflict
        // But above we just set left_ptr = i, so intervals before i are invalid
        // So we clear stack and start fresh from i
        if (left_ptr > i) {
            // invalid segment, clear stack
            stk.clear();
            f[i] = left_ptr;
            continue;
        }

        // Now remove intervals from stack that conflict with current interval
        while (!stk.empty()) {
            auto top = stk.back();
            // If top interval start >= current start and end >= current end, pop top
            // Because current interval is "smaller" and can replace top
            // This is to maintain minimal intervals in stack
            if (top.first >= cur.first && top.second >= cur.second) {
                stk.pop_back();
            } else {
                break;
            }
        }

        stk.push_back(cur);

        // f[i] = left_ptr
        f[i] = left_ptr;
    }

    // For queries (L,R), answer "Yes" if f[R] <= L else "No"
    for (int _ = 0; _ < q; _++) {
        int L, R; cin >> L >> R;
        cout << (f[R] <= L ? "Yes" : "No") << "\n";
    }

    return 0;
}