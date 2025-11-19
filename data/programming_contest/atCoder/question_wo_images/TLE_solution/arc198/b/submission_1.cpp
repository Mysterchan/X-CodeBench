#include <bits/stdc++.h>
using namespace std;
int t,x,y,z;
int main() {
  scanf("%d",&t);
  while (t--) {
    scanf("%d%d%d",&x,&y,&z);
    if (x<z) { puts("No"); continue; }
    int m=0;
    for (int i=0; i<z; i++) {
      if (y>0) --y;
      if (i<z-1 && y>0) --y;
    }
    x-=z;
    for (int i=0; i<x; i++) if (y>1) y-=2;
    if (z>0 && y>0) --y;
    puts(y?"No":"Yes");
  }
  return 0;
}
