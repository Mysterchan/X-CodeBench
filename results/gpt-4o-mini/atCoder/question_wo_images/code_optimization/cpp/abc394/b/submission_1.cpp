#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<string> s(n);
    
    for (int i = 0; i < n; i++) {
        cin >> s[i];
    }

    // Sort the strings based on their lengths
    sort(s.begin(), s.end(), [](const string &a, const string &b) {
        return a.length() < b.length();
    });
    
    // Concatenate sorted strings and output the result
    for (const string &str : s) {
        cout << str;
    }
}

int main() {
    solve();
    return 0;
}