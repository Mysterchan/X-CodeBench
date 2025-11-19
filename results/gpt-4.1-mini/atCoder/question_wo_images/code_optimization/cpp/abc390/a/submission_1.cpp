#include <bits/stdc++.h>
using namespace std;

int main() {
    int a[5];
    for (int i = 0; i < 5; ++i) cin >> a[i];

    // Check if already sorted - must perform exactly one swap, so print No
    bool sorted = true;
    for (int i = 0; i < 4; ++i) {
        if (a[i] > a[i + 1]) {
            sorted = false;
            break;
        }
    }
    if (sorted) {
        cout << "No\n";
        return 0;
    }

    // Try swapping each adjacent pair once and check if sorted
    for (int i = 0; i < 4; ++i) {
        swap(a[i], a[i + 1]);
        bool now_sorted = true;
        for (int j = 0; j < 4; ++j) {
            if (a[j] > a[j + 1]) {
                now_sorted = false;
                break;
            }
        }
        swap(a[i], a[i + 1]); // revert

        if (now_sorted) {
            cout << "Yes\n";
            return 0;
        }
    }

    cout << "No\n";
    return 0;
}