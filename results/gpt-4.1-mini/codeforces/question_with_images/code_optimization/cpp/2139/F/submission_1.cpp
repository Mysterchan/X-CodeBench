#include <iostream>
#include <vector>
#include <map>
#include <set>

constexpr int MOD = 1000000007;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return res;
}

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

void solve() {
    int n;
    long long m;
    int q;
    std::cin >> n >> m >> q;

    std::vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }

    std::vector<std::pair<int, long long>> ops(q);
    std::vector<long long> T(q);
    std::set<long long> val_set;

    // Precompute b0[i] = a[i] - (i+1)
    std::vector<long long> b0(n);
    for (int i = 0; i < n; ++i) {
        b0[i] = a[i] - (i + 1);
        val_set.insert(b0[i]);
    }

    // Read operations and compute T[i] = x - i
    std::map<long long, std::vector<int>> ops_by_T;
    for (int i = 0; i < q; ++i) {
        int idx; long long x;
        std::cin >> idx >> x;
        ops[i] = {idx, x};
        T[i] = x - idx;
        val_set.insert(T[i]);
        ops_by_T[T[i]].push_back(idx);
    }

    // If no operations, just output initial positions mod
    if (q == 0) {
        for (int j = 1; j <= n; ++j) {
            long long ans = (b0[j - 1] + j) % MOD;
            if (ans < 0) ans += MOD;
            std::cout << ans << (j == n ? "\n" : " ");
        }
        return;
    }

    // Extract sorted unique values of b0 and T
    std::vector<long long> V(val_set.begin(), val_set.end());
    int L = (int)V.size();

    // ops_at_j_ge_v[j]: number of operations on slider j with T >= current v
    // ops_at_j_lt_v[j]: number of operations on slider j with T < current v
    std::vector<int> ops_at_j_ge_v(n + 1, 0);
    std::vector<int> ops_at_j_lt_v(n + 1, 0);

    // Initialize counts for v = V[0]
    int d_total_lt_v = 0;
    for (int k = 0; k < q; ++k) {
        if (T[k] >= V[0]) {
            ops_at_j_ge_v[ops[k].first]++;
        } else {
            ops_at_j_lt_v[ops[k].first]++;
            d_total_lt_v++;
        }
    }

    std::vector<long long> E_b(n + 1, 0); // Expected b for each slider

    // Precompute factorial q! mod
    long long q_fact = 1;
    for (int i = 1; i <= q; ++i) {
        q_fact = (q_fact * i) % MOD;
    }

    // Iterate over all unique values v in ascending order
    for (int l = 0; l < L; ++l) {
        long long v = V[l];

        // For l > 0, update ops_at_j_ge_v and ops_at_j_lt_v by moving ops with T = V[l-1]
        if (l > 0) {
            long long v_prev = V[l - 1];
            auto it = ops_by_T.find(v_prev);
            if (it != ops_by_T.end()) {
                for (int idx : it->second) {
                    ops_at_j_ge_v[idx]--;
                    ops_at_j_lt_v[idx]++;
                    d_total_lt_v++;
                }
            }
        }

        int u = 0; // sum of ops_at_j_ge_v for sliders <= j
        int d_prefix_sum_lt = 0; // sum of ops_at_j_lt_v for sliders < j

        for (int j = 1; j <= n; ++j) {
            u += ops_at_j_ge_v[j];
            int d = d_total_lt_v - d_prefix_sum_lt;

            long long prob_ge_v = 0;
            if (u + d == 0) {
                // No operations on slider j, so probability depends on b0[j-1]
                prob_ge_v = (b0[j - 1] >= v) ? 1 : 0;
            } else {
                // Probability that the last operation on slider j has T >= v
                prob_ge_v = (static_cast<long long>(u) * modInverse(u + d)) % MOD;
            }

            long long term;
            if (l == 0) {
                long long v_mod = (v % MOD + MOD) % MOD;
                term = (v_mod * prob_ge_v) % MOD;
            } else {
                long long v_prev = V[l - 1];
                long long delta_v = v - v_prev;
                long long delta_v_mod = (delta_v % MOD + MOD) % MOD;
                term = (delta_v_mod * prob_ge_v) % MOD;
            }
            E_b[j] = (E_b[j] + term) % MOD;

            d_prefix_sum_lt += ops_at_j_lt_v[j];
        }
    }

    // Output final results: sum over all permutations = q! * E[b_j] + q! * j
    for (int j = 1; j <= n; ++j) {
        long long total_b_sum = (q_fact * E_b[j]) % MOD;
        long long pos_offset = (q_fact * j) % MOD;
        long long final_ans = (total_b_sum + pos_offset) % MOD;
        std::cout << final_ans << (j == n ? "\n" : " ");
    }
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t; std::cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}