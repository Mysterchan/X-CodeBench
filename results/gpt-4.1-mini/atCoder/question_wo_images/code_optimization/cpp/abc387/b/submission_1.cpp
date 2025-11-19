#include <iostream>
using namespace std;

int main() {
    int x;
    cin >> x;

    // Total sum of all products i*j for i,j in [1..9]
    // sum_i=1..9 i = 45
    // sum_j=1..9 j = 45
    // total sum = 45 * 45 = 2025
    int total = 2025;

    // Count how many times x appears in the table
    // For each i in [1..9], if x % i == 0 and x/i in [1..9], then x appears once at (i, x/i)
    int count = 0;
    for (int i = 1; i <= 9; i++) {
        if (x % i == 0) {
            int j = x / i;
            if (j >= 1 && j <= 9) {
                count++;
            }
        }
    }

    // Subtract x * count from total
    cout << total - x * count << "\n";

    return 0;
}