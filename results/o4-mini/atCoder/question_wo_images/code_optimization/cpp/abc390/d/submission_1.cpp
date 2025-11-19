#include <bits/stdc++.h>
using namespace std;
using ull = unsigned long long;

int n;
ull A[12];
ull csum[12];
vector<ull> results;

void dfs(int idx, int groups, ull currXor) {
    if (idx == n) {
        results.push_back(currXor);
        return;
    }
    ull v = A[idx];
    // Try adding A[idx] to each existing group
    for (int j = 0; j < groups; ++j) {
        ull old = csum[j];
        ull nw = old + v;
        csum[j] = nw;
        dfs(idx + 1, groups, currXor ^ old ^ nw);
        csum[j] = old;
    }
    // Try making a new group with A[idx]
    csum[groups] = v;
    dfs(idx + 1, groups + 1, currXor ^ v);
    // csum[groups] will be overwritten in further calls
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> A[i];
    }
    results.reserve(4500000);
    // initialize csum to zero
    for (int i = 0; i < n; ++i) csum[i] = 0ull;
    dfs(0, 0, 0ull);
    sort(results.begin(), results.end());
    ull uniqueCount = 0;
    ull prev = 0;
    for (size_t i = 0; i < results.size(); ++i) {
        if (i == 0 || results[i] != prev) {
            ++uniqueCount;
            prev = results[i];
        }
    }
    cout << uniqueCount << "\n";
    return 0;
}