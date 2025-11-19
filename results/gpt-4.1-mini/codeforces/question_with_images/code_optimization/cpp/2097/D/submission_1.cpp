#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        string s, u;
        cin >> s >> u;

        // If n is odd, strings must be equal to be transformable
        if (n & 1) {
            cout << (s == u ? "YES\n" : "NO\n");
            continue;
        }

        // Count ones in s and u
        int cnt_s = 0, cnt_u = 0;
        for (char c : s) cnt_s += (c == '1');
        for (char c : u) cnt_u += (c == '1');

        // If both strings are all zeros, they are transformable only if equal
        if (cnt_s == 0 && cnt_u == 0) {
            cout << (s == u ? "YES\n" : "NO\n");
            continue;
        }

        // If one is all zeros and the other is not, impossible
        if ((cnt_s == 0) != (cnt_u == 0)) {
            cout << "NO\n";
            continue;
        }

        // Otherwise, the strings are transformable if and only if
        // the parity of the number of ones in s and u is the same
        // and the length is a power of two or can be split recursively.
        // But the problem reduces to checking if the multisets of substrings
        // after recursive splitting are equal.
        // This is equivalent to checking if s and u are equal after sorting
        // their halves recursively.

        // Implement a function to get the canonical form of a string:
        // recursively split into halves, get canonical forms of halves,
        // then return the lex smaller of (left+right) and (right+left).

        function<string(const string&)> canonical = [&](const string &str) -> string {
            int len = (int)str.size();
            if (len & 1) return str;
            string left = canonical(str.substr(0, len / 2));
            string right = canonical(str.substr(len / 2));
            if (left < right) return left + right;
            else return right + left;
        };

        cout << (canonical(s) == canonical(u) ? "YES\n" : "NO\n");
    }

    return 0;
}