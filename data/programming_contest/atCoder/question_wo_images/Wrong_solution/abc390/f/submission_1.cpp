#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; ++i) cin >> A[i];
    vector<int> v(N + 4, -1);
    long long ans = 0;
    for (int i = 0; i < N; ++i) {
        long long cur = 0;
        int T = 0;
        T = max(T, v[A[i] - 1] + 1);
        T = max(T, v[A[i]] + 1);
        T = max(T, v[A[i] + 1] + 1);
        cur += 1LL * (i - T + 1) * (N - i);
        if (v[A[i] - 1] != -1 && v[A[i] + 1] != -1) {
            if (v[A[i]] == -1) {
                int S = 0;
                S = min(v[A[i] + 1], v[A[i] - 1]);
                cur -= 1LL * (S + 1) * (N - i);
            } else {
                int S = v[A[i]] + 1;
                S = max(S, min(v[A[i] + 1], v[A[i] - 1]));
                cur -= 1LL * (S + 1) * (N - i);
            }
        }
        ans += cur;
        v[A[i]] = i;
    }
    cout << ans << endl;
}