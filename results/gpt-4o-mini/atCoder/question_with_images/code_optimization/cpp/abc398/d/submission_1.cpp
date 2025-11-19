#include<bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false), cin.tie(0);
    int n, r, c;
    string s, result;
    cin >> n >> r >> c >> s;

    int smoke_x = 0, smoke_y = 0; // Position of smoke at (0,0)
    vector<pair<int, int>> smoke_positions = {{0, 0}}; // Initialize smoke at the campfire

    for (int i = 0; i < n; ++i) {
        // Update smoke positions based on wind direction
        char direction = s[i];
        for (auto &pos : smoke_positions) {
            if (direction == 'N') {
                pos.first -= 1; // Move up
            } else if (direction == 'W') {
                pos.second -= 1; // Move left
            } else if (direction == 'S') {
                pos.first += 1; // Move down
            } else if (direction == 'E') {
                pos.second += 1; // Move right
            }
        }

        // Check if there's smoke at (0, 0) after moving
        if (find(smoke_positions.begin(), smoke_positions.end(), make_pair(0, 0)) == smoke_positions.end()) {
            smoke_positions.emplace_back(0, 0); // Generate new smoke at (0,0)
        }

        // Check if the given (r, c) has smoke in this iteration
        result += (find(smoke_positions.begin(), smoke_positions.end(), make_pair(r, c)) != smoke_positions.end()) ? '1' : '0';
    }

    cout << result;
    return 0;
}