#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i = 0; i < (n); i++)
using ll = long long;

int main() {
    int n;
    cin >> n;
    map<ll,string> a;
    string s;
    rep(i,n) {
      cin >> s;
      int p = s.size();
      a[p] = s;
    }
    n += 2;
    rep(i,n) {
      auto result = a.find(i);
      if(result != a.end()) {
        cout << a[i];
      }
    }
    return 0;
}