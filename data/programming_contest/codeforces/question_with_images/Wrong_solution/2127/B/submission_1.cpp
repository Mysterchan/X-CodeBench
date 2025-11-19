#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll t;
    cin >> t;
    while (t--) {
        ll n, x; 
        cin >> n >> x;
        string s; 
        cin >> s;

        ll left = 0;
        for(int i = 0; i < x - 1; i++) {
            if(s[i] == '#') left++;
        }

        ll right = 0;
        for(int i = x; i < n; i++) {
            if(s[i] == '#') right++;
        }

        cout << min(left, right) + 1 << '\n';
    }
}