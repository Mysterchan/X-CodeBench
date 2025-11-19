#include<bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    int counter = 0;
    int n = s.size();

    for (int j = 1; j < n - 1; j++) {
        if (s[j] == 'B') {
            for (int d = 1; j - d >= 0 && j + d < n; d++) {
                int i = j - d;
                int k = j + d;

                if (s[i] == 'A' && s[k] == 'C') {
                    counter++;
                }
            }
        }
    }

    cout << counter;
    return 0;
}