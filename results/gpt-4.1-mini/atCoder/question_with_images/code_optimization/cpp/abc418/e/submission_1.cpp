#include <bits/stdc++.h>
using namespace std;
#define int long long
typedef pair<int,int> PII;

const int N = 2005;

int n;
int x[N], y[N];
unordered_map<long long, int> slope_count;
unordered_map<long long, int> mid_count;

inline long long gcd_ll(long long a, long long b) {
    while (b) {
        long long t = a % b;
        a = b;
        b = t;
    }
    return a;
}

// Encode slope as a pair of reduced integers packed into a single 64-bit integer
inline long long encode_slope(int dx, int dy) {
    if (dx == 0) return (1LL << 32); // vertical line special code
    if (dy == 0) return 0;            // horizontal line special code
    int g = gcd_ll(abs(dx), abs(dy));
    dx /= g; dy /= g;
    // Ensure dx > 0 for unique representation
    if (dx < 0) {
        dx = -dx;
        dy = -dy;
    }
    return ((long long)dx << 32) | ((unsigned int)dy & 0xFFFFFFFF);
}

// Encode midpoint as a pair of sums (x1+x2, y1+y2) packed into 64-bit integer
inline long long encode_mid(int x1, int y1, int x2, int y2) {
    // sums fit in 32-bit since max coordinate is 1e7, sum max 2e7 < 2^31
    return ((long long)(x1 + x2) << 32) | (unsigned int)(y1 + y2);
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    for (int i = 1; i <= n; i++) cin >> x[i] >> y[i];

    slope_count.reserve(n * n / 2);
    mid_count.reserve(n * n / 2);

    int p = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = i + 1; j <= n; j++) {
            long long mid = encode_mid(x[i], y[i], x[j], y[j]);
            p += mid_count[mid]++;
            int dx = x[j] - x[i];
            int dy = y[j] - y[i];
            long long slope = encode_slope(dx, dy);
            slope_count[slope]++;
        }
    }

    int ans = 0;
    for (auto &kv : slope_count) {
        int c = kv.second;
        ans += c * (c - 1) / 2;
    }

    cout << ans - p << "\n";

    return 0;
}