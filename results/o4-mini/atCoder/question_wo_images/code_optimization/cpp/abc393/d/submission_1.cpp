#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    string S;
    cin >> N >> S;

    vector<long long> B;
    B.reserve(N);
    for (int i = 0, cnt = 0; i < N; i++) {
        if (S[i] == '1') {
            B.push_back((long long)(i + 1) - cnt);
            cnt++;
        }
    }

    int K = B.size();
    int mid = K / 2;
    long long t = B[mid];
    long long ans = 0;
    for (int i = 0; i < K; i++) {
        ans += llabs(B[i] - t);
    }
    cout << ans << "\n";
    return 0;
}