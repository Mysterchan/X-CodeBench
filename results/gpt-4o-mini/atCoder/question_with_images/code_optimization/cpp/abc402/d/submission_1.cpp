#include <bits/stdc++.h>
#define ll long long
using namespace std;

const ll MAX_M = 300000;

ll n, m, ans;
pair<ll, ll> lines[MAX_M];

bool doIntersect(pair<ll, ll>& a, pair<ll, ll>& b) {
    ll x1 = a.first, x2 = a.second;
    ll y1 = b.first, y2 = b.second;
    
    return (x1 < y1 && x2 > y2) || (y1 < x1 && y2 > x2);
}

int main() {
    scanf("%lld%lld", &n, &m);
    
    for (ll i = 0; i < m; i++) {
        scanf("%lld%lld", &lines[i].first, &lines[i].second);
        if (lines[i].first > lines[i].second) {
            swap(lines[i].first, lines[i].second);
        }
    }
    
    sort(lines, lines + m);
    
    ans = 0;
    for (ll i = 0; i < m; i++) {
        for (ll j = i + 1; j < m; j++) {
            if (doIntersect(lines[i], lines[j])) {
                ans++;
            }
        }
    }
    
    printf("%lld\n", ans);
    return 0;
}