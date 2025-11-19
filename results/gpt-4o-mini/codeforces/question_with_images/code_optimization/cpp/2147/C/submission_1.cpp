#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        int n;
        scanf("%d", &n);
        
        string s;
        cin >> s;

        bool valid = true;

        for (int i = 0; i < n; i++) {
            if (s[i] == '0') {
                // Check the left and right adjacent pots
                bool leftOccupied = (i > 0 && s[i - 1] == '1');
                bool rightOccupied = (i < n - 1 && s[i + 1] == '1');

                // If both sides are occupied, it's invalid
                if (leftOccupied && rightOccupied) {
                    valid = false;
                    break;
                }
            }
        }

        printf(valid ? "YES\n" : "NO\n");
    }
    return 0;
}