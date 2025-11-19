#include <bits/stdc++.h>
using namespace std;

int main() {
    int X;
    cin >> X;
    int result = 2025;

    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (i * j == X) {
                result -= X;
            }
        }
    }
    cout << result << endl;
}