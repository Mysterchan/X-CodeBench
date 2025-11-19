#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <set>
#include <map>


long long power(long long base, long long exp) {
    long long res = 1;
    base %= 1000000007;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % 1000000007;
        base = (base * base) % 1000000007;
        exp /= 2;
    }
    return res;
}


long long modInverse(long long n) {
    return power(n, 1000000007 - 2);
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

    std::vector<long long> b0(n);
    for (int i = 0; i < n; ++i) {
        b0[i] = a[i] - (i + 1);
        val_set.insert(b0[i]);
    }

    std::map<long long, std::vector<int>> ops_by_T;
    for (int i = 0; i < q; ++i) {
        std::cin >> ops[i].first >> ops[i].second;
        T[i] = ops[i].second - ops[i].first;
        val_set.insert(T[i]);
        ops_by_T[T[i]].push_back(ops[i].first);
    }

    std::vector<long long> V(val_set.begin(), val_set.end());
    int L = V.size();

    if (q == 0) {
        for (int j = 1; j <= n; ++j) {
            long long final_ans = (b0[j-1] + j);
            final_ans = (final_ans % 1000000007 + 1000000007) % 1000000007;
            std::cout << final_ans << (j == n ? "" : " ");
        }
        std::cout << std::endl;
        return;
    }

    std::vector<long long> E_b(n + 1, 0);
    
    std::vector<int> ops_at_j_ge_v(n + 1, 0);
    std::vector<int> ops_at_j_lt_v(n + 1, 0);
    
    
    int d_total_lt_v = 0;
    for (int k = 0; k < q; ++k) {
        if (T[k] >= V[0]) {
            ops_at_j_ge_v[ops[k].first]++;
        } else {
            ops_at_j_lt_v[ops[k].first]++;
            d_total_lt_v++;
        }
    }

    for (int l = 0; l < L; ++l) {
        long long v = V[l];

       
        if (l > 0) {
            long long v_prev = V[l - 1];
            if (ops_by_T.count(v_prev)) {
                for (int i_k : ops_by_T[v_prev]) {
                    
                    ops_at_j_ge_v[i_k]--;
                    ops_at_j_lt_v[i_k]++;
                    d_total_lt_v++;
                }
            }
        }

       
        int u = 0;
        int d_prefix_sum_lt = 0;
        for (int j = 1; j <= n; ++j) {
            u += ops_at_j_ge_v[j];
            int d = d_total_lt_v - d_prefix_sum_lt;

            long long prob_ge_v = 0;
            if (u + d == 0) {
                if (b0[j - 1] >= v) {
                    prob_ge_v = 1;
                }
            } else {
                prob_ge_v = (static_cast<long long>(u) * modInverse(u + d)) % 1000000007;
            }

            long long term;
            if (l == 0) {
                long long v_mod = (v % 1000000007 + 1000000007) % 1000000007;
                term = (v_mod * prob_ge_v) % 1000000007;
            } else {
                long long v_prev = V[l-1];
                long long delta_v = v - v_prev;
                long long delta_v_mod = delta_v % 1000000007;
                term = (delta_v_mod * prob_ge_v) % 1000000007;
            }
            E_b[j] = (E_b[j] + term + 1000000007) % 1000000007;
            
            d_prefix_sum_lt += ops_at_j_lt_v[j];
        }
    }

    long long q_fact = 1;
    for (int i = 1; i <= q; ++i) {
        q_fact = (q_fact * i) % 1000000007;
    }

    for (int j = 1; j <= n; ++j) {
        long long total_b_sum = (q_fact * E_b[j]) % 1000000007;
        long long pos_offset = (q_fact * j) % 1000000007;
        long long final_ans = (total_b_sum + pos_offset) % 1000000007;
        std::cout << final_ans << (j == n ? "" : " ");
    }
    std::cout << std::endl;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    int t;
    std::cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}