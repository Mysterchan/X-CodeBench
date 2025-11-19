#include <bits/stdc++.h>
using namespace std;
using cd = complex<double>;
const double PI = acos(-1);

void fft(vector<cd> & a, bool invert) {
    int n = a.size();
    static vector<int> rev;
    static vector<cd> roots{ {0,0}, {1,0} };
    if ((int)rev.size() != n) {
        rev.assign(n, 0);
        for (int i = 0; i < n; i++) {
            rev[i] = (rev[i >> 1] >> 1) | ((i & 1) ? (n >> 1) : 0);
        }
    }
    if ((int)roots.size() < n) {
        int k = roots.size();
        roots.resize(n);
        while (k < n) {
            double angle = 2 * PI / (2 * k);
            for (int i = 0; i < k; i++) {
                roots[k + i] = polar(1.0, angle * i);
            }
            k <<= 1;
        }
    }
    for (int i = 0; i < n; i++) {
        if (i < rev[i]) swap(a[i], a[rev[i]]);
    }
    for (int len = 1; len < n; len <<= 1) {
        for (int i = 0; i < n; i += 2 * len) {
            for (int j = 0; j < len; j++) {
                cd u = a[i + j];
                cd v = a[i + j + len] * roots[len + j];
                a[i + j] = u + v;
                a[i + j + len] = u - v;
            }
        }
    }
    if (invert) {
        reverse(a.begin() + 1, a.end());
        for (int i = 0; i < n; i++) {
            a[i] /= n;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<int> S(N);
    int maxv = 0;
    for (int i = 0; i < N; i++) {
        cin >> S[i];
        if (S[i] > maxv) maxv = S[i];
    }

    int need = 2 * maxv + 1;
    int sz = 1;
    while (sz < need) sz <<= 1;

    vector<cd> a(sz);
    for (int x : S) {
        a[x] = 1;
    }

    fft(a, false);
    for (int i = 0; i < sz; i++) {
        a[i] *= a[i];
    }
    fft(a, true);

    long long result = 0;
    for (int b : S) {
        int idx = 2 * b;
        if (idx < sz) {
            long long m = (long long)(a[idx].real() + 0.5);
            // subtract the (b,b) pair, then each fine triplet counted twice
            result += (m - 1) / 2;
        }
    }

    cout << result << "\n";
    return 0;
}