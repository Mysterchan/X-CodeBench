#include <iostream>
#include <vector>

using namespace std;

const int N = 1e6 + 10;

int at[N];

int main() {
    int n, q;
    cin >> n >> q;

    // Initially, each pigeon is in its own nest.
    for (int i = 1; i <= n; i++) {
        at[i] = i;
    }

    while (q--) {
        int t, a, b;
        cin >> t;

        if (t == 1) {
            cin >> a >> b;
            // Move pigeon a to nest b
            at[a] = b;
        } else if (t == 2) {
            cin >> a >> b;
            // Swap nests a and b
            for (int i = 1; i <= n; i++) {
                if (at[i] == a) {
                    at[i] = b;
                } else if (at[i] == b) {
                    at[i] = a;
                }
            }
        } else if (t == 3) {
            cin >> a;
            // Output the current nest of pigeon a
            cout << at[a] << '\n';
        }
    }

    return 0;
}