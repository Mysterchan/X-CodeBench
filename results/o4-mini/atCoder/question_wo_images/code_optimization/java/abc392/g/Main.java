#include <bits/stdc++.h>
using namespace std;
using cd = complex<double>;
const double PI = acos(-1);

void fft(vector<cd> & a, bool invert) {
    int n = a.size();
    static vector<int> rev;
    static vector<cd> roots{ {0,0}, {1,0} };
    if ((int)rev.size() != n) {
        int k = __builtin_ctz(n);
        rev.assign(n,0);
        for (int i = 0; i < n; i++) {
            rev[i] = (rev[i>>1] >> 1) | ((i&1) << (k-1));
        }
    }
    if ((int)roots.size() < n) {
        // compute roots
        roots.resize(n);
        for (int len = roots.size()>>1; len < n; len <<= 1) {
            double ang = 2 * PI / (len<<1);
            for (int i = len; i < (len<<1); i++) {
                roots[i] = cd(cos(ang*(i-len)), sin(ang*(i-len)));
            }
        }
    }
    for (int i = 0; i < n; i++) {
        if (i < rev[i]) swap(a[i], a[rev[i]]);
    }
    for (int len = 1; len < n; len <<= 1) {
        for (int i = 0; i < n; i += (len<<1)) {
            for (int j = 0; j < len; j++) {
                cd u = a[i+j];
                cd v = a[i+j+len] * roots[len+j];
                a[i+j] = u + v;
                a[i+j+len] = u - v;
            }
        }
    }
    if (invert) {
        reverse(a.begin() + 1, a.end());
        for (int i = 0; i < n; i++)
            a[i] /= n;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    vector<int> S(N);
    int maxVal = 0;
    for (int i = 0; i < N; i++) {
        cin >> S[i];
        if (S[i] > maxVal) maxVal = S[i];
    }

    int m = maxVal;
    int L = 1;
    while (L <= 2*m) L <<= 1;

    vector<cd> fa(L);
    for (int v : S) {
        fa[v] = 1.0;
    }

    fft(fa, false);
    for (int i = 0; i < L; i++) {
        fa[i] *= fa[i];
    }
    fft(fa, true);

    vector<long long> g(2*m+1);
    for (int i = 0; i <= 2*m; i++) {
        long long val = (long long)(fa[i].real() + 0.5);
        g[i] = val;
    }

    long long count = 0;
    for (int v : S) {
        int idx = 2 * v;
        if (idx <= 2*m) {
            // subtract self-pair and divide by 2
            long long tot = g[idx] - 1;
            if (tot > 0) count += tot / 2;
        }
    }

    cout << count << "\n";
    return 0;
}