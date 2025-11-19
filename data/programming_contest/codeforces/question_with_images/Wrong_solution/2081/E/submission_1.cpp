#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using ll = long long;

const int MOD = 998244353;

std::vector<std::vector<int>> adj; 
std::vector<int> entry_time;
std::vector<int> exit_time;
int timer;


void dfs_timer(int u) {
    timer++;
    entry_time[u] = timer;
    if (u >= 0 && u < adj.size()) {
        for (int v : adj[u]) {
            if (v >= 0 && v < adj.size()) {
                dfs_timer(v);
            }
        }
    }
    timer++;
    exit_time[u] = timer;
}


bool is_ancestor(int u, int v, int n) {
    if (u < 0 || u > n || v < 0 || v > n) return false; 
    if (u == v) return true; 
    if (u == 0) return v != 0; 
    if (v == 0) return false; 
    
    if (u < 0 || u >= entry_time.size() || v < 0 || v >= entry_time.size()) return false; 
    if (entry_time[u] == 0 || entry_time[v] == 0) return false; 

    return entry_time[u] <= entry_time[v] && exit_time[u] >= exit_time[v];
}

std::vector<std::vector<int>> rev_constraint_adj; // Stores prerequisites: rev_constraint_adj[j] contains indices i such that chip i must precede chip j
std::vector<ll> dp; // DP table for counting topological sorts. dp[mask] stores the number of ways to arrange chips in the subset represented by mask.
int M; // Number of chips

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int t; // Number of test cases
    std::cin >> t;
    while (t--) {
        int n; // Number of nodes in the tree is n+1 (labeled 0 to n)
        std::cin >> n >> M; // Read n and number of chips M

        adj.assign(n + 1, std::vector<int>());
        for (int i = 1; i <= n; ++i) {
            int p_i; // Parent of node i
            std::cin >> p_i;
            if (p_i >= 0 && p_i <= n) {
               adj[p_i].push_back(i);
            }
        }

        std::vector<int> colors(M); 
        for (int i = 0; i < M; ++i) {
            std::cin >> colors[i];
        }
        std::vector<int> d(M); 
        for (int i = 0; i < M; ++i) {
            std::cin >> d[i];
        }

        entry_time.assign(n + 1, 0);
        exit_time.assign(n + 1, 0);
        timer = 0;
        if (n >= 0) { 
             dfs_timer(0); // Start DFS from the root node 0
        }

        rev_constraint_adj.assign(M, std::vector<int>());
        for (int i = 0; i < M; ++i) {
            for (int j = i + 1; j < M; ++j) { // Consider pairs of distinct chips (i, j) with i < j
                if (colors[i] != colors[j]) { // Constraints only apply between chips of different colors
                    bool i_anc_j = is_ancestor(d[i], d[j], n);
                    bool j_anc_i = is_ancestor(d[j], d[i], n);
                    if (i_anc_j || j_anc_i) {
                        rev_constraint_adj[j].push_back(i); 
                    }
                }
            }
        }
        
        dp.assign(1 << M, 0);
        dp[0] = 1; // Base case: There is one way to arrange an empty set of chips (empty sequence).

        for (int mask = 1; mask < (1 << M); ++mask) {
            for (int i = 0; i < M; ++i) {
                if (mask & (1 << i)) { 
                    int prev_mask = mask ^ (1 << i); 
                    
                    bool possible = true; // Assume chip 'i' can be the last element added
                    for (int prereq_idx : rev_constraint_adj[i]) {
                        if (!(prev_mask & (1 << prereq_idx))) { 
                            possible = false; // Then chip 'i' cannot be the last one added to form 'mask' from 'prev_mask'
                            break; // Stop checking prerequisites for chip 'i'
                        }
                    }
                    
                    if (possible) {
                        dp[mask] = (dp[mask] + dp[prev_mask]) % MOD;
                    }
                }
            }
        }

        std::cout << dp[(1 << M) - 1] << "\n";
    }
    return 0;
}