#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, R, C;
    string S;
    cin >> N >> R >> C >> S;

    // We track the position of the smoke relative to (0,0) at each time.
    // At time 0, smoke is at (0,0).
    // At time t, smoke moves according to S[t-1].
    // If smoke is not at (0,0) after moving, new smoke is generated at (0,0).
    // So smoke positions at time t are:
    // - the previous smoke positions moved by S[t-1]
    // - plus (0,0) if no smoke was there after moving.

    // Instead of tracking all smoke positions (which can be large),
    // we track the set of offsets of smoke positions relative to (0,0).
    // But this is still expensive.

    // Key insight:
    // The smoke positions at time t are:
    // - The set of positions reachable by applying the wind moves from (0,0),
    //   plus possibly (0,0) if no smoke was there after moving.

    // But the problem only asks if smoke exists at (R,C) at time t+0.5.
    // Let's consider the reverse movement:
    // At time t+0.5, smoke is at (R,C) if and only if
    // at time t, smoke was at (R', C') such that after moving by S[t], it reaches (R,C).
    // That is, (R', C') = (R, C) moved opposite to S[t].

    // Also, if no smoke at (0,0) at time t, new smoke is generated at (0,0).
    // So smoke at time t is union of:
    // - all smoke positions at time t-1 moved by S[t]
    // - plus (0,0) if (0,0) not in the moved set.

    // We want to know if (R,C) is in smoke positions at time t.

    // Let's track the position of (R,C) backward in time:
    // Define (rr, cc) = (R,C)
    // For t = N down to 1:
    //   At time t, smoke is at (rr, cc) if:
    //     - (rr, cc) == (0,0), or
    //     - (rr, cc) was reachable from time t-1 by moving according to S[t-1].
    //
    // So we can simulate backward:
    // At time t, if smoke is at (rr, cc), then at time t-1, smoke was at (rr', cc') where
    // (rr', cc') = (rr, cc) moved opposite to S[t-1].

    // Also, if at time t-1, smoke was not at (0,0), new smoke is generated at (0,0).
    // So smoke always exists at (0,0) at time t if it was not there after moving.

    // We can track the position of (R,C) backward through time,
    // and check if at time t, smoke exists at (R,C).

    // Implementation:
    // We start from (R,C) at time t.
    // For t = 1 to N:
    //   We move (R,C) backward by the opposite of S[t-1].
    //   If (R,C) == (0,0) at time t, then smoke exists at (R,C) at time t+0.5.
    //   Else, if (0,0) is not in the smoke positions at time t, smoke is generated at (0,0),
    //   so smoke exists at (0,0) at time t, but we only care about (R,C).

    // But we need to know if smoke exists at (R,C) at time t+0.5.
    // The smoke positions at time t are:
    //   - the positions at time t-1 moved by S[t-1]
    //   - plus (0,0) if (0,0) not in the moved set.

    // So if (R,C) == (0,0), smoke always exists at (0,0).
    // For other positions, we track backward.

    // Let's implement the backward simulation.

    int rr = R, cc = C;
    string ans(N, '0');

    // Direction mapping for opposite moves
    // N: (r-1,c) => opposite is (r+1,c)
    // W: (r,c-1) => opposite is (r,c+1)
    // S: (r+1,c) => opposite is (r-1,c)
    // E: (r,c+1) => opposite is (r,c-1)
    for (int i = N - 1; i >= 0; i--) {
        // Check if smoke exists at (rr, cc) at time i+1 (t+0.5)
        // Smoke exists if (rr, cc) == (0,0) or if smoke existed at time i at position (rr', cc')
        // where (rr, cc) = (rr', cc') moved by S[i]

        // At time i+1, smoke exists at (rr, cc) if:
        // - (rr, cc) == (0,0), or
        // - smoke existed at time i at position (rr', cc') = (rr, cc) moved opposite to S[i]

        // So if (rr, cc) == (0,0), smoke exists at time i+1 at (rr, cc)
        if (rr == 0 && cc == 0) {
            ans[i] = '1';
        } else {
            // Otherwise, smoke exists at (rr, cc) at time i+1 if smoke existed at time i at (rr', cc')
            // We don't know if smoke existed at (rr', cc') at time i, but we can track backward.

            // So we set ans[i] = '0' for now, and continue backward.

            // Actually, we can only say smoke exists at (rr, cc) at time i+1 if smoke existed at time i at (rr', cc')
            // or if (0,0) was added at time i (if no smoke at (0,0) after moving).

            // But since we track backward, we just update (rr, cc) to (rr', cc') for next iteration.
        }

        // Move (rr, cc) backward by opposite of S[i]
        char ch = S[i];
        if (ch == 'N') rr += 1;
        else if (ch == 'W') cc += 1;
        else if (ch == 'S') rr -= 1;
        else /* ch == 'E' */ cc -= 1;
    }

    // After processing all, print ans
    cout << ans << "\n";

    return 0;
}