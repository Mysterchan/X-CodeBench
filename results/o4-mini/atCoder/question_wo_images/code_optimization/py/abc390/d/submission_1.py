#include <bits/stdc++.h>
using namespace std;
using ull = unsigned long long;

int N;
ull A[12];
ull sums[12];
unordered_set<ull> results;

void dfs(int idx, int groups, ull current_xor) {
    if (idx == N) {
        results.insert(current_xor);
        return;
    }
    ull ai = A[idx];
    // Try adding to existing groups
    for (int j = 0; j < groups; ++j) {
        ull old_sum = sums[j];
        ull new_sum = old_sum + ai;
        // update xor: remove old_sum, add new_sum
        sums[j] = new_sum;
        dfs(idx + 1, groups, current_xor ^ old_sum ^ new_sum);
        sums[j] = old_sum;
    }
    // Create a new group
    sums[groups] = ai;
    dfs(idx + 1, groups + 1, current_xor ^ ai);
    // sums[groups] will be overwritten or ignored on backtrack
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }
    results.reserve(500000);
    dfs(0, 0, 0ULL);
    cout << results.size() << "\n";
    return 0;
}