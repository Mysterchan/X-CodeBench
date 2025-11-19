#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<ll> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    // Any sequence of length 2 is always a geometric progression
    if (N <= 2) {
        cout << "Yes";
        return 0;
    }

    // Let r = A[1] / A[0]; check A[i] / A[i-1] == r via cross multiplication:
    // A[i] * A[0] == A[1] * A[i-1] for all i >= 2
    for (int i = 2; i < N; i++) {
        if (A[i] * A[0] != A[1] * A[i - 1]) {
            cout << "No";
            return 0;
        }
    }

    cout << "Yes";
    return 0;
}