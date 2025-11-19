#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<long long> heights(n);
        for (int i = 0; i < n; i++) {
            cin >> heights[i];
        }

        vector<long long> final(n, 0);
        long long blocks = 0;
        int mex = 0;

        for (int i = 0; i < n; ++i) {
            blocks += heights[i];

            // Calculate how many blocks can be added to the current position
            final[i] = min(blocks, (long long)i + 1);
            blocks -= final[i];
        }

        // Calculate the maximum MEX from the final array
        for (int i = 0; i < n; ++i) {
            if (final[i] == mex) {
                mex++;
            }
        }

        cout << mex << endl;
    }
    return 0;
}