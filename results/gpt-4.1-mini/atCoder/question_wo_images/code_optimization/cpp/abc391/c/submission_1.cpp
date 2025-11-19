#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;

    vector<int> pigeons(n + 1);
    vector<int> count(n + 1, 1);
    for (int i = 1; i <= n; i++) {
        pigeons[i] = i;
    }

    int doubleCount = 0;

    for (int _ = 0; _ < q; _++) {
        int t;
        cin >> t;
        if (t == 1) {
            int p, h;
            cin >> p >> h;

            int oldNest = pigeons[p];
            // Decrement count of old nest
            if (count[oldNest] == 2) doubleCount--;
            count[oldNest]--;

            // Move pigeon p to new nest h
            pigeons[p] = h;

            // Increment count of new nest
            if (count[h] == 1) doubleCount++;
            count[h]++;
        } else {
            cout << doubleCount << "\n";
        }
    }

    return 0;
}