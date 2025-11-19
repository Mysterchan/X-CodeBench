#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

const long long MOD = 998244353;
const int MAXN = 2030;

int N, M, A[MAXN];
int cycle_id[MAXN];
int comp_root[MAXN];
vector<int> ch[MAXN];
long long dp[MAXN][MAXN];

void find_cycles_and_components() {
    vector<int> color(N + 1, 0);
    
    for (int start = 1; start <= N; start++) {
        if (color[start] != 0) continue;
        
        vector<int> path;
        int cur = start;
        
        while (color[cur] == 0) {
            color[cur] = -1;
            path.push_back(cur);
            cur = A[cur];
        }
        
        if (color[cur] == -1) {
            int cyc_start = cur;
            bool in_cycle = false;
            for (int node : path) {
                if (node == cyc_start) in_cycle = true;
                if (in_cycle) {
                    cycle_id[node] = cyc_start;
                    comp_root[node] = cyc_start;
                    color[node] = 2;
                }
            }
            for (int node : path) {
                if (color[node] != 2) {
                    comp_root[node] = comp_root[A[node]];
                    color[node] = 2;
                }
            }
        } else {
            for (int node : path) {
                comp_root[node] = comp_root[cur];
                color[node] = 2;
            }
        }
    }
}

long long solve(int node, int max_val) {
    if (max_val <= 0) return 0;
    if (dp[node][max_val] != -1) return dp[node][max_val];
    
    if (ch[node].empty()) {
        return dp[node][max_val] = max_val;
    }
    
    long long res = 0;
    
    for (int v = 1; v <= max_val; v++) {
        long long ways = 1;
        for (int c : ch[node]) {
            ways = ways * solve(c, v) % MOD;
        }
        res = (res + ways) % MOD;
    }
    
    return dp[node][max_val] = res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    cin >> N >> M;
    for (int i = 1; i <= N; i++) {
        cin >> A[i];
        cycle_id[i] = -1;
        comp_root[i] = -1;
    }
    
    for (int i = 1; i <= N; i++) {
        ch[A[i]].push_back(i);
    }
    
    find_cycles_and_components();
    
    memset(dp, -1, sizeof(dp));
    
    vector<bool> processed(N + 1);
    long long ans = 1;
    
    for (int i = 1; i <= N; i++) {
        int root = comp_root[i];
        if (root == -1 || processed[root]) continue;
        
        processed[root] = true;
        
        vector<int> cyc;
        int cur = root;
        do {
            cyc.push_back(cur);
            cur = A[cur];
        } while (cur != root);
        
        long long total = 0;
        for (int val = 1; val <= M; val++) {
            long long ways = 1;
            for (int node : cyc) {
                for (int c : ch[node]) {
                    if (cycle_id[c] != cycle_id[node]) {
                        ways = ways * solve(c, val) % MOD;
                    }
                }
            }
            total = (total + ways) % MOD;
        }
        
        ans = ans * total % MOD;
    }
    
    cout << ans << endl;
    
    return 0;
}