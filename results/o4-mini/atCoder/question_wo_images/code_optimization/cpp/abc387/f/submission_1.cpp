#include <bits/stdc++.h>
using namespace std;
const int MOD = 998244353;
const int MAXN = 2025;
int N, M;
int A[MAXN+1];
bool visited1[MAXN+1], onStack[MAXN+1], inCycle[MAXN+1], visited2[MAXN+1];
vector<int> children[MAXN+1];
vector<vector<int>> cycles;
int dp[MAXN+1][MAXN+1];
int preSum[MAXN+1][MAXN+1];
vector<int> postOrder;

void dfsOrder(int u) {
    visited2[u] = true;
    for (int v : children[u]) {
        if (!visited2[v]) dfsOrder(v);
    }
    postOrder.push_back(u);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;
    for (int i = 1; i <= N; i++) {
        cin >> A[i];
    }
    // detect cycles
    for (int i = 1; i <= N; i++) {
        if (visited1[i]) continue;
        int u = i;
        vector<int> path;
        while (!visited1[u]) {
            visited1[u] = true;
            path.push_back(u);
            onStack[u] = true;
            u = A[u];
        }
        if (onStack[u]) {
            // u is start of a cycle
            vector<int> cyc;
            int idx = (int)path.size() - 1;
            while (idx >= 0 && path[idx] != u) idx--;
            for (int j = idx; j < (int)path.size(); j++) {
                int node = path[j];
                inCycle[node] = true;
                cyc.push_back(node);
            }
            cycles.push_back(cyc);
        }
        for (int x : path) onStack[x] = false;
    }
    // build children excluding cycle edges
    for (int i = 1; i <= N; i++) {
        int p = A[i];
        if (inCycle[i] && inCycle[p]) {
            // skip cycle edge
        } else {
            children[p].push_back(i);
        }
    }
    // get post-order from all cycle nodes
    postOrder.reserve(N);
    for (auto &cyc : cycles) {
        for (int r : cyc) {
            if (!visited2[r]) dfsOrder(r);
        }
    }
    // DP in post-order
    for (int u : postOrder) {
        // compute dp[u][val] for val=1..M
        for (int val = 1; val <= M; val++) {
            long long prod = 1;
            for (int c : children[u]) {
                prod = prod * preSum[c][val] % MOD;
            }
            dp[u][val] = (int)prod;
        }
        // build preSum[u][*]
        preSum[u][0] = 0;
        int acc = 0;
        for (int val = 1; val <= M; val++) {
            acc += dp[u][val];
            if (acc >= MOD) acc -= MOD;
            preSum[u][val] = acc;
        }
    }
    // compute answer per cycle component
    long long answer = 1;
    for (auto &cyc : cycles) {
        long long compWays = 0;
        for (int val = 1; val <= M; val++) {
            long long prod = 1;
            for (int r : cyc) {
                prod = prod * dp[r][val] % MOD;
            }
            compWays += prod;
            if (compWays >= MOD) compWays -= MOD;
        }
        answer = answer * compWays % MOD;
    }
    cout << answer << "\n";
    return 0;
}