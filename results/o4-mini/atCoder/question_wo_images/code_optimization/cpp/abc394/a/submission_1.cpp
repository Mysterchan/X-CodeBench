#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string S;
    cin >> S;

    string result;
    result.reserve(S.size());
    for (char c : S) {
        if (c == '2') {
            result.push_back(c);
        }
    }

    cout << result;
    return 0;
}