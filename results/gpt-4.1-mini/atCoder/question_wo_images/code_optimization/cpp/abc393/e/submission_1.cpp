#include <bits/stdc++.h>
using namespace std;

const int MAX_A = 1'000'000;
const int MAX_N = 1'200'000;

int n, k;
int a[MAX_N + 1];
int freq[MAX_A + 1];
int cnt[MAX_A + 1];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> k;
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        ++freq[a[i]];
    }

    // cnt[d] = number of elements divisible by d
    for (int d = 1; d <= MAX_A; ++d) {
        int sum = 0;
        for (int multiple = d; multiple <= MAX_A; multiple += d) {
            sum += freq[multiple];
        }
        cnt[d] = sum;
    }

    // For each element, find max divisor d of a[i] with cnt[d] >= k
    // To optimize divisor enumeration, precompute divisors for all numbers up to MAX_A
    // But memory/time is tight, so we do divisor enumeration on the fly with sqrt

    for (int i = 1; i <= n; ++i) {
        int x = a[i];
        int res = 1;
        int limit = (int)std::sqrt(x);
        for (int d = 1; d <= limit; ++d) {
            if (x % d == 0) {
                int d1 = d;
                int d2 = x / d;
                if (cnt[d1] >= k && d1 > res) res = d1;
                if (d1 != d2 && cnt[d2] >= k && d2 > res) res = d2;
            }
        }
        cout << res << '\n';
    }

    return 0;
}