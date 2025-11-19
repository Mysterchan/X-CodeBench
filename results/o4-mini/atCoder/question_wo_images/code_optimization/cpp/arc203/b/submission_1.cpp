#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    if(!(cin >> T)) return 0;
    while(T--){
        int N;
        cin >> N;
        vector<int> A(N), B(N);
        ll sumA = 0, sumB = 0;
        for(int i = 0; i < N; i++){
            cin >> A[i];
            sumA += A[i];
        }
        for(int i = 0; i < N; i++){
            cin >> B[i];
            sumB += B[i];
        }
        if(sumA != sumB){
            cout << "No\n";
            continue;
        }
        // if there's exactly 1 one or exactly 1 zero, no non-trivial swaps possible
        if(sumA == 1 || sumA == N-1){
            // only possible if A already equals B
            if(A == B) cout << "Yes\n";
            else cout << "No\n";
        } else {
            // otherwise, as long as sums match, it's always possible
            cout << "Yes\n";
        }
    }
    return 0;
}