#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

const int MAX_SIDE = 150;
const int MAX_N = 10;

int fib[MAX_N + 1];

void precomputeFibonacci() {
    fib[1] = 1;
    fib[2] = 2;
    for (int i = 3; i <= MAX_N; ++i) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }
}

bool canFit(int n, int w, int l, int h) {
    int maxSize = fib[n];
    if (maxSize > min(w, min(l, h))) return false;
    
    // Get the number of cubes that will be placed
    int totalHeight = 0;
    for (int i = n; i >= 1; --i) {
        if ((i == n || fib[i] == fib[i + 1]) && (fib[i] <= w && fib[i] <= l)) {
            totalHeight += fib[i];
        } else {
            return false;
        }
    }
    return totalHeight <= h;
}

int main() {
    precomputeFibonacci();
    int t;
    cin >> t;

    while (t--) {
        int n, m;
        cin >> n >> m;
        string result;

        for (int i = 0; i < m; ++i) {
            int w, l, h;
            cin >> w >> l >> h;

            if (canFit(n, w, l, h)) {
                result += '1';
            } else {
                result += '0';
            }
        }
        cout << result << '\n';
    }

    return 0;
}