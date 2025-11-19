#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll MOD = 998244353;

int add(int a, int b) { a += b; if (a >= MOD) a -= MOD; return a; }
int mul(ll a, ll b) { return int((a * b) % MOD); }
ll modpow(ll a, ll e = MOD-2) {
    ll r = 1;
    while (e) {
        if (e & 1) r = (r * a) % MOD;
        a = (a * a) % MOD;
        e >>= 1;
    }
    return r;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    string s;
    cin >> n >> s;
    // Build tree with virtual root 0
    int total_nodes = 0;
    vector<vector<int>> children(n/2 + 5);
    vector<int> stk;
    stk.reserve(n/2 + 5);
    for (int i = 0; i < n; i++) {
        if (s[i] == '(') {
            total_nodes++;
            int cur = total_nodes;
            if (stk.empty()) {
                children[0].push_back(cur);
            } else {
                children[stk.back()].push_back(cur);
            }
            stk.push_back(cur);
        } else {
            // ')'
            if (!stk.empty()) stk.pop_back();
        }
    }
    int N = total_nodes + 1; // including 0

    // Precompute factorials and inv factorials up to n
    int maxF = n;
    vector<int> fact(maxF+1), invfact(maxF+1);
    fact[0] = 1;
    for (int i = 1; i <= maxF; i++) fact[i] = mul(fact[i-1], i);
    invfact[maxF] = (int)modpow(fact[maxF]);
    for (int i = maxF; i > 0; i--) invfact[i-1] = mul(invfact[i], i);

    // Prepare for canonical labeling
    vector<int> id(N, 0);
    vector<vector<int>> sorted_child_ids(N);
    map<vector<int>, int> id_map;
    int next_id = 1;
    // assign id for empty vector = 1
    id_map[vector<int>()] = next_id++;
    // DFS post-order to assign ids
    function<void(int)> dfs = [&](int v) {
        for (int u : children[v]) {
            dfs(u);
        }
        // gather child ids
        vector<int> cv;
        cv.reserve(children[v].size());
        for (int u : children[v]) {
            cv.push_back(id[u]);
        }
        sort(cv.begin(), cv.end());
        sorted_child_ids[v] = cv;
        auto it = id_map.find(cv);
        if (it == id_map.end()) {
            id_map[cv] = next_id;
            id[v] = next_id;
            next_id++;
        } else {
            id[v] = it->second;
        }
    };
    dfs(0);

    // Compute answer
    ll ans = 1;
    for (int v = 0; v < N; v++) {
        int c = (int)sorted_child_ids[v].size();
        // multiply by c!
        ans = ans * fact[c] % MOD;
        // divide by factorial of counts of identical
        int i = 0;
        while (i < c) {
            int j = i+1;
            while (j < c && sorted_child_ids[v][j] == sorted_child_ids[v][i]) j++;
            int cnt = j - i;
            ans = ans * invfact[cnt] % MOD;
            i = j;
        }
    }

    cout << ans << "\n";
    return 0;
}