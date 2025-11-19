#include <bits/stdc++.h>
using namespace std;
int main () {
  int N;
  cin >> N;
  string s = "1";
  for (int i = 0; i < N; i ++) {
    char c;
    cin >> c;
    s += c;
  }
  s += '1';
  int Q;
  cin >> Q;
  int oz = 0;
  int ozo = 0;
  for (int i = 0; i < N; i ++) {
    oz += (s.substr(i, 2) == "10");
    ozo += (s.substr(i, 3) == "101");
  }
  int cnt[] = {0, 0};
  for (int i = 1; i <= N; i ++) cnt[s[i] - '0'] ++;
  while (Q--) {
    int i;
    cin >> i;
    for (int j = i-1; j < i+1; j ++) oz -= (s.substr(j, 2) == "10");
    for (int j = max(0, i-2); j < min(N, i+1); j ++) ozo -= (s.substr(j, 3) == "101");
    cnt[s[i] - '0'] --;
    s[i] = (s[i] == '1' ? '0' : '1');
    cnt[s[i] - '0'] ++;
    for (int j = i-1; j < i+1; j ++) oz += (s.substr(j, 2) == "10");
    for (int j = max(0, i-2); j < min(N, i+1); j ++) ozo += (s.substr(j, 3) == "101");
    if (min(cnt[0], cnt[1]) == 0) {
      cout << (cnt[0] ? 2 : N) << endl;
      continue;
    }
    int os = oz - 1;
    os += (s[1] == '1') + (s[N] == '1');
    int z1 = ozo;
    int zl = (oz - ozo) * 2;
    if (s[1] == '0' && s[2] == '1') {
      z1 --;
      zl ++;
    }
    if (s[N] == '0' && s[N-1] == '1') {
      z1 --;
      zl ++;
    }
    os -= z1;
    cout << os + zl << endl;
  }
}