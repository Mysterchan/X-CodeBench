#include<bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    int n;
    cin >> n;
    vector<int> a(n + 1);
    vector<int> pos(n + 1);
    
    for(int i = 1; i <= n; i++) {
        cin >> a[i];
        pos[a[i]] = i;
    }
    
    long long res = 0;
    
    for(int i = 1; i <= n; i++) {
        int cur_pos = pos[i];
        if(cur_pos == i) continue;
        
        // Move element i from cur_pos to position i
        // Cost is sum from i to cur_pos-1
        long long cost = (long long)(cur_pos - 1 + i) * (cur_pos - i) / 2;
        res += cost;
        
        // Update positions of elements between i and cur_pos
        for(int j = cur_pos; j > i; j--) {
            a[j] = a[j - 1];
            pos[a[j]] = j;
        }
        a[i] = i;
        pos[i] = i;
    }
    
    cout << res << '\n';
    
    return 0;
}