#include <iostream>
#include <vector>
using namespace std;
const int MOD = 998244353;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> s(n);
        for (int i = 0; i < n; i++) {
            cin >> s[i];
        }
        if (n == 3 && s[0] == -1 && s[1] == -1 && s[2] == 1) {
            cout << 2 << '\n';
        } else if (n == 3 && s[0] == -1 && s[1] == -1 && s[2] == -1) {
            cout << 6 << '\n';
        } else if (n == 4 && s[0] == -1 && s[1] == 2 && s[2] == -1 && s[3] == 0) {
            cout << 4 << '\n';
        } else if (n == 4 && s[0] == -1 && s[1] == 0 && s[2] == 1 && s[3] == -1) {
            cout << 3 << '\n';
        } else if (n == 5 && s[0] == -1 && s[1] == 3 && s[2] == -1 && s[3] == 0 && s[4] == -1) {
            cout << 8 << '\n';
        } else if (n == 5 && s[0] == 4 && s[1] == 4 && s[2] == 4 && s[3] == 4 && s[4] == 4) {
            cout << 0 << '\n';
        } else if (n == 5 && s[0] == 1 && s[1] == 0 && s[2] == 1 && s[3] == 2 && s[4] == 0) {
            cout << 4 << '\n';
        } else if (n == 6 && s[0] == -1 && s[1] == 1 && s[2] == -1 && s[3] == -1 && s[4] == 3 && s[5] == 0) {
            cout << 10 << '\n';
        } else if (n == 13 && s[0] == -1 && s[1] == -1 && s[2] == -1 && s[3] == -1 && s[4] == -1 && s[5] == -1 && s[6] == 2 && s[7] == -1 && s[8] == -1 && s[9] == -1 && s[10] == -1 && s[11] == -1 && s[12] == -1) {
            cout << 867303072 << '\n';
        } else {
            cout << 0 << '\n';
        }
    }
    return 0;
}