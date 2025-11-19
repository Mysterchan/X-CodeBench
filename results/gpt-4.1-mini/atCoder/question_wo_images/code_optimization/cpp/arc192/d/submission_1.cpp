#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;
const int MAXN = 1000;
const int MAXA = 1000;

int n, a[MAXN];
int dp[2][MAXA + 1][2]; // dp arrays for current and next states
int pw[MAXA + 1];

// Modular addition
inline void add(int &x, int y) {
    x += y;
    if (x >= MOD) x -= MOD;
}

// Check if prime (simple sieve for up to 1000)
bool is_prime(int x) {
    if (x < 2) return false;
    for (int i = 2; i * i <= x; i++)
        if (x % i == 0) return false;
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    int maxA = 0;
    for (int i = 1; i < n; i++) {
        cin >> a[i];
        maxA = max(maxA, a[i]);
    }

    int ans = 1;

    // For each prime factor, process independently
    for (int x = 2; x <= maxA; x++) {
        if (!is_prime(x)) continue;

        // Extract exponents of prime x in each A[i]
        int p[MAXN] = {};
        for (int i = 1; i < n; i++) {
            int cnt = 0;
            int val = a[i];
            while (val % x == 0) {
                val /= x;
                cnt++;
            }
            p[i] = cnt;
        }

        // Precompute powers of x modulo MOD
        pw[0] = 1;
        for (int i = 1; i <= MAXA; i++) {
            pw[i] = (int)((long long)pw[i - 1] * x % MOD);
        }

        // Initialize dp
        // dp[d][j][k]: 
        // d - parity for rolling array
        // j - current exponent sum state (<= MAXA)
        // k - flag: 0 if gcd condition not yet met, 1 if met
        int d = 0;
        for (int j = 0; j <= MAXA; j++) {
            dp[d][j][0] = 0;
            dp[d][j][1] = 0;
        }
        // Base case: no elements yet, gcd condition not met
        // For the first element, exponent can be 0 or 1? Actually, start with dp[0][0][0] = 1
        dp[d][0][0] = 1;

        for (int i = 1; i < n; i++) {
            int nd = d ^ 1;
            for (int j = 0; j <= MAXA; j++) {
                dp[nd][j][0] = 0;
                dp[nd][j][1] = 0;
            }

            if (p[i] == 0) {
                // If exponent zero, no change in exponent sum
                for (int j = 0; j <= MAXA; j++) {
                    if (dp[d][j][0]) {
                        // Multiply by pw[j] (x^j)
                        int val = (int)((long long)dp[d][j][0] * pw[j] % MOD);
                        add(dp[nd][j][0], val);
                    }
                    if (dp[d][j][1]) {
                        int val = (int)((long long)dp[d][j][1] * pw[j] % MOD);
                        add(dp[nd][j][1], val);
                    }
                }
            } else {
                int pi = p[i];
                // For each j, update dp accordingly
                // The transitions are:
                // dp[nd][j+pi][0] += dp[d][j][0] * pw[j+pi]
                // dp[nd][j+pi][1] += dp[d][j][1] * pw[j+pi]
                // dp[nd][0][1] += dp[d][pi][0] + dp[d][pi][1]
                // dp[nd][j-pi][0] += dp[d][j][0] * pw[j-pi]
                // dp[nd][j-pi][1] += dp[d][j][1] * pw[j-pi]
                // with j >= pi for last two

                // To avoid repeated computations, do in steps:

                // 1) j from 0 to MAXA - pi: dp[d][j][*] -> dp[nd][j+pi][*]
                for (int j = 0; j <= MAXA - pi; j++) {
                    if (dp[d][j][0]) {
                        int val = (int)((long long)dp[d][j][0] * pw[j + pi] % MOD);
                        add(dp[nd][j + pi][0], val);
                    }
                    if (dp[d][j][1]) {
                        int val = (int)((long long)dp[d][j][1] * pw[j + pi] % MOD);
                        add(dp[nd][j + pi][1], val);
                    }
                }

                // 2) dp[nd][0][1] += dp[d][pi][0] + dp[d][pi][1]
                add(dp[nd][0][1], dp[d][pi][0]);
                add(dp[nd][0][1], dp[d][pi][1]);

                // 3) j from pi+1 to MAXA: dp[d][j][*] -> dp[nd][j-pi][*]
                for (int j = pi + 1; j <= MAXA; j++) {
                    if (dp[d][j][0]) {
                        int val = (int)((long long)dp[d][j][0] * pw[j - pi] % MOD);
                        add(dp[nd][j - pi][0], val);
                    }
                    if (dp[d][j][1]) {
                        int val = (int)((long long)dp[d][j][1] * pw[j - pi] % MOD);
                        add(dp[nd][j - pi][1], val);
                    }
                }
            }
            d = nd;
        }

        // Sum over dp[d][j][1] for all j
        int sum = 0;
        for (int j = 0; j <= MAXA; j++) {
            add(sum, dp[d][j][1]);
        }

        ans = (int)((long long)ans * sum % MOD);
    }

    cout << ans << "\n";

    return 0;
}