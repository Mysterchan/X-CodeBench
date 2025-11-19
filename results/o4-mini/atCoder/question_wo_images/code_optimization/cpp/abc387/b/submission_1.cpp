#include <iostream>
using namespace std;

int main() {
    int X;
    cin >> X;
    // Total sum of 1*1 + 1*2 + ... + 9*9 = (1+2+...+9)^2 = 45*45 = 2025
    const int TOTAL_SUM = 2025;
    int count_eq = 0;
    // Count how many (i, j) pairs in [1..9]x[1..9] satisfy i*j == X
    for (int i = 1; i <= 9; ++i) {
        if (X % i == 0) {
            int j = X / i;
            if (1 <= j && j <= 9) {
                ++count_eq;
            }
        }
    }
    int result = TOTAL_SUM - X * count_eq;
    cout << result << "\n";
    return 0;
}