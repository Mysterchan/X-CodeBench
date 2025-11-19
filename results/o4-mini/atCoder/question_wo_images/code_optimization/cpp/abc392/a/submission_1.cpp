#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b, c;
    cin >> a >> b >> c;

    if (a * b == c || a * c == b || b * c == a) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}