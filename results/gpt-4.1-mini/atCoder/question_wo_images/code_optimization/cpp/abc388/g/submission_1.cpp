#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200000 + 3;

int n, q;
int a[MAXN];
int b[MAXN]; // b[i] = minimal j > i with a[j] >= 2 * a[i], or n+1 if none
int st[MAXN][20]; // Sparse table for RMQ on b

int log2_table[MAXN];

// Precompute log2 for RMQ
void build_log2() {
    log2_table[1] = 0;
    for (int i = 2; i <= n; i++) {
        log2_table[i] = log2_table[i/2] + 1;
    }
}

// Build sparse table for RMQ (min)
void build_st() {
    for (int i = 1; i <= n; i++) {
        st[i][0] = b[i];
    }
    for (int j = 1; (1 << j) <= n; j++) {
        for (int i = 1; i + (1 << j) - 1 <= n; i++) {
            st[i][j] = min(st[i][j-1], st[i + (1 << (j-1))][j-1]);
        }
    }
}

// Query RMQ min on b[l..r]
int query_min(int l, int r) {
    if (l > r) return n+1;
    int len = r - l + 1;
    int k = log2_table[len];
    return min(st[l][k], st[r - (1 << k) + 1][k]);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    for (int i = 1; i <= n; i++) cin >> a[i];

    // Precompute b[i]: minimal j > i with a[j] >= 2 * a[i]
    for (int i = 1; i <= n; i++) {
        int val = 2 * (long long)a[i];
        // binary search for minimal j > i with a[j] >= val
        int low = i + 1, high = n, pos = n + 1;
        while (low <= high) {
            int mid = (low + high) >> 1;
            if (a[mid] >= val) {
                pos = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        b[i] = pos;
    }
    // For i = n, b[n] = n+1 (no j > n)
    b[n] = n + 1;

    build_log2();
    build_st();

    cin >> q;
    while (q--) {
        int L, R;
        cin >> L >> R;

        int len = R - L + 1;
        int maxK = len / 2;

        int low = 0, high = maxK, ans = 0;
        while (low <= high) {
            int mid = (low + high) >> 1;
            if (mid == 0) {
                ans = 0;
                low = mid + 1;
                continue;
            }
            int left = L;
            int right = L + mid - 1;
            if (right > R) {
                // Not enough elements to pick mid pairs
                high = mid - 1;
                continue;
            }
            int min_b = query_min(left, right);
            if (min_b <= R) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        cout << ans << "\n";
    }

    return 0;
}