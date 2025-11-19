#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct Fenwick {
    int n;
    vector<int> f;
    Fenwick(int _n): n(_n), f(n+1, 0) {}
    // add v at index i
    void update(int i, int v=1) {
        for (; i <= n; i += i & -i) f[i] += v;
    }
    // sum of [1..i]
    int query(int i) const {
        int s = 0;
        for (; i > 0; i -= i & -i) s += f[i];
        return s;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    vector<int> A(N+1);
    for (int i = 1; i <= N; i++) {
        cin >> A[i];
    }
    // Maximum possible T value is up to A[i] + D[i] + i <= 5e5+5e5+5e5 = 1.5e6
    int M = 1500005;
    Fenwick bit(M);

    vector<int> T(N+1), D(N+1), B(N+1);
    // Process each alien
    for (int j = 1; j <= N; j++) {
        if (j == 1) {
            D[j] = 0;
        } else {
            // count of previous k with T_k >= j is (j-1) - count of T_k < j
            int lessCount = bit.query(j-1);
            D[j] = (j - 1) - lessCount;
        }
        T[j] = A[j] + D[j] + j;
        if (T[j] > M) T[j] = M; // safety cap, though should not exceed
        bit.update(T[j], 1);
    }

    // Compute final stones
    for (int i = 1; i <= N; i++) {
        int x = T[i] - N;
        if (x < 0) x = 0;
        B[i] = x;
    }
    // Output
    for (int i = 1; i <= N; i++) {
        cout << B[i] << (i==N?'\n':' ');
    }

    return 0;
}