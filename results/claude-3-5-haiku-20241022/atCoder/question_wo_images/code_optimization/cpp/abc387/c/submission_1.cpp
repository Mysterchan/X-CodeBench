#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll countSnake(ll n) {
    if (n < 10) return 0;
    
    string s = to_string(n);
    int len = s.size();
    ll count = 0;
    
    // Count all snake numbers with fewer digits
    for (int d = 2; d < len; d++) {
        for (int top = 1; top <= 9; top++) {
            ll ways = 1;
            for (int pos = 1; pos < d; pos++) {
                ways *= top;
            }
            count += ways;
        }
    }
    
    // Count snake numbers with same number of digits up to n
    for (int top = 1; top < s[0] - '0'; top++) {
        ll ways = 1;
        for (int pos = 1; pos < len; pos++) {
            ways *= top;
        }
        count += ways;
    }
    
    // Count snake numbers starting with s[0]
    int topDigit = s[0] - '0';
    function<ll(int, bool)> solve = [&](int pos, bool tight) -> ll {
        if (pos == len) return 1;
        
        ll res = 0;
        int limit = tight ? (s[pos] - '0') : (topDigit - 1);
        
        for (int d = 0; d <= limit; d++) {
            if (tight && d == s[pos] - '0') {
                res += solve(pos + 1, true);
            } else if (d < topDigit) {
                ll rem = len - pos - 1;
                ll ways = 1;
                for (int i = 0; i < rem; i++) {
                    ways *= topDigit;
                }
                res += ways;
            }
        }
        return res;
    };
    
    count += solve(1, true);
    
    return count;
}

int main(void){
    ll l, r;
    cin >> l >> r;
    
    ll result = countSnake(r) - countSnake(l - 1);
    
    cout << result << endl;
    return 0;
}