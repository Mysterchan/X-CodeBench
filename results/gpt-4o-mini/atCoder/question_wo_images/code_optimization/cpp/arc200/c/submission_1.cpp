#include <bits/stdc++.h>

using namespace std;

const int MAXN = 500;

int L[MAXN + 5], R[MAXN + 5], P[MAXN + 5];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;

        for (int i = 1; i <= N; i++) {
            cin >> L[i] >> R[i];
        }

        vector<int> indices(N);
        iota(indices.begin(), indices.end(), 1);

        // Custom comparator: Sort based on time L and then R
        sort(indices.begin(), indices.end(), [](int a, int b) {
            return L[a] < L[b] || (L[a] == L[b] && R[a] < R[b]);
        });

        set<int> availableSeats;
        for (int i = 1; i <= N; i++) {
            availableSeats.insert(i);
        }

        for (int i : indices) {
            // Allocate the smallest available seat
            int smallestSeat = *availableSeats.begin();
            P[i] = smallestSeat;
            availableSeats.erase(smallestSeat);
        }

        for (int i = 1; i <= N; i++) {
            cout << P[i] << " ";
        }
        cout << "\n";
    }

    return 0;
}
