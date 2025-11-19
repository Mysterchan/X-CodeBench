#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    
    long long answer = 0;
    
    for (int L = 0; L < N; L++) {
        vector<bool> present(N + 1, false);
        int min_val = N + 1, max_val = 0;
        
        for (int R = L; R < N; R++) {
            int val = A[R];
            
            if (!present[val]) {
                present[val] = true;
                
                if (val < min_val) {
                    min_val = val;
                }
                if (val > max_val) {
                    max_val = val;
                }
            }
            
            int components = 0;
            bool in_component = false;
            
            for (int v = min_val; v <= max_val; v++) {
                if (present[v]) {
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