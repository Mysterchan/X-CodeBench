#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    int ones = 0, moves = 0;

    for (int i = 0; i < n; i++) {
        cin >> a[i];
        if (a[i] == 1) {
            ones++;
        } else {
            moves += (a[i] - 1);
        }
    }

    // If there's at least one '1' in the array
    if (ones > 0) {
        // If total count of elements is odd, Fennec wins, else Snuke wins
        cout << (n % 2 == 1 ? "Fennec" : "Snuke") << endl;
    } else {
        // Total moves + number of elements determines the winner
        cout << ((moves + n) % 2 == 0 ? "Snuke" : "Fennec") << endl;
    }

    return 0;
}
