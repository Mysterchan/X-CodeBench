#include <bits/stdc++.h>
using namespace std;
static int freq[1000005];
static int divcnt[1000005];
static int ans_val[1000005];
static int a[1200005];
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N >> K;
    int maxA = 0;
    for (int i = 0; i < N; ++i) {
        cin >> a[i];
        ++freq[a[i]];
        if (a[i] > maxA) maxA = a[i];
    }
    // Count how many numbers are divisible by d
    for (int d = 1; d <= maxA; ++d) {
        for (int j = d; j <= maxA; j += d) {
            divcnt[d] += freq[j];
        }
    }
    // For each d with divcnt[d] >= K, update all multiples
    for (int d = 1; d <= maxA; ++d) {
        if (divcnt[d] >= K) {
            for (int j = d; j <= maxA; j += d) {
                if (d > ans_val[j]) ans_val[j] = d;
            }
        }
    }
    // Output answers
    for (int i = 0; i < N; ++i) {
        cout << ans_val[a[i]] << '\n';
    }
    return 0;
}