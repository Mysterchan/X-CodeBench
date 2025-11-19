#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

int main() {
    int N, W;
    cin >> N >> W;

    vector<pair<int, int>> blocks(N); // Storing the position of blocks
    unordered_map<int, vector<int>> column_blocks; // Mapping to store filled rows for each column

    for (int i = 0; i < N; i++) {
        int X, Y;
        cin >> X >> Y;
        X--; // Convert to 0-indexed
        column_blocks[X].push_back(Y);
        blocks[i] = {X, Y};
    }

    // Sort each column's block positions
    for (auto& pair : column_blocks) {
        sort(pair.second.begin(), pair.second.end());
    }

    int Q;
    cin >> Q;
    for (int q = 0; q < Q; q++) {
        int T, A;
        cin >> T >> A;
        A--; // Convert to 0-indexed
        int X = blocks[A].first;
        int Y = blocks[A].second;

        // Check if the block is still intact
        if (Y - T >= 0) {
            cout << "Yes" << endl;
            continue;
        }

        // Check how many blocks are below block A in its column
        int blocks_below = lower_bound(column_blocks[X].begin(), column_blocks[X].end(), Y) - column_blocks[X].begin();

        // Check other columns for blocks that are not moving above
        bool exists = false;
        for (int i = 0; i < W; i++) {
            if (i == X) continue;
            int blocks_in_col = lower_bound(column_blocks[i].begin(), column_blocks[i].end(), T) - column_blocks[i].begin();
            if (blocks_below >= blocks_in_col) {
                exists = true;
                break;
            }
        }

        cout << (exists ? "Yes" : "No") << endl;
    }

    return 0;
}