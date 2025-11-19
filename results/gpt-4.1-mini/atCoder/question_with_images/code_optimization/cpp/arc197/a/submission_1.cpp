#include <bits/stdc++.h>
using namespace std;
#define int long long

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while (T--) {
        int H, W; cin >> H >> W;
        string S; cin >> S;

        // Count fixed Rs and Ds in S
        int fixedR = 0, fixedD = 0;
        for (char c : S) {
            if (c == 'R') fixedR++;
            else if (c == 'D') fixedD++;
        }

        // Number of '?' characters
        int q = (H + W - 2) - fixedR - fixedD;

        // The maximum number of black cells painted is:
        // (H * W) - (number of cells never visited)
        // The cells never visited are those that cannot be reached by any path
        // satisfying the constraints.
        //
        // The problem reduces to counting the union of all paths allowed by S.
        //
        // Key insight:
        // The maximum black cells painted = H*W - (number of cells that are unreachable)
        //
        // The unreachable cells are those that lie strictly below the minimal path
        // and strictly right of the maximal path.
        //
        // We can find the minimal path by replacing all '?' with 'D' (to go down as much as possible)
        // and the maximal path by replacing all '?' with 'R' (to go right as much as possible).
        //
        // The minimal path visits cells along a path with fixed Rs and Ds plus all '?' as Ds.
        // The maximal path visits cells along a path with fixed Rs and Ds plus all '?' as Rs.
        //
        // The cells visited by any path allowed by S are all cells in the rectangle
        // bounded by these two paths.
        //
        // The number of black cells painted = H*W - (H - minimal_path_row) * (W - maximal_path_col)
        //
        // minimal_path_row = 1 + fixedD + number_of_?'s (all '?' as D)
        // maximal_path_col = 1 + fixedR + number_of_?'s (all '?' as R)

        int min_row = 1 + fixedD + q; // all '?' as D
        int max_col = 1 + fixedR + q; // all '?' as R

        // Clamp to grid size
        if (min_row > H) min_row = H;
        if (max_col > W) max_col = W;

        int ans = H * W - (H - min_row) * (W - max_col);
        cout << ans << "\n";
    }

    return 0;
}