#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string D;
    cin >> D;
    for (char &c : D) {
        if (c == 'N')      c = 'S';
        else if (c == 'S') c = 'N';
        else if (c == 'E') c = 'W';
        else if (c == 'W') c = 'E';
    }
    cout << D << '\n';
    return 0;
}