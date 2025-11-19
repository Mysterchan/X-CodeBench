#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cassert>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <random>
#include <iomanip>
#include <numeric>
#include <fstream>
#include <cstdint>
#include <bitset>
using namespace std;
#define ll long long
#define ull unsigned ll
#define ld long double
#define clf(i, from, to) for (ll i = from; i < to; ++i)
#define all(v) v.begin(), v.end()

mt19937 rnd(time(0));

ll rd() {
    ll x;
    cin >> x;
    assert(cin);
    return x;
}

void print(vector<ll>& a) {
    for (ll& x : a) {
        cout << x << ' ';
    }
    cout << '\n';
}

void solve() {
    ll q = rd();
    set<pair<ll, pair<ll, ll>>> free;
    set<pair<ll, pair<ll, ll>>> taken;
    clf(i, 0, 230) {
        clf(j, 0, 230) {
            clf(a, 1, 3) {
                clf(b, 1, 3) {
                    ll x = i * 3 + a;
                    ll y = j * 3 + b;
                    ll add = (a == 2 && b == 2) ? 2 : 0;
                    free.insert({ x + y + add, {x, y} });
                }
            }
        }
    }
    clf(i, 0, q) {
        ll flag = rd();
        if (!flag || taken.empty() || (*taken.begin()) > (*free.begin())) {
            auto [dist, coord] = *free.begin();
            auto [x, y] = coord;
            ll x1 = x / 3 * 3;
            ll y1 = y / 3 * 3;
            clf(a, 1, 3) {
                clf(b, 1, 3) {
                    free.erase({ x1 + a + y1 + b + ((a == 2 && b == 2) ? 2 : 0), {x1 + a, y1 + b} });
                    taken.insert({ x1 + a + y1 + b + ((a == 2 && b == 2) ? 2 : 0), {x1 + a, y1 + b} });
                }
            }
            taken.erase({ dist, coord });
            cout << x << ' ' << y << '\n';
        }
        else {
            auto [dist, coord] = *taken.begin();
            auto [x, y] = coord;
            taken.erase(taken.begin());
            cout << x << ' ' << y << '\n';
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
    ll t = rd(); while (t--) solve();
}