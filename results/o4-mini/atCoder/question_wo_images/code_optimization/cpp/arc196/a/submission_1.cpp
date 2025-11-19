#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<ll> A(N);
    for(int i = 0; i < N; i++){
        cin >> A[i];
    }
    sort(A.begin(), A.end());
    int M = N / 2;
    ll sum_small = 0, sum_large = 0;
    for(int i = 0; i < M; i++){
        sum_small += A[i];
    }
    for(int i = N - M; i < N; i++){
        sum_large += A[i];
    }
    cout << (sum_large - sum_small) << "\n";
    return 0;
}