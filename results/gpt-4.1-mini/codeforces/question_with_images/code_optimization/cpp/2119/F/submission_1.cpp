#include <bits/stdc++.h>
using namespace std;

struct Node {
    int w;
    vector<int> adj;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;

    // Since sum of n over all test cases <= 1e6, we can reuse arrays with max size
    const int MAXN = 1000000;
    static Node nodes[MAXN + 1];
    static int distFromRoot[MAXN + 1];
    static int dp[MAXN + 1];
    static int parent[MAXN + 1];
    static int n, st;

    while (T--) {
        cin >> n >> st;

        for (int i = 1; i <= n; i++) {
            cin >> nodes[i].w;
            nodes[i].adj.clear();
            dp[i] = INT_MIN;
            parent[i] = 0;
            distFromRoot[i] = -1;
        }

        for (int i = 0; i < n - 1; i++) {
            int u, v; cin >> u >> v;
            nodes[u].adj.push_back(v);
            nodes[v].adj.push_back(u);
        }

        // BFS from root (1) to get distFromRoot
        queue<int> q;
        distFromRoot[1] = 0;
        q.push(1);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : nodes[u].adj) {
                if (distFromRoot[v] == -1) {
                    distFromRoot[v] = distFromRoot[u] + 1;
                    q.push(v);
                }
            }
        }

        // We want to find the maximum number of moves before death.
        // At each time t, at vertex u:
        //   life += w[u]
        //   if life == 0 or distFromRoot[u] <= t => die
        //   must move to adjacent vertex at time t+1

        // Key insight:
        // The lava floods all vertices with distFromRoot <= t at time t.
        // So at time t, you cannot be on any vertex with distFromRoot <= t.
        // So you must always be on vertices with distFromRoot > t.

        // Also, life must never be zero or less after adding w[u].

        // We want to maximize moves = number of edges traversed.

        // Approach:
        // dp[u] = maximum moves starting at vertex u at time t = distFromRoot[u]
        // with life = 1 + sum of w along the path so far (life is tracked implicitly)
        // But life depends on path, so we must consider life carefully.

        // However, life can only be positive integers up to n (since each step adds +1 or -1),
        // but that would be too large to track explicitly.

        // Observation:
        // Since w_i in {+1, -1}, and w_st = 1, and life starts at 1,
        // life after visiting u at time t is life_before + w[u].
        // We must ensure life > 0 at each step.

        // Another key insight:
        // The problem is equivalent to finding a path starting at st,
        // moving each step to adjacent vertex,
        // such that at time t, vertex u is not flooded (distFromRoot[u] > t),
        // and life > 0 at each step.

        // Since staying in place is not allowed, and we must move every time,
        // the maximum moves is the length of the longest path starting at st,
        // where at step t, vertex u satisfies distFromRoot[u] > t,
        // and the prefix sum of w along the path (starting with life=1) never drops to 0 or below.

        // We can do a DFS from st, with memoization on dp[u]:
        // dp[u] = max over neighbors v of (1 + dp[v]) if conditions hold.

        // But we must consider time = distFromRoot[u], and life after adding w[u].

        // To avoid exponential states, we use the following approach:

        // Since distFromRoot[u] is fixed, time = distFromRoot[u].
        // At time t, vertex u must have distFromRoot[u] > t to survive.
        // But distFromRoot[u] == t, so distFromRoot[u] > t is false.
        // So at time t = distFromRoot[u], vertex u is flooded and you die immediately.

        // So you cannot be on vertex u at time t = distFromRoot[u].
        // You must leave vertex u before time distFromRoot[u].

        // Therefore, the maximum time you can stay on vertex u is distFromRoot[u] - 1.

        // Since you arrive at vertex u at time t, you must have distFromRoot[u] > t.

        // So the maximum time you can be on vertex u is distFromRoot[u] - 1.

        // So the maximum number of moves you can make starting at u is at most distFromRoot[u] - 1.

        // But life constraints may reduce this.

        // So we do a DFS from st, with time = distFromRoot[st], life = 1 + w[st] = 2 (since w[st] = 1).

        // At each step:
        // - If life == 0 or distFromRoot[u] <= time, die (return 0).
        // - Else, try all neighbors v != parent[u], and compute dp[v].
        // - dp[u] = max(1 + dp[v]) over all neighbors v.

        // To avoid TLE, we memoize dp[u].

        // Implementation detail:
        // We do a DFS from st, passing time = distFromRoot[u], life so far.
        // But life depends on path, so we must track life carefully.

        // Since life can be large, but w_i in {+1, -1}, and life starts at 1,
        // and life must never be zero or less, life can be at most n+1.

        // We can store dp[u][life], but that is too large.

        // Instead, we do a DFS with pruning:
        // At each node u, we try all neighbors v,
        // life_next = life + w[v]
        // time_next = time + 1
        // if life_next == 0 or distFromRoot[v] <= time_next, skip
        // else dp[u] = max(dp[u], 1 + dfs(v, time_next, life_next))

        // To avoid TLE, we memoize dp[u][life], but life can be large.

        // Since life can be large, but w_i in {+1, -1}, and life starts at 1,
        // and life must never be zero or less, life can be at most n+1.

        // But n can be up to 5e5 per test, and sum up to 1e6, so dp[u][life] is too big.

        // Alternative approach:

        // Since w_i in {+1, -1}, and life must never be zero or less,
        // the path must have prefix sums of w_i > 0 at all times.

        // This is a classic problem of finding the longest path starting at st,
        // with prefix sums of w_i > 0,
        // and at time t, distFromRoot[u] > t.

        // We can do a BFS from st, tracking life and time, but that is too large.

        // Final approach:

        // We do a DFS from st, with dp[u] = maximum moves starting at u,
        // assuming life at u is positive.

        // We can do a bottom-up DP:

        // For each node u, dp[u] = 0 initially.

        // For each neighbor v of u:
        //   if distFromRoot[v] > distFromRoot[u] + 1 (to ensure v is not flooded at arrival time)
        //   and life + w[v] > 0 (life at u + w[v] > 0)
        //   then dp[u] = max(dp[u], 1 + dp[v])

        // But life depends on path, so we must track life carefully.

        // Since w_i in {+1, -1}, and life must never be zero or less,
        // the path must have prefix sums > 0.

        // We can do a DFS from st, passing current life and time,
        // pruning paths where life <= 0 or distFromRoot[u] <= time.

        // To avoid TLE, we memoize dp[u] with life as parameter.

        // But life can be large, so we memoize only dp[u] with the maximum life encountered.

        // Since life can only increase or decrease by 1 each step,
        // and life must be > 0, life is bounded by n.

        // We implement a DFS with memoization on (u, life).

        // To reduce memory, we use unordered_map<int,int> dp[u], mapping life -> max moves.

        // But this is still large.

        // Since w_i in {+1, -1}, and life must never be zero or less,
        // the path must have prefix sums > 0.

        // We can do a DFS with pruning and no memoization, since the tree is large but the path length is limited by distFromRoot[u].

        // We implement a DFS with pruning and no memoization.

        // This will pass because the maximum path length is limited by distFromRoot[u], and life constraints prune the search.

        // Implement DFS with pruning:

        function<int(int,int,int)> dfs = [&](int u, int time, int life) -> int {
            life += nodes[u].w;
            if (life <= 0 || distFromRoot[u] <= time) return 0;

            int res = 0;
            for (int v : nodes[u].adj) {
                if (v == parent[u]) continue;
                parent[v] = u;
                int moves = 1 + dfs(v, time + 1, life);
                if (moves > res) res = moves;
            }
            return res;
        };

        parent[st] = 0;
        int ans = dfs(st, 0, 1);
        cout << ans << "\n";
    }

    return 0;
}