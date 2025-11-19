#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        string s, t;
        cin >> s >> t;
        
        // Count the number of 1's in both strings
        int count_s = count(s.begin(), s.end(), '1');
        int count_t = count(t.begin(), t.end(), '1');

        // Check if they can be made equal
        cout << (count_s % 2 == count_t % 2 && (count_s > 0 || count_t == 0) ? "Yes" : "No") << "\n";
    }
    
    return 0;
}