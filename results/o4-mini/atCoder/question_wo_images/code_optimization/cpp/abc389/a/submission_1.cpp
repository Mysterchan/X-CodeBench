#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;
    int a = s[0] - '0';
    int b = s[2] - '0';
    cout << a * b;
    return 0;
}