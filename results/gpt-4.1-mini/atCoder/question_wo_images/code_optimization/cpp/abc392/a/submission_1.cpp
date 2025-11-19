#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int A[3];
    for (int i = 0; i < 3; i++) cin >> A[i];

    // Check all permutations of A
    sort(A, A + 3);
    do {
        if (A[0] * A[1] == A[2]) {
            cout << "Yes\n";
            return 0;
        }
    } while (next_permutation(A, A + 3));

    cout << "No\n";
    return 0;
}