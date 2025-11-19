#include <iostream>
#include <vector>
#include <algorithm>
#define rep(i,n) for(int i=0;i<(n);i++)
using namespace std;

int N;
vector<vector<int>> G;
vector<vector<int>> memo;

int dfs(int n, int p) {
    if (memo[n][p] != -2) return memo[n][p];
    
    vector<int> child_vals;
    child_vals.reserve(G[n].size());
    
    for (int x : G[n]) {
        if (x == p) continue;
        int val = dfs(x, n);
        if (val > 0) child_vals.push_back(val);
    }
    
    int sz = child_vals.size();
    
    if (p == N) {
        // n is the root
        if (sz < 4) {
            memo[n][p] = -1;
        } else {
            nth_element(child_vals.begin(), child_vals.begin() + 3, child_vals.end(), greater<int>());
            memo[n][p] = 1 + child_vals[0] + child_vals[1] + child_vals[2] + child_vals[3];
        }
    } else {
        // n is not the root
        if (sz < 3) {
            memo[n][p] = 1;
        } else {
            nth_element(child_vals.begin(), child_vals.begin() + 2, child_vals.end(), greater<int>());
            memo[n][p] = 1 + child_vals[0] + child_vals[1] + child_vals[2];
        }
    }
    
    return memo[n][p];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> N;
    G.resize(N);
    memo.assign(N, vector<int>(N + 1, -2));
    
    rep(i, N - 1) {
        int a, b;
        cin >> a >> b;
        a--; b--;
        G[a].push_back(b);
        G[b].push_back(a);
    }
    
    int ans = -1;
    rep(i, N) {
        int val = dfs(i, N);
        if (val > ans) ans = val;
    }
    
    cout << ans << endl;
    return 0;
}