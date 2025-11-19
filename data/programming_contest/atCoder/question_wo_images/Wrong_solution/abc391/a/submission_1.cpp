#include <bits/stdc++.h>
using namespace std;

int main() {
    string D;
    cin >> D;
    string ans = "";
    for (char d : D) {
        if (d == 'N') {
        } else if (d == 'S') {
            ans += 'N';
        } else if (d == 'E') {
            ans += 'W';
        } else if (d == 'W') {
            ans += 'E';
        }
    }
    cout << ans << endl;
}
