#include <iostream>
using namespace std;

int main() {
    long long x;
    cin >> x;

    long long fact = 1;
    int n = 1;

    while (fact < x) {
        n++;
        fact *= n;
    }

    cout << n << endl;
    return 0;
}