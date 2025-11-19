#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<long long> A(N);
    for(int i = 0; i < N; i++){
        cin >> A[i];
    }

    if(N <= 2){
        cout << "Yes\n";
        return 0;
    }

    bool ok = true;
    for(int i = 2; i < N; i++){
        // Check A[i] / A[i-1] == A[1] / A[0] using cross multiplication
        if (A[i] * A[0] != A[1] * A[i-1]) {
            ok = false;
            break;
        }
    }

    cout << (ok ? "Yes\n" : "No\n");
    return 0;
}