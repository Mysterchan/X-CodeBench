#include <iostream>
#include <cmath>

using namespace std;

int main() {
    long long r;
    cin >> r;

    long long count = 0;
    long long limit = r * r;

    for (long long x = -r; x <= r; ++x) {
        long long y_bound = sqrt(limit - x * x);
        count += (y_bound * 2) + 1;
    }

    cout << count << endl;
    return 0;
}