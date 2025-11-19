#include <bits/stdc++.h>
using namespace std;

int main() {
  string S;
  cin >> S;
  
  for(char &c : S) {
    if(c == 'N') c = 'S';
    else if(c == 'S') c = 'N';
    else if(c == 'E') c = 'W';
    else if(c == 'W') c = 'E';
  }
  
  cout << S << endl;
}