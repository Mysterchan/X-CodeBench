#include <iostream>
using namespace std;

int main() {
    unsigned long long X;
    cin >> X;
    unsigned long long n = 1;
    while (X > 1) {
        ++n;
        X /= n;
    }
    cout << n << "\n";
    return 0;
}