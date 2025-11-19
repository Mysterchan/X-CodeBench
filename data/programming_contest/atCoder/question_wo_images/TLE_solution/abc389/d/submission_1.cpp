#include <iostream>

using namespace std;

long long_sqrt(long x)
{
    long result = 0;
    for (long i = 1; i * i <= x; i++) {
        result = i;
    }
    return result;
}

long f(long r, long x)
{
    return (long_sqrt((2 * r) * (2 * r) - (x + 1) * (x + 1)) - 1) / 2 * 2 + 1;
}

int main()
{
    long r;
    cin >> r;

    long answer = 0;
    for (long j = 2; j <= long_sqrt((2 * r) * (2 * r) - 1); j += 2) {
        answer += f(r, j);
    }
    answer *= 2;
    answer += f(r, 0);

    cout << answer << endl;
}