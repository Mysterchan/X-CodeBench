#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; 
    cin >> n;
    vector<int> a(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];

    // Count how many aliens have at least one stone at the start
    int adults_with_stones = 0;
    for (int i = 1; i <= n; i++) {
        if (a[i] > 0) adults_with_stones++;
    }

    // Result array
    vector<int> res(n + 1);

    // For each alien i:
    // They become adult at year i.
    // At that moment, all adults who have at least one stone (except i itself) give one stone to i.
    // So alien i receives (adults_with_stones - (a[i] > 0 ? 1 : 0)) stones.
    // Each alien who had stones loses one stone for each alien that becomes adult after them.
    // Number of aliens becoming adult after i is (n - i).
    // But only those who had stones at the start lose stones.
    // Actually, each alien with stones loses one stone for each alien that becomes adult after them.
    // So total stones lost by alien i = (a[i] > 0 ? (n - i) : 0)

    for (int i = 1; i <= n; i++) {
        int lost = (a[i] > 0) ? (n - i) : 0;
        int gained = adults_with_stones - (a[i] > 0 ? 1 : 0);
        res[i] = a[i] - lost + gained;
        if (res[i] < 0) res[i] = 0; // stones can't be negative
    }

    for (int i = 1; i <= n; i++) {
        cout << res[i] << (i == n ? '\n' : ' ');
    }

    return 0;
}