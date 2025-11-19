#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long A, B;
    cin >> A >> B;
    long long sum = A + B;
    cout << sum * sum << "\n";

    return 0;
}