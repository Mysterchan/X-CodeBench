#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

void solve(){
    int n, m;
    cin >> n >> m;
    string s, t;
    cin >> s >> t;
    
    // Sort T in descending order to get largest values first
    sort(t.begin(), t.end(), greater<char>());
    
    int idx = 0;
    // Greedily replace from left to right if T[idx] > S[i]
    for(int i = 0; i < n && idx < m; i++) {
        if(t[idx] > s[i]) {
            s[i] = t[idx];
            idx++;
        }
    }
    
    // If we still have unused characters, place the largest at the last position
    while(idx < m) {
        s[n-1] = max(s[n-1], t[idx]);
        idx++;
    }
    
    cout << s << "\n";
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    solve();
    
    return 0;
}