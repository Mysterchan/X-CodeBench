#include<bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<string> grid(N, string(N, '.')); // Initialize the grid with '.'

    for (int i = 1; i <= N; i++) {
        int j = N + 1 - i; // Calculate the end point
        
        if (i <= j) {
            char fillChar = (i % 2 == 1) ? '#' : '.'; // Determine fill character based on i's parity
            
            for (int row = i - 1; row < j; row++) { // Fill the grid
                for (int col = i - 1; col < j; col++) {
                    grid[row][col] = fillChar;
                }
            }
        }
    }

    // Output the grid
    for (const auto& line : grid) {
        cout << line << endl;
    }

    return 0;
}
