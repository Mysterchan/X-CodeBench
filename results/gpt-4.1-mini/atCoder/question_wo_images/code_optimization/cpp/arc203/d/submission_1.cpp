#include <bits/stdc++.h>
using namespace std;

const int N = 200005;

int n, q;
int a[N];

// We maintain:
// - q1: number of ones in a
// - q000: number of triples of zeros (a[i], a[i+1], a[i+2]) == (0,0,0)
// - s: set of positions i where a[i] + a[i+1] == 0 (adjacent zero pairs)
// We keep track of these values and update them efficiently after each flip.

// Function to check if a pair (i, i+1) is zero pair
inline bool is_zero_pair(int i) {
    if (i < 0 || i >= n) return false;
    return (a[i] + a[i + 1]) == 0;
}

// Function to check if a triple (i, i+1, i+2) is zero triple
inline bool is_zero_triple(int i) {
    if (i < 0 || i + 2 >= n) return false;
    return (a[i] + a[i + 1] + a[i + 2]) == 0;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];

    // Initialize q1, q000, and s
    int q1 = 0;
    for (int i = 0; i < n; i++) q1 += a[i];

    int q000 = 0;
    for (int i = 0; i + 2 < n; i++) {
        if (is_zero_triple(i)) q000++;
    }

    set<int> s;
    s.insert(-1);
    for (int i = 0; i < n; i++) {
        if (is_zero_pair(i)) s.insert(i);
    }
    s.insert(n); // sentinel

    cin >> q;
    while (q--) {
        int i; cin >> i; i--; // zero-based index

        // Before flip, update q1
        if (a[i] == 1) q1--;
        else q1++;

        // Flip a[i]
        a[i] ^= 1;

        // After flip, update q1
        // (already updated above)

        // Update q000 for triples that include position i
        // triples at i-2, i-1, i
        for (int start = i - 2; start <= i; start++) {
            if (start < 0 || start + 2 >= n) continue;
            bool before = (a[start] + a[start + 1] + a[start + 2]) == 0;
            // We need to know if before flip it was zero triple or not.
            // But we don't have old a, so we must store old triple states before flip.

            // To handle this, we store old triple states before flip.

            // So we do the following:
            // We'll store old triple states before flip, then after flip, update q000 accordingly.

            // To do this efficiently, we can store old triple states before flip.

            // So we need to do this outside the loop.

            // So let's do the following:
            // Before flip, store old triple states for i-2, i-1, i
            // After flip, check new triple states and update q000 accordingly.

            // We'll implement this outside the loop.
        }

        // So we need to store old triple states before flip:
        // Let's do it now:

        // We'll store old triple states for i-2, i-1, i before flip
        // So we need to do this before flipping a[i]

        // So we need to reorder code.

        // Let's do the following:

        // Move flip after storing old triple states.

        // So let's restart the update process:

        // Store old triple states
        static bool old_triple[3];
        for (int idx = 0; idx < 3; idx++) {
            int start = i - 2 + idx;
            if (start < 0 || start + 2 >= n) old_triple[idx] = false;
            else old_triple[idx] = is_zero_triple(start);
        }

        // Store old zero pairs for i-1 and i (pairs that might be affected)
        // pairs at i-1 and i
        static bool old_pair[2];
        for (int idx = 0; idx < 2; idx++) {
            int pos = i - 1 + idx;
            if (pos < 0 || pos >= n) old_pair[idx] = false;
            else old_pair[idx] = is_zero_pair(pos);
        }

        // Store old a[i]
        int old_ai = a[i];

        // Flip a[i]
        a[i] ^= 1;

        // Update q1
        if (old_ai == 1) q1--;
        else q1++;

        // Update q000
        for (int idx = 0; idx < 3; idx++) {
            int start = i - 2 + idx;
            if (start < 0 || start + 2 >= n) continue;
            bool new_triple = is_zero_triple(start);
            if (old_triple[idx] && !new_triple) q000--;
            else if (!old_triple[idx] && new_triple) q000++;
        }

        // Update s (zero pairs)
        // pairs at i-1 and i
        for (int idx = 0; idx < 2; idx++) {
            int pos = i - 1 + idx;
            if (pos < 0 || pos >= n) continue;
            bool new_pair = is_zero_pair(pos);
            if (old_pair[idx] && !new_pair) s.erase(pos);
            else if (!old_pair[idx] && new_pair) s.insert(pos);
        }

        // Now compute answer
        // ans = n - q000 + sum over intervals between zero pairs of F(*it, *jt, q1)
        // We can compute this efficiently by iterating over s

        // The function F(l, r, q1) is:
        // l and r are positions in s (positions where a[i]+a[i+1]==0)
        // F(l,r,q1):
        //   l += 2; r -= 1;
        //   if l > r return 0;
        //   if l == 1 && r == n:
        //       if q1 == n return 0;
        //       else return 2 - (r - l + 1);
        //   return 1 - (r - l + 1);

        // Note: original code uses 1-based indexing, we use 0-based.
        // So adjust accordingly.

        // We'll implement F accordingly.

        int ans = n - q000;

        auto it = s.begin();
        auto jt = it;
        ++jt;
        while (jt != s.end()) {
            int l = *it;
            int r = *jt;
            // Adjust l and r for F:
            int L = l + 2;
            int R = r - 1;
            if (L <= R) {
                if (L == 1 && R == n - 1) {
                    if (q1 == n) {
                        // add 0
                    } else {
                        ans += 2 - (R - L + 1);
                    }
                } else {
                    ans += 1 - (R - L + 1);
                }
            }
            ++it; ++jt;
        }

        cout << ans << "\n";
    }

    return 0;
}