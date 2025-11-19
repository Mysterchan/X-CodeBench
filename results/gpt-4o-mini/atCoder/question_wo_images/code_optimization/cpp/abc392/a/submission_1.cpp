#include <iostream>
using namespace std;

int main() {
    int A[3];
    for (int i = 0; i < 3; i++) {
        cin >> A[i];
    }
    
    // Check all combinations of multiplying two numbers and compare with the third
    if ((A[0] * A[1] == A[2]) || (A[0] * A[2] == A[1]) || (A[1] * A[2] == A[0])) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

    return 0;
}