#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string S;
    cin >> S;
    if (!S.empty()) {
        cout << S[0] << "UPC";
    }
    return 0;
}