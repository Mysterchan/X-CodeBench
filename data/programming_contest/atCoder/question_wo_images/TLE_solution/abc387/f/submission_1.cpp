#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

const long long MOD = 998244353;
const int MAXN =3000;

int N, M, A[MAXN];
int color[MAXN];
int cycle_id[MAXN];
int comp_root[MAXN];
vector<int> ch[MAXN];
long long dp[MAXN][MAXN];
bool vis[MAXN][MAXN];

void dfs(int u) {
    color[u] = 1;
    int v = A[u];
    
    if (color[v] == 0) {
        dfs(v);
    } else if (color[v] == 1) {
        int cyc_id = v;
        int cur = v;
        do {
            cycle_id[cur] = cyc_id;
            comp_root[cur] = cyc_id;
            cur = A[cur];
        } while (cur != v);
    }
    
    if (comp_root[v] != -1 && comp_root[u] == -1) {
        comp_root[u] = comp_root[v];
    }
    
    color[u] = 2;
}

long long solve(int node, int max_val) {
    if (max_val <= 0) return 0;
    if (vis[node][max_val]) return dp[node][max_val];
    
    vis[node][max_val] = true;
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
    
    for (int i = 1; i <= N; i++) {
        if (color[i] == 0) {
            dfs(i);
        }
    }
    
    for (int i = 1; i <= N; i++) {
        if (comp_root[i] == -1) {
            int cur = i;
            while (comp_root[cur] == -1) {
                cur = A[cur];
            }
            comp_root[i] = comp_root[cur];
        }
    }
    
    vector<bool> done(N + 1);
    long long ans = 1;
    
    for (int i = 1; i <= N; i++) {
        if (done[i] || comp_root[i] == -1) continue;
        
        int root = comp_root[i];
        if (done[root]) continue;
        
        vector<int> cyc;
        int cur = root;
        do {
            cyc.push_back(cur);
            done[cur] = true;
            cur = A[cur];
        } while (cur != root);
        
        for (int j = 1; j <= N; j++) {
            if (comp_root[j] == root) {
                done[j] = true;
            }
        }
        
        long long total = 0;
        for (int val = 1; val <= M; val++) {
            long long ways = 1;
            for (int node : cyc) {
                for (int c : ch[node]) {
                    if (cycle_id[c] == -1 || cycle_id[c] != cycle_id[node]) {
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