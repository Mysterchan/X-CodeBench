#include <iostream>
using namespace std;

int main() {
    string S;
    cin >> S;
    // Since S is always in the format digit x digit, directly multiply the digits
    cout << (S[0] - '0') * (S[2] - '0') << "\n";
    return 0;
}