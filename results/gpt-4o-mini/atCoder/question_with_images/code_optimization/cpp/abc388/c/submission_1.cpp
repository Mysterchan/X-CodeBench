#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    
    vector<int> A(N);
    for(int i = 0; i < N; i++){
        cin >> A[i];
    }
    
    int64_t totalCount = 0;
    
    for(int i = 0; i < N; i++) {
        int limit = 2 * A[i];
        int j = lower_bound(A.begin(), A.end(), limit) - A.begin(); // Find the first index where A[j] >= limit
        totalCount += (N - j); // Count the number of valid mochi that can be stacked on A[i]
    }
    
    cout << totalCount;
}