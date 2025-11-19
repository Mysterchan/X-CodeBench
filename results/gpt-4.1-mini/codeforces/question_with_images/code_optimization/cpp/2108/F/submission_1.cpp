#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        vector<long long> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];

        // The key insight:
        // After knocking down all towers in order from left to right,
        // the final height of tower i is:
        // final[i] = max(i, a[i]) - a[i] + (sum of increments from previous towers)
        // But increments from previous towers can be simulated by a "carry" variable.
        //
        // We want the final array to be non-decreasing.
        // We can simulate the process greedily from left to right:
        // At each tower i:
        //   - We have a carry (increments from previous towers)
        //   - The tower height after knocking down is max(a[i] - carry, 0)
        //   - We set carry = max(carry, a[i])
        //
        // The final heights after all operations are the values of carry at each step.
        //
        // The maximum MEX is the largest integer m such that all integers from 0 to m-1
        // appear in the final array.
        //
        // Since the final array is non-decreasing and each element >= carry,
        // the MEX is the smallest integer not in the final array.
        //
        // We can find MEX by checking from 0 upwards if carry >= mex.

        long long carry = 0;
        for (int i = 0; i < n; i++) {
            if (a[i] > carry) carry = a[i];
            else carry = carry;
            carry = max(carry - 1, 0LL);
        }

        // The MEX is carry + 1
        cout << carry + 1 << "\n";
    }

    return 0;
}