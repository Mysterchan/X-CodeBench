#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;

        string A, B;
        cin >> A >> B;

        vector<int> positionsA, positionsB;

        // Record the positions of '1's in A
        for (int i = 0; i < N; ++i) {
            if (A[i] == '1') {
                positionsA.push_back(i);
            }
        }

        // Record the positions of '1's in B
        for (int i = 0; i < N; ++i) {
            if (B[i] == '1') {
                positionsB.push_back(i);
            }
        }

        int mA = positionsA.size(), mB = positionsB.size();
        int ans = 0;

        // If B has '1's and A does not have sufficient '1's to cover all of B's requirements
        if (mA < mB) {
            cout << -1 << '\n';
            continue;
        }

        for (int i = 0; i < mB; ++i) {
            // Calculate distance from the closest '1' in A for each '1' in B
            int dist = abs(positionsA[i % mA] - positionsB[i]);
            ans += dist;
        }

        cout << ans << '\n';
    }

    return 0;
}
