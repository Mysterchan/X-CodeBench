#include <bits/stdc++.h>
using namespace std;

const int N = 35;
int n, mod;
long long C[N*N][N*N];
long long S[N][N][N*N];

inline int add(int x, int y) {
    x += y;
    return x >= mod ? x - mod : x;
}

inline int mul(long long x, long long y) {
    return (x * y) % mod;
}

void precompute() {
    int maxn = n * n / 2 + 1;
    for(int i = 0; i < maxn; i++) {
        C[i][0] = 1;
        for(int j = 1; j <= min(i, n); j++) {
            C[i][j] = (C[i-1][j-1] + C[i-1][j]) % mod;
        }
    }
    
    for(int m = 1; m <= n; m++) {
        for(int d = 1; d <= n - m; d++) {
            if(d == 1) {
                for(int e = d; e <= n * (n - 1) / 2; e++) {
                    S[m][d][e] = C[m][e];
                }
            } else {
                for(int e = d; e <= n * (n - 1) / 2; e++) {
                    long long sum = 0;
                    for(int t = 1; t <= e; t++) {
                        long long diff = (C[d - 1 + m][t] - C[d - 1][t] + mod) % mod;
                        sum = (sum + S[m][d - 1][e - t] * diff) % mod;
                    }
                    S[m][d][e] = sum;
                }
            }
        }
    }
}

int main() {
    scanf("%d %d", &n, &mod);
    precompute();
    
    int M = n * (n - 1) / 2;
    
    // Use map for sparse DP
    map<tuple<int,int,int,int,int>, int> f, nf;
    f[make_tuple(1, 0, 0, n, 1)] = 1;
    
    for(int i = 1; i < n; i++) {
        nf.clear();
        for(auto& [state, val] : f) {
            auto [vi, j, k, l, m] = state;
            
            for(int d = 1; d <= n - i; d++) {
                long long cmb = C[n - i][d];
                for(int e = d; e <= M - j; e++) {
                    long long contrib = mul(mul(val, cmb), S[m][d][e]);
                    auto nstate = make_tuple(i + d, j + e, k ^ 1, l + ((k & 1) ? 1 : -1) * d, d);
                    nf[nstate] = add(nf[nstate], contrib);
                }
            }
        }
        swap(f, nf);
    }
    
    for(int m = n - 1; m <= M; m++) {
        int ans = 0;
        for(auto& [state, val] : f) {
            auto [vi, j, k, l, mm] = state;
            if(j == m && l == n) {
                ans = add(ans, val);
            }
        }
        printf("%d ", ans);
    }
    puts("");
    
    return 0;
}