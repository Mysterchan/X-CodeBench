#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];

    unordered_map<int, int> last_pos;
    int ans = N + 1;

    for (int i = 0; i < N; i++) {
        if (last_pos.count(A[i])) {
            int length = i - last_pos[A[i]] + 1;
            if (length < ans) ans = length;
        }
        last_pos[A[i]] = i;
    }

    if (ans == N + 1) cout << -1 << "\n";
    else cout << ans << "\n";

    return 0;
}