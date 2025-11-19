#include<bits/stdc++.h>
using namespace std;
#define endl "\n"
typedef long long ll;

ll n;
string s;
vector<string> levels;
map<pair<ll,ll>, ll> memo;

ll solve(ll level, ll pos) {
    if (level == n + 1) {
        return 1;
    }
    
    pair<ll,ll> state = {level, pos};
    if (memo.count(state)) {
        return memo[state];
    }
    
    ll base = pos * 3;
    ll cnt0 = 0, cnt1 = 0;
    
    for (ll i = 0; i < 3; i++) {
        if (levels[level + 1][base + i] == '0') cnt0++;
        else cnt1++;
    }
    
    char current = levels[level][pos];
    char target = (current == '0') ? '1' : '0';
    
    ll ans = LLONG_MAX;
    
    if (target == '1') {
        if (cnt1 < cnt0) {
            if (cnt0 == 3) {
                for (ll i = 0; i < 3; i++) {
                    for (ll j = i + 1; j < 3; j++) {
                        ans = min(ans, solve(level + 1, base + i) + solve(level + 1, base + j));
                    }
                }
            } else {
                for (ll i = 0; i < 3; i++) {
                    if (levels[level + 1][base + i] == '0') {
                        ans = min(ans, solve(level + 1, base + i));
                    }
                }
            }
        }
    } else {
        if (cnt1 > cnt0) {
            if (cnt1 == 3) {
                for (ll i = 0; i < 3; i++) {
                    for (ll j = i + 1; j < 3; j++) {
                        ans = min(ans, solve(level + 1, base + i) + solve(level + 1, base + j));
                    }
                }
            } else {
                for (ll i = 0; i < 3; i++) {
                    if (levels[level + 1][base + i] == '1') {
                        ans = min(ans, solve(level + 1, base + i));
                    }
                }
            }
        }
    }
    
    memo[state] = (ans == LLONG_MAX) ? 0 : ans;
    return memo[state];
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> n >> s;
    
    levels.resize(n + 2);
    levels[n + 1] = s;
    
    for (ll i = n + 1; i >= 2; i--) {
        for (ll j = 0; j < levels[i].size(); j += 3) {
            ll cnt0 = (levels[i][j] == '0') + (levels[i][j+1] == '0') + (levels[i][j+2] == '0');
            ll cnt1 = 3 - cnt0;
            levels[i-1].push_back(cnt0 > cnt1 ? '0' : '1');
        }
    }
    
    cout << solve(1, 0) << endl;
    
    return 0;
}