#include<bits/stdc++.h>
using namespace std;
#define int long long

signed main() {
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];

    sort(A.begin(), A.end());

    int ans = 0;
    for (int i = 0; i < N / 2; i++) {
        ans += A[N - 1 - i] - A[i];
    }

    cout << ans;
}
