#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; cin >> n;
    vector<int> a(n);
    int sum = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        sum += a[i];
    }

    // If no zeros, answer is Yes
    if (sum == n) {
        cout << "Yes\n";
        return 0;
    }

    // Check for the condition "ture" in original code:
    // There exist two 1's at positions with even distance (difference divisible by 2)
    // i.e. there exist i < j with a[i] = a[j] = 1 and (j - i) % 2 == 0
    // Since the array is circular, we check pairs modulo n.

    // To optimize, we can check parity groups:
    // If there are at least two 1's in the same parity index (even or odd),
    // then ture = true.

    int even_count = 0, odd_count = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] == 1) {
            if (i % 2 == 0) even_count++;
            else odd_count++;
        }
    }

    bool ture = (even_count > 1) || (odd_count > 1);

    // Now apply the final condition from original code:
    // if n % 4 == 0 => Yes
    // else if n % 4 == 1 or 3 and sum > 0 => Yes
    // else if n % 4 == 2 and ture => Yes
    // else No

    int mod = n % 4;
    if (mod == 0) {
        cout << "Yes\n";
    } else if ((mod == 1 || mod == 3) && sum > 0) {
        cout << "Yes\n";
    } else if (mod == 2 && ture) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}