#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while (T--) {
        long long X, Y, Z;
        cin >> X >> Y >> Z;

        // The problem reduces to checking if a sequence with given counts of 0,1,2
        // can satisfy the condition:
        // For each element A_i, exactly A_i neighbors are less than A_i.
        //
        // From analysis and the original code logic:
        // - If X < Z, answer is No.
        // - Then, after some deductions on Y, if Y is zero or less, answer is Yes, else No.
        //
        // The original code tries to simulate some decrements on Y based on Z and X.
        // We can directly compute the final Y after these decrements to avoid loops.
        //
        // Let's rewrite the logic mathematically:
        //
        // Step 1: if X < Z => No
        // Step 2: y -= z + max(0, z-1) = y - (2z -1) if z>0 else y
        // Step 3: x -= z
        // Step 4: y -= 2 * max(0, x - 0) if y > 1 (but original code does it in a loop)
        // Actually, the original code:
        //   for i in [0..z-1]:
        //     if y>0 y--
        //     if i<z-1 and y>0 y--
        // So total y decremented by z + (z-1) = 2z -1 if z>0, else 0
        //
        // Then:
        //   x -= z
        //   for i in [0..x-1]:
        //     if y>1 y -= 2
        // So y is reduced by 2 for each i while y>1
        // This is equivalent to y -= 2 * min(x, y/2)
        //
        // Finally:
        //   if z>0 and y>0 y--
        //
        // Then if y == 0 output Yes else No
        //
        // Let's implement this logic directly with O(1) operations.

        if (X < Z) {
            cout << "No\n";
            continue;
        }

        // Decrement y by 2z -1 if z>0
        if (Z > 0) {
            Y -= 2 * Z - 1;
        }

        if (Y < 0) {
            cout << "No\n";
            continue;
        }

        X -= Z;

        // Decrement y by 2 * min(X, Y/2)
        long long dec = min(X, Y / 2);
        Y -= 2 * dec;

        if (Z > 0 && Y > 0) {
            Y--;
        }

        cout << (Y == 0 ? "Yes" : "No") << "\n";
    }

    return 0;
}