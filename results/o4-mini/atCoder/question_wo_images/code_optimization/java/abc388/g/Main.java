#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    vector<ll> A(N);
    for(int i = 0; i < N; i++){
        cin >> A[i];
    }
    int Q;
    cin >> Q;
    while(Q--){
        int L, R;
        cin >> L >> R;
        // convert to 0-based
        L--; R--;
        int len = R - L + 1;
        int maxPairs = len / 2;
        int i = L;
        int j = L + (len+1)/2;
        int cnt = 0;
        // greedy two-pointer
        while(i < L + maxPairs && j <= R){
            if (2LL * A[i] <= A[j]){
                cnt++;
                i++;
                j++;
            } else {
                j++;
            }
        }
        cout << cnt << "\n";
    }
    return 0;
}