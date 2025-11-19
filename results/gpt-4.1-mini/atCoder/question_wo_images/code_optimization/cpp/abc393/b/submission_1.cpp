#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;
    int n = s.size();
    int counter = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] != 'A') continue;
        for (int d = 1; i + 2 * d < n; d++) {
            int j = i + d;
            int k = i + 2 * d;
            if (s[j] == 'B' && s[k] == 'C') {
                counter++;
            }
        }
    }
    cout << counter;
    return 0;
}