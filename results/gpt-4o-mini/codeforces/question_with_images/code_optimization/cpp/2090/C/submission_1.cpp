#include <iostream>
#include <vector>
#include <set>

using namespace std;

#define ll long long

void solve() {
    ll q;
    cin >> q;
    
    for (ll i = 0; i < q; i++) {
        ll n;
        cin >> n;
        vector<ll> guests(n);
        for (ll j = 0; j < n; j++) {
            cin >> guests[j];
        }

        set<pair<ll, ll>> free, taken;
        for (ll x = 0; x < 200; x++) {
            for (ll y = 0; y < 200; y++) {
                free.insert({3 * x + 1, 3 * y + 1});
                free.insert({3 * x + 1, 3 * y + 2});
                free.insert({3 * x + 2, 3 * y + 1});
                free.insert({3 * x + 2, 3 * y + 2});
            }
        }

        for (ll j = 0; j < n; j++) {
            if (guests[j] == 0) {
                auto it = free.begin();
                ll x = it->first, y = it->second;
                cout << x << ' ' << y << '\n';
                taken.insert({x, y});
                free.erase(it);
                if (x % 3 == 1 && y % 3 == 1) free.erase({x, y + 1}), free.erase({x + 1, y}), free.erase({x + 1, y + 1});
                else if (x % 3 == 1 && y % 3 == 2) free.erase({x, y - 1}), free.erase({x + 1, y}), free.erase({x + 1, y - 1});
                else if (x % 3 == 2 && y % 3 == 1) free.erase({x - 1, y}), free.erase({x, y + 1}), free.erase({x - 1, y + 1});
                else if (x % 3 == 2 && y % 3 == 2) free.erase({x - 1, y}), free.erase({x, y - 1}), free.erase({x - 1, y - 1});
            } else {
                auto it = taken.begin();
                ll x = it->first, y = it->second;
                cout << x << ' ' << y << '\n';
                taken.erase(it);
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    solve();
    return 0;
}