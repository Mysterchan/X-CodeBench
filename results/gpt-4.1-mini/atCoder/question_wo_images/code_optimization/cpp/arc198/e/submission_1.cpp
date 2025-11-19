#include <bits/stdc++.h>
using namespace std;

constexpr int MOD = 998244353;

struct Mint {
    int v;
    Mint(long long x = 0) {
        if (x < 0) x = x % MOD + MOD;
        if (x >= MOD) x %= MOD;
        v = int(x);
    }
    Mint& operator+=(const Mint &a) {
        if ((v += a.v) >= MOD) v -= MOD;
        return *this;
    }
    Mint& operator-=(const Mint &a) {
        if ((v -= a.v) < 0) v += MOD;
        return *this;
    }
    Mint& operator*=(const Mint &a) {
        v = int((long long)v * a.v % MOD);
        return *this;
    }
    friend Mint operator+(Mint a, const Mint &b) { return a += b; }
    friend Mint operator-(Mint a, const Mint &b) { return a -= b; }
    friend Mint operator*(Mint a, const Mint &b) { return a *= b; }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M; cin >> N >> M;
    int max_mask = (1 << N) - 1;

    vector<int> c(max_mask + 1, 0);
    for (int i = 0; i < M; i++) {
        int x; cin >> x;
        c[x]++;
    }

    // Fast zeta transform (superset sum) on c
    // c[S] = sum of counts of all subsets of S
    for (int i = 0; i < N; i++) {
        for (int mask = 0; mask <= max_mask; mask++) {
            if ((mask & (1 << i)) == 0) {
                c[mask] += c[mask | (1 << i)];
            }
        }
    }

    // DP arrays
    // f[S]: number of ways to reach state S
    // A[S], B[S]: auxiliary arrays for divide and conquer DP
    vector<Mint> f(max_mask + 1, 0), A(max_mask + 1, 0), B(max_mask + 1, 0);

    // Recursive function to solve DP using divide and conquer on bits
    function<void(int,int)> solve = [&](int S, int bit) {
        if (bit < 0) {
            // Base case
            A[S] = (S == 0 ? Mint(1) : f[S - 1]);
            f[S] += A[S] * c[S];
            B[S] = f[S];
            return;
        }
        solve(S, bit - 1);
        int len = 1 << bit;
        for (int i = S; i < S + len; i++) {
            int nxt = i | len;
            f[nxt] += A[i] * c[nxt] - B[i];
        }
        solve(S | len, bit - 1);
        for (int i = S; i < S + len; i++) {
            int nxt = i | len;
            A[nxt] += A[i];
            B[nxt] += B[i];
        }
    };

    solve(0, N - 1);

    cout << f[max_mask].v << "\n";

    return 0;
}