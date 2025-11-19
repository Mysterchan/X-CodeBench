#include <iostream>
using namespace std;

int main() {
    long long x;
    cin >> x;
    
    for (int i = 1; i <= 20; i++) {
        x /= i;
        if (x == 1) {
            cout << i << endl;
            return 0;
        }
    }
    
    return 0;
}