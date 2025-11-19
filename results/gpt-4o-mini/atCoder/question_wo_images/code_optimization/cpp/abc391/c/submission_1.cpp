#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
    ll n, q;
    cin >> n >> q;

    vector<ll> nests(n + 1, 0); // Number of pigeons in each nest
    ll doubleCount = 0; // Count of nests with more than one pigeon

    for (ll i = 1; i <= n; i++) {
        nests[i] = 1; // Initially, each nest has one pigeon
    }

    for (ll i = 0; i < q; i++) {
        char c;
        cin >> c;
        if (c == '1') {
            ll p, h;
            cin >> p >> h;

            // Move pigeon from its current nest to the new nest
            ll currentNest = p;  // Each pigeon starts in its respective nest
            nests[currentNest]--; // Remove a pigeon from the current nest
            nests[h]++;           // Add a pigeon to the new nest

            // Update double count when moving:
            if (nests[currentNest] == 1) doubleCount--; // Only one pigeon was in the current nest
            if (nests[currentNest] == 0) doubleCount++; // Current nest now has zero pigeons
            
            if (nests[h] == 2) doubleCount++;           // Nest h now has two pigeons
            if (nests[h] == 1) doubleCount--;           // Nest h was empty before the move
            
        } else {
            cout << doubleCount << endl; // Output the current count of nests with more than one pigeon
        }
    }
    return 0;
}