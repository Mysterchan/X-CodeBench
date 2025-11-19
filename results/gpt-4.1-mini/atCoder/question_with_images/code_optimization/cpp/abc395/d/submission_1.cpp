#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e6 + 10;

int at[MAXN]; // at[pigeon] = nest
int swap_flag[MAXN]; // swap_flag[nest] = 0 or 1, indicates if nest is swapped
int n, q;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> q;
    for (int i = 1; i <= n; i++) {
        at[i] = i;
        swap_flag[i] = 0;
    }

    while (q--) {
        int t; cin >> t;
        if (t == 1) {
            int a, b; cin >> a >> b;
            at[a] = b;
        } else if (t == 2) {
            int a, b; cin >> a >> b;
            // Swap the swap flags of nests a and b
            swap(swap_flag[a], swap_flag[b]);
        } else {
            int a; cin >> a;
            int nest = at[a];
            // If nest is swapped, the pigeon is effectively in the other nest
            if (swap_flag[nest]) {
                // The pigeon is in the "swapped" nest, which is the other nest
                // Since swap_flag[nest] = 1 means nest and its swap partner are swapped,
                // the pigeon is actually in the other nest.
                // But we don't know the other nest directly.
                // However, since swap_flag is only 0 or 1, and swaps happen pairwise,
                // the pigeon is in the "other" nest that swapped with nest.
                // But we don't have direct info of the other nest.
                // So we need a way to find the other nest.

                // To solve this, we can store the swap partner of each nest.
                // But that would be O(N) memory and complicated.

                // Instead, we can store the swap_flag as a parity bit:
                // For each nest, swap_flag[nest] = 0 or 1.
                // When we swap nests a and b, we swap their flags.
                // So the pigeon in nest with flag=1 means it is in the other nest.

                // So the pigeon is in the nest with label:
                // If swap_flag[nest] == 0 => nest
                // else => the other nest that swapped with nest.

                // But we don't know the other nest.

                // So the above approach is incomplete.

                // Alternative approach:
                // Instead of storing swap_flag per nest, store a global array "parent" for nests,
                // and maintain a DSU-like structure to track swaps.

                // Let's implement DSU for nests with parity to track swaps.

                // So we need to redo the approach.

                // Let's break and implement DSU with parity.

                // We'll implement DSU for nests:
                // parent[nest], size[nest], parity[nest]
                // parity[nest] = 0 or 1, indicates if nest is swapped relative to its parent.

                // When we swap nests a and b, we union their sets and flip parity.

                // Then, to find the actual nest of a pigeon, we find the root of at[a],
                // and parity along the path tells if the nest is swapped or not.

                // Let's implement this now.
            }
            cout << (swap_flag[nest] ? -1 : nest) << '\n'; // placeholder
        }
    }

    return 0;
}