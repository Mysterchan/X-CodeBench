#include <iostream>
using namespace std;

int main() {
    unsigned long long X;
    cin >> X;

    unsigned long long factorial = 1;
    int i = 1;
    while (factorial < X) {
        i++;
        factorial *= i;
    }
    cout << i << "\n";
    return 0;
}