#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        string s; cin >> s;

        // If there is no empty pot, answer is YES trivially
        if (s.find('0') == string::npos) {
            cout << "YES\n";
            continue;
        }

        // If all pots are empty, answer is YES
        if (s.find('1') == string::npos) {
            cout << "YES\n";
            continue;
        }

        // Check for any adjacent empty pots "00"
        // If found, answer is YES
        if (s.find("00") != string::npos) {
            cout << "YES\n";
            continue;
        }

        // Otherwise, answer is NO
        cout << "NO\n";
    }
    return 0;
}