#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    string S;
    cin >> N >> S;

    vector<long long> pos;
    pos.reserve(N);
    for (int i = 0; i < N; i++) {
        if (S[i] == '1') pos.push_back(i);
    }
    int k = pos.size();
    if (k <= 1) {
        cout << 0 << "\n";
        return 0;
    }

    vector<long long> q(k);
    for (int i = 0; i < k; i++) {
        q[i] = pos[i] - i;
    }
    long long median = q[k/2];
    long long ans = 0;
    for (int i = 0; i < k; i++) {
        ans += llabs(q[i] - median);
    }
    cout << ans << "\n";
    return 0;
}