#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    cin >> N >> M;
    vector<int> A(N), B(M);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    for (int i = 0; i < M; i++) {
        cin >> B[i];
    }
    vector<int> L(M), R(M);
    // compute leftmost match positions
    int pos = 0;
    for (int i = 0; i < M; i++) {
        while (pos < N && A[pos] != B[i]) {
            pos++;
        }
        if (pos == N) {
            cout << "No\n";
            return 0;
        }
        L[i] = pos;
        pos++;
    }
    // compute rightmost match positions
    pos = N - 1;
    for (int i = M - 1; i >= 0; i--) {
        while (pos >= 0 && A[pos] != B[i]) {
            pos--;
        }
        if (pos < 0) {
            cout << "No\n";
            return 0;
        }
        R[i] = pos;
        pos--;
    }
    // if there's any difference between L and R, we have two distinct subsequences
    for (int i = 0; i < M; i++) {
        if (L[i] != R[i]) {
            cout << "Yes\n";
            return 0;
        }
    }
    cout << "No\n";
    return 0;
}