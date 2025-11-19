#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N;
    cin >> N;
    
    vector<int> P(N + 1);
    for (int i = 1; i <= N; i++) {
        cin >> P[i];
    }
    
    int Q;
    cin >> Q;
    
    while (Q--) {
        int A0, A1, A2;
        cin >> A0 >> A1 >> A2;
        
        int ans = 2 * min(A0, A1) + min(abs(A0 - A1), A2);
        cout << ans << '\n';
    }
    
    return 0;
}