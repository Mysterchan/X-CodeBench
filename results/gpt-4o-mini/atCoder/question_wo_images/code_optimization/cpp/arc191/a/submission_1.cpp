#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

void solve() {
    int n, m;
    cin >> n >> m;
    string s, t;
    cin >> s >> t;

    // Sort T in descending order to easily access the largest available digits
    sort(t.rbegin(), t.rend());

    int j = 0; // Index for T
    for (int i = 0; i < n; i++) {
        // Check if we still have characters left in T and if the current character in T is greater than the character in S
        if (j < m && t[j] > s[i]) {
            s[i] = t[j]; // Replace S[i] with the character from T
            j++; // Move to the next character in T
        }
    }

    cout << s; // Output the modified string S
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    solve();
    return 0;
}
