#include <bits/stdc++.h>
using namespace std;
using ull = unsigned long long;

int N;
ull A[12];
ull blockSum[12];
vector<ull> results;

// Precomputed Bell numbers for n = 0..12
const int BELL[13] = {
    1,       // Bell(0)
    1,       // Bell(1)
    2,       // Bell(2)
    5,       // Bell(3)
    15,      // Bell(4)
    52,      // Bell(5)
    203,     // Bell(6)
    877,     // Bell(7)
    4140,    // Bell(8)
    21147,   // Bell(9)
    115975,  // Bell(10)
    678570,  // Bell(11)
    4213597  // Bell(12)
};

void dfs_partition(int idx, int blocks) {
    if (idx == N) {
        ull x = 0;
        for (int b = 0; b < blocks; b++) {
            x ^= blockSum[b];
        }
        results.push_back(x);
        return;
    }
    // Try adding A[idx] to each existing block
    for (int b = 0; b < blocks; b++) {
        blockSum[b] += A[idx];
        dfs_partition(idx + 1, blocks);
        blockSum[b] -= A[idx];
    }
    // Or start a new block with A[idx]
    blockSum[blocks] = A[idx];
    dfs_partition(idx + 1, blocks + 1);
    // Not strictly needed to clear blockSum[blocks] back to 0,
    // but we'll do it for clarity.
    blockSum[blocks] = 0;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    // Reserve according to Bell(N) to avoid reallocations
    results.reserve(BELL[N]);

    // Initialize block sums to zero
    memset(blockSum, 0, sizeof(blockSum));

    // Enumerate all set partitions of {0..N-1}
    dfs_partition(0, 0);

    // Sort and count distinct XOR values
    sort(results.begin(), results.end());
    ull countDistinct = 0;
    ull prev = 0;
    for (size_t i = 0; i < results.size(); i++) {
        if (i == 0 || results[i] != prev) {
            countDistinct++;
            prev = results[i];
        }
    }

    cout << countDistinct << "\n";
    return 0;
}