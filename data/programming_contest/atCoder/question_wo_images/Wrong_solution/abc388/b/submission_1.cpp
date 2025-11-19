#include <bits/stdc++.h>
using namespace std;
int t[105], l[105];
int main() {
  int n, d;
  cin >> n >> d;
  for(int i=0;i<n;i++) {
    cin >> t[i] >> l[i];
  }
  for(int k=1;k<=d;k++) {
    int max_weight=0;
    for(int i=0;i<n;i++) {
      int weight=t[i]*(l[i]+k);
      max_weight=max(max_weight, weight);
    }
    cout << max_weight;
  }
  return 0;
}