#include <iostream>
using namespace std;

int main() {
    int A[5];
    for (int i = 0; i < 5; ++i) {
        cin >> A[i];
    }

    int swapCount = 0;

    for (int i = 0; i < 4; ++i) {
        if (A[i] > A[i + 1]) {
            swapCount++;
            if (swapCount > 1) {
                cout << "No" << endl;
                return 0;
            }
        }
    }

    if (swapCount == 1) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

    return 0;
}