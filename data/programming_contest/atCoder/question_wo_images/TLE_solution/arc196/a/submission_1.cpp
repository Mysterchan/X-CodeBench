#include<bits/stdc++.h>
using namespace std;
#define int long long

signed main() {
  int N;
  cin >> N;
  if (N%2 == 0) {
    vector<int> A(N);
    for (int i = 0; i<N; i++) cin >> A[i];
    sort(A.rbegin(), A.rend());
    int M = N/2;
    int ans = 0;
    for (int i = 0; i<M; i++) ans += A[i];
    for (int i = 1; i<=M; i++) ans -= A[N-i];
    cout << ans;
  }
  else {
    while (true) {
      
    }
  }
}
