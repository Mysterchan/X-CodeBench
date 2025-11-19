#include <bits/stdc++.h>
using namespace std;

bool check(unsigned n, string ch, vector<short> occup, unsigned id) {
  if (id == n) {
    if (ch[id] == '1') return find(occup.begin(), occup.end(), 1) == occup.end();

    if (ch[id - 1] == '1') occup[id - 1] = 0;
    auto crushed = find(occup.begin(), occup.end(), 1);
    if (crushed != occup.end() - 2 && crushed != occup.end())
      return false;

    return true;
  }

  if (ch[id] == '0') {
    if (ch[id - 1] == '1' && ch[id + 1] == '1') {
      occup[id - 1]++;
      bool res1 = check(n, ch, occup, id + 1);
      occup[id - 1]--;
      occup[id + 1]++;
      bool res2 = check(n, ch, occup, id + 1);
      return (res1 | res2);
    }
    if (ch[id - 1] == '1') {
      occup[id - 1]++;
      bool res1 = check(n, ch, occup, id + 1);
      occup[id - 1]--;
      bool res2 = check(n, ch, occup, id + 1);
      return (res1 | res2);
    }
    if (ch[id + 1] == '1') {
      occup[id + 1]++;
      bool res1 = check(n, ch, occup, id + 1);
      occup[id + 1]--;
      bool res2 = check(n, ch, occup, id + 1);
      return (res1 | res2);
    }


  }


  return check(n, ch, occup, id + 1);
}

int main() {
  int t;
  scanf("%d", &t);
  for (int i = 0; i < t; ++i) {
    unsigned n;
    scanf("%u", &n);

    char str[n];
    scanf("%s", str);

    bool nice = check(n, string("0") + str + "0", vector<short>(n + 2, 0), 1);

    if (nice) printf("YES\n");
    else printf("NO\n");
  }
}
