#include<iostream>
#include<vector>
#include<unordered_map>
#include<algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;
    
    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    
    unordered_map<int, int> last_pos;
    int min_length = N + 1;
    
    for (int i = 0; i < N; i++) {
        if (last_pos.find(A[i]) != last_pos.end()) {
            min_length = min(min_length, i - last_pos[A[i]] + 1);
        }
        last_pos[A[i]] = i;
    }
    
    if (min_length == N + 1) {
        cout << -1;
    } else {
        cout << min_length;
    }
    
    return 0;
}