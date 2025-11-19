#include<bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        long long l1, b1, l2, b2, l3, b3;
        cin >> l1 >> b1 >> l2 >> b2 >> l3 >> b3;

        // Check if we can form a square
        bool canFormSquare = (l1 == b1 && (l2 + l3 == b1) && (l2 == b2 || b3 == 0) && (l3 == b3 || l3 == 0)) ||
                             (b1 == l1 && (l2 + l3 == b1) && (l2 == b2 || b3 == 0) && (l3 == b3 || l3 == 0)) ||
                             (l1 == b2 && (l2 + l3 == l1) && (l2 == b1 || b3 == 0) && (l3 == b3 || l3 == 0)) ||
                             (b1 == b2 && (l2 + l3 == l1) && (l2 == l1 || b3 == 0) && (l3 == b3 || l3 == 0)) ||
                             (l1 == l2 && (b1 + b3 == l1) && (b2 == b3)) ||
                             (b1 == b2 && (l1 + l3 == b1) && (l2 == b3)) ||
                             (l1 == b3 && (b1 + b2 == l1) && (l2 == l3)) ||
                             (b1 == b3 && (l1 + l2 == b1) && (l2 == l3));

        cout << (canFormSquare ? "YES" : "NO") << endl;
    }
    return 0;
}