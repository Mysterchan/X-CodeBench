#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int MOD = 998244353;

int addmod(int a, int b) {
    int c = a + b;
    if (c >= MOD) c -= MOD;
    return c;
}

int mulmod(ll a, ll b) {
    return int((a * b) % MOD);
}

int N, M;
vector<int> A;
vector<int> state_arr;
vector<vector<int>> cycles;
vector<bool> inCycle;

void dfsCycle(int u) {
    state_arr[u] = 1;
    int v = A[u];
    if (state_arr[v] == 0) {
        dfsCycle(v);
    } else if (state_arr[v] == 1) {
        // found a cycle
        vector<int> cyc;
        int x = v;
        do {
            cyc.push_back(x);
            x = A[x];
        } while (x != v);
        cycles.push_back(cyc);
    }
    state_arr[u] = 2;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;
    A.assign(N+1, 0);
    for (int i = 1; i <= N; i++) {
        cin >> A[i];
    }

    state_arr.assign(N+1, 0);
    inCycle.assign(N+1, false);

    // find cycles
    for (int i = 1; i <= N; i++) {
        if (state_arr[i] == 0) {
            dfsCycle(i);
        }
    }
    // mark inCycle
    for (auto &cyc : cycles) {
        for (int u : cyc) {
            inCycle[u] = true;
        }
    }

    // assign compId
    vector<int> compId(N+1, -1);
    int compCount = 0;
    for (auto &cyc : cycles) {
        for (int u : cyc) {
            compId[u] = compCount;
        }
        compCount++;
    }
    // singletons for non-cycle
    for (int i = 1; i <= N; i++) {
        if (compId[i] == -1) {
            compId[i] = compCount++;
        }
    }

    // build component graph
    vector<vector<int>> compAdj(compCount);
    vector<int> indegree(compCount, 0);
    for (int i = 1; i <= N; i++) {
        int cu = compId[i], cv = compId[A[i]];
        if (cu != cv) {
            compAdj[cv].push_back(cu);
            indegree[cu]++;
        }
    }

    // prepare DP array
    vector<vector<int>> cnt(compCount, vector<int>(M+1, 0));

    // DP on comp forest
    function<void(int)> dfsDP = [&](int u) {
        // process children
        for (int v : compAdj[u]) {
            dfsDP(v);
        }
        // initialize cnt[u][i] = 1
        for (int i = 1; i <= M; i++) {
            cnt[u][i] = 1;
        }
        cnt[u][0] = 0;
        // multiply by children contributions
        for (int v : compAdj[u]) {
            for (int i = 1; i <= M; i++) {
                cnt[u][i] = mulmod(cnt[u][i], cnt[v][i]);
            }
        }
        // prefix sum
        for (int i = 1; i <= M; i++) {
            cnt[u][i] = addmod(cnt[u][i-1], cnt[u][i]);
        }
    };

    ll answer = 1;
    for (int c = 0; c < compCount; c++) {
        if (indegree[c] == 0) {
            dfsDP(c);
            answer = (answer * cnt[c][M]) % MOD;
        }
    }

    cout << answer << "\n";
    return 0;
}