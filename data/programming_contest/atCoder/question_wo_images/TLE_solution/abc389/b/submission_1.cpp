#include <iostream>
using namespace std;

int main() {
    int x;
    cin >> x;

    long long kaijo = 1;
    for (int i = 1; ; i++) {
        kaijo = kaijo * i;
            if (kaijo == x) {
                cout << i << endl;
                return 0;
            }
    }

}