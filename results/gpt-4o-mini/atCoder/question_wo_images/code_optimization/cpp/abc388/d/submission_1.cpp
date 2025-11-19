#include<bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n+1), b(n+1);

    for(int i = 1; i <= n; i++) {
        cin >> a[i];
    }

    // Calculate the cumulative stones given as gifts
    for(int i = 1; i <= n; i++) {
        if (a[i] > 0) {
            int stones_given = min(a[i], n - i);
            b[i] += stones_given; // The current alien receives stones
            if (i + stones_given + 1 <= n) {
                b[i + stones_given + 1] -= stones_given; // The current alien will not give more stones after this year
            }
        }
    }

    // Calculate the final number of stones for each alien
    int current_gifts = 0;
    for(int i = 1; i <= n; i++) {
        current_gifts += b[i];
        a[i] -= i > 1 ? (a[i - 1] - (i - 1)) : 0; // Only apply the reduction from the previous alien
        a[i] += current_gifts; // Add the gifts
        cout << a[i] << ' ';
    }

    return 0;
}