#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int T;
    cin >> T;
    while (T--) {
        int n, m;
        cin >> n >> m;

        vector<int> A(n), B(n);
        for (int i = 0; i < n; i++) cin >> A[i];
        for (int i = 0; i < n; i++) cin >> B[i];

        // Sort both arrays
        sort(A.begin(), A.end());
        sort(B.begin(), B.end());

        int result = 0;
        
        // Calculate the possible maximum for the rearrangement
        for (int i = 0; i < n; i++) {
            result = max(result, (A[i] + B[n - 1 - i]) % m);
        }
        
        cout << result << '\n';
    }
    return 0;
}
