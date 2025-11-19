#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

const int MAX_A = 1000000;

vector<int> precompute() {
    vector<int> ans(MAX_A + 1, 0);
    
    for (int a = 2; a <= MAX_A; a++) {
        double log_a = log(a);
        double log_fact = 0.0;
        int n = 1;
        while (true) {
            log_fact += log(n);
            if (log_fact > n * log_a) {
                ans[a] = n;
                break;
            }
            n++;
        }
    }
    
    return ans;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    vector<int> ans = precompute();
    
    int t;
    cin >> t;
    
    while (t--) {
        int a;
        cin >> a;
        cout << ans[a] << "\n";
    }
    
    return 0;
}