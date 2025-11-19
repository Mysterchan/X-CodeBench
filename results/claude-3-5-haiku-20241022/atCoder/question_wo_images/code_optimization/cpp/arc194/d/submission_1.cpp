#include <bits/stdc++.h>
using namespace std;

#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

const long long mod = 998244353LL;

int n;
string s;
vector<long long> f, inv;

long long exp(long long b, long long e) {
    long long res = 1;
    b %= mod;
    while (e > 0) {
        if (e & 1) res = (res * b) % mod;
        b = (b * b) % mod;
        e >>= 1;
    }
    return res;
}

string normalize(int l, int r) {
    if (l + 1 == r) return "()";
    
    int depth = 0;
    bool single_block = true;
    
    for (int i = l; i < r; i++) {
        depth += (s[i] == '(') ? 1 : -1;
        if (depth == 0 && i < r - 1) {
            single_block = false;
            break;
        }
    }
    
    if (single_block) {
        return "(" + normalize(l + 1, r - 1) + ")";
    }
    
    vector<string> blocks;
    int start = l;
    depth = 0;
    
    for (int i = l; i < r; i++) {
        depth += (s[i] == '(') ? 1 : -1;
        if (depth == 0) {
            blocks.push_back(normalize(start, i + 1));
            start = i + 1;
        }
    }
    
    sort(blocks.begin(), blocks.end());
    
    string result;
    for (const auto& block : blocks) {
        result += block;
    }
    
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> n >> s;
    
    f.resize(n + 1);
    inv.resize(n + 1);
    f[0] = 1;
    inv[0] = 1;
    for (int i = 1; i <= n; i++) {
        f[i] = (f[i - 1] * i) % mod;
        inv[i] = exp(f[i], mod - 2);
    }
    
    vector<vector<int>> children(n + 1);
    vector<int> stack;
    vector<pair<int, int>> ranges(n + 1);
    
    stack.push_back(0);
    ranges[0] = {0, n};
    
    for (int i = 0; i < n; i++) {
        if (s[i] == '(') {
            int parent = stack.back();
            children[parent].push_back(i + 1);
            stack.push_back(i + 1);
            ranges[i + 1].first = i;
        } else {
            stack.pop_back();
        }
    }
    
    for (int i = 1; i <= n; i++) {
        if (ranges[i].first > 0) {
            int depth = 1;
            for (int j = ranges[i].first + 1; j < n; j++) {
                depth += (s[j] == '(') ? 1 : -1;
                if (depth == 0) {
                    ranges[i].second = j + 1;
                    break;
                }
            }
        }
    }
    
    long long ans = 1;
    
    for (int i = 0; i <= n; i++) {
        if (children[i].empty()) continue;
        
        unordered_map<string, int> count;
        
        for (int child : children[i]) {
            string norm = normalize(ranges[child].first, ranges[child].second);
            count[norm]++;
        }
        
        int total = children[i].size();
        ans = (ans * f[total]) % mod;
        
        for (const auto& p : count) {
            ans = (ans * inv[p.second]) % mod;
        }
    }
    
    cout << ans << endl;
    
    return 0;
}