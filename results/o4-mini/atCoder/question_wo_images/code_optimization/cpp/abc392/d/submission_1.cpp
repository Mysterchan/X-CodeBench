#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<int> K(N);
    vector<vector<int>> A(N);
    int maxA = 0;
    for (int i = 0; i < N; i++) {
        cin >> K[i];
        A[i].resize(K[i]);
        for (int j = 0; j < K[i]; j++) {
            cin >> A[i][j];
            if (A[i][j] > maxA) maxA = A[i][j];
        }
    }
    // For each value x, store list of (die index, frequency)
    vector<vector<pair<int,int>>> valList(maxA + 1);
    for (int i = 0; i < N; i++) {
        auto &vec = A[i];
        sort(vec.begin(), vec.end());
        int sz = vec.size();
        int ptr = 0;
        while (ptr < sz) {
            int x = vec[ptr];
            int cnt = 1;
            ptr++;
            while (ptr < sz && vec[ptr] == x) {
                cnt++;
                ptr++;
            }
            valList[x].emplace_back(i, cnt);
        }
    }
    // common[i][j] = sum of freq products for dice i<j
    vector<vector<long long>> common(N, vector<long long>(N, 0LL));
    for (int x = 0; x <= maxA; x++) {
        auto &lst = valList[x];
        int m = lst.size();
        if (m < 2) continue;
        for (int u = 0; u < m - 1; u++) {
            int i = lst[u].first;
            int fi = lst[u].second;
            for (int v = u + 1; v < m; v++) {
                int j = lst[v].first;
                int fj = lst[v].second;
                common[i][j] += 1LL * fi * fj;
            }
        }
    }
    double ans = 0.0;
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if (common[i][j] == 0) continue;
            double p = common[i][j] / (double)K[i] / (double)K[j];
            if (p > ans) ans = p;
        }
    }
    cout << fixed << setprecision(15) << ans << "\n";
    return 0;
}