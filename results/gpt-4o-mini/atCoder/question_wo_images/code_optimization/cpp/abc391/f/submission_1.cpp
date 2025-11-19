#include<bits/stdc++.h>
using namespace std;
#define int long long
const int N = 2e5 + 10;
int a[N], b[N], c[N];

signed main(){
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int n, K;
    cin >> n >> K;
    
    for(int i = 1; i <= n; i++) {
        cin >> a[i];
    }
    
    for(int i = 1; i <= n; i++) {
        cin >> b[i];
    }
    
    for(int i = 1; i <= n; i++) {
        cin >> c[i];
    }
    
    // Use a max-heap to keep track of the K largest values
    priority_queue<int> maxHeap;
    
    // The calculations of the values will be done in a smart way
    // Instead of calculating all combinations,
    // we will traverse over the elements considering their contributions
    
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j++) {
            for(int k = 1; k <= n; k++) {
                // Compute the value directly
                int currentValue = a[i] * b[j] + b[j] * c[k] + c[k] * a[i];
                
                // If we haven't reached K elements yet, we push directly
                if(maxHeap.size() < K) {
                    maxHeap.push(currentValue);
                } else if(currentValue > maxHeap.top()) {
                    // If the current value is greater than the smallest in the heap
                    maxHeap.pop();
                    maxHeap.push(currentValue);
                }
                
                // Early stopping condition: if we have looked at enough values
                if(maxHeap.size() >= K && currentValue <= maxHeap.top()) {
                    break; // No need to check further for this j,k combination
                }
            }
        }
    }
    
    // The K-th largest value will be at the top of the max-heap
    cout << maxHeap.top();
    return 0;
}