#include <bits/stdc++.h>
using namespace std;

int n;
char s[110][110];
char t[110][110];

// Function to count number of cells that are the same in S and T
int countMatches(char source[][110], char target[][110]) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (source[i][j] == target[i][j]) {
                count++;
            }
        }
    }
    return count;
}

// Function to rotate the grid 90 degrees clockwise
void rotate(char source[][110], char target[][110]) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            target[j][n - 1 - i] = source[i][j];
        }
    }
}

int main() {
    cin >> n;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> s[i][j];
        }
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> t[i][j];
        }
    }

    // This will store the minimum number of operations found
    int min_operations = n * n;

    for (int rotations = 0; rotations < 4; rotations++) { // Check all 4 rotations
        int matches = countMatches(s, t);
        int changes_needed = n * n - matches; // Cells that need to change
        min_operations = min(min_operations, changes_needed);

        // Rotate the grid for next comparison
        char rotated[110][110];
        rotate(s, rotated);
        memcpy(s, rotated, sizeof(rotated)); // Update S with the rotated version
    }

    cout << min_operations << endl;
    return 0;
}