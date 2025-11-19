#include <bits/stdc++.h>
using namespace std;
const int MOD = 998244353;
int add(int a, int b) { a += b; if (a >= MOD) a -= MOD; return a; }
int subm(int a, int b) { a -= b; if (a < 0) a += MOD; return a; }
int mul(int a, int b) { return (int)((long long)a * b % MOD); }

int N, M;
int pnt[2025+5];
int state_v[2025+5], bel[2025+5];
bool done_dp[2025+5];
vector<int> cycles_nodes[2025+5];
int cycles_cnt = 0;
vector<int> children_[2025+5];
int f_dp[2025+5][2025+5]; // f_dp[u][s], s=0..M

void dfs_dp(int u) {
    if (done_dp[u]) return;
    for (int v : children_[u]) {
        if (!done_dp[v]) dfs_dp(v);
    }
    // compute g[s] = product of f_dp[v][s] for v in children_[u]
    // then f_dp[u][s] = prefix sum of g[s]
    f_dp[u][0] = 0;
    // We can compute on the fly without extra array
    // First for s=1..M compute g and prefix
    int pref = 0;
    for (int s = 1; s <= M; ++s) {
        int g = 1;
        for (int v : children_[u]) {
            g = mul(g, f_dp[v][s]);
        }
        pref = add(pref, g);
        f_dp[u][s] = pref;
    }
    done_dp[u] = true;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;
    for (int i = 0; i < N; ++i) {
        int a; cin >> a;
        pnt[i] = a - 1;
    }
    // init
    for (int i = 0; i < N; ++i) {
        state_v[i] = 0;
        bel[i] = -1;
    }
    // find cycles in functional graph
    for (int i = 0; i < N; ++i) {
        if (state_v[i] != 0) continue;
        int u = i;
        vector<int> path;
        while (state_v[u] == 0) {
            state_v[u] = 1;
            path.push_back(u);
            u = pnt[u];
        }
        if (state_v[u] == 1) {
            // found cycle starting at u
            int idx = (int)path.size() - 1;
            vector<int> cyc;
            while (path[idx] != u) {
                cyc.push_back(path[idx]);
                idx--;
            }
            cyc.push_back(u);
            // assign cycle id
            for (int v : cyc) {
                bel[v] = cycles_cnt;
            }
            cycles_nodes[cycles_cnt] = cyc;
            cycles_cnt++;
        }
        for (int v : path) state_v[v] = 2;
    }
    // build children excluding cycle edges
    for (int i = 0; i < N; ++i) {
        int j = pnt[i];
        if (bel[i] >= 0 && bel[j] >= 0 && bel[i] == bel[j]) {
            // cycle edge, skip
        } else {
            children_[j].push_back(i);
        }
    }
    // init dp done flags
    for (int i = 0; i < N; ++i) done_dp[i] = false;
    // For each cycle, compute dp for cycle nodes and their trees
    long long ans = 1;
    for (int cid = 0; cid < cycles_cnt; ++cid) {
        // compute dp for all nodes in this cycle (and their subtrees)
        for (int u : cycles_nodes[cid]) {
            dfs_dp(u);
        }
        // compute contribution of this cycle
        vector<int> G(M+1, 1);
        for (int u : cycles_nodes[cid]) {
            // g_u[s] = f_dp[u][s] - f_dp[u][s-1]
            for (int s = 1; s <= M; ++s) {
                int gu = subm(f_dp[u][s], f_dp[u][s-1]);
                G[s] = mul(G[s], gu);
            }
        }
        int sumc = 0;
        for (int s = 1; s <= M; ++s) {
            sumc = add(sumc, G[s]);
        }
        ans = ans * sumc % MOD;
    }
    cout << ans << "\n";
    return 0;
}