#include <iostream>
#include <string>
using namespace std;

int main() {
    string S;
    cin >> S;
    for (char c : S) {
        if (c == '2') cout << c;
    }
    cout << '\n';
    return 0;
}