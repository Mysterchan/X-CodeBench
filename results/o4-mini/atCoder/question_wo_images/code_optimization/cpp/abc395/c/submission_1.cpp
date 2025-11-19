#include <iostream>
#include <vector>
#include <limits>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    const int MAXA = 1000000;
    vector<int> lastPos(MAXA + 1, -1);
    int answer = numeric_limits<int>::max();

    for (int i = 0; i < N; i++) {
        int x;
        cin >> x;
        if (lastPos[x] != -1) {
            int length = i - lastPos[x] + 1;
            if (length < answer) {
                answer = length;
            }
        }
        lastPos[x] = i;
    }

    if (answer == numeric_limits<int>::max()) {
        cout << -1 << "\n";
    } else {
        cout << answer << "\n";
    }

    return 0;
}