#include<bits/stdc++.h>
using namespace std;
#define int long long

int n;
int a[20];
set<int> s;

void dfs(int mask, vector<int>& groups) {
    if(mask == (1 << n) - 1) {
        int res = 0;
        for(int g : groups) {
            res ^= g;
        }
        s.insert(res);
        return;
    }
    
    int next_bag = __builtin_ctzll(~mask & ((1LL << n) - 1));
    
    // Add to existing group
    for(int i = 0; i < groups.size(); i++) {
        groups[i] += a[next_bag];
        dfs(mask | (1 << next_bag), groups);
        groups[i] -= a[next_bag];
    }
    
    // Create new group
    groups.push_back(a[next_bag]);
    dfs(mask | (1 << next_bag), groups);
    groups.pop_back();
}

void solve() {
    cin >> n;
    for(int i = 0; i < n; i++) cin >> a[i];
    
    vector<int> groups;
    dfs(0, groups);
    
    cout << s.size() << '\n';
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    solve();
}