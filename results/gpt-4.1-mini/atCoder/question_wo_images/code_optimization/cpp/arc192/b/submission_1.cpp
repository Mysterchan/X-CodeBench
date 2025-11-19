#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll n;
    cin >> n;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];

    // The game ends when all indices are in S.
    // Each index i must be chosen at least once to add i to S.
    // The minimal number of moves is n (one per index).
    // After that, the remaining moves are sum(A_i) - n.
    // Players alternate moves starting with Fennec.
    // The winner is the player who makes the last move.
    // So total moves = sum(A_i).
    // If sum(A_i) is odd, Fennec wins; else Snuke wins.

    ll sumA = 0;
    for (auto x : a) sumA += x;

    if (sumA % 2 == 1)
        cout << "Fennec\n";
    else
        cout << "Snuke\n";

    return 0;
}