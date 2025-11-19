#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    
    long long answer = 0;
    
    for (int L = 1; L <= N; L++) {
        for (int R = L; R <= N; R++) {
            vector<bool> present(N + 1, false);
            int min_val = N + 1, max_val = 0;
            
            for (int i = L - 1; i < R; i++) {
                present[A[i]] = true;
                min_val = min(min_val, A[i]);
                max_val = max(max_val, A[i]);
            }
            
            int components = 0;
            bool in_component = false;
            
            for (int val = min_val; val <= max_val; val++) {
                if (present[val]) {
                    if (!in_component) {
                        components++;
                        in_component = true;
                    }
                } else {
                    in_component = false;
                }
            }
            
            answer += components;
        }
    }
    
    cout << answer << endl;
    return 0;
}