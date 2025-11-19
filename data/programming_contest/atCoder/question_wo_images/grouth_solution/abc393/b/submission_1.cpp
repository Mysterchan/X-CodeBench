#include<bits/stdc++.h>
using namespace std;

int main(){
  string s;
  cin >> s;
  int n = 0, l = s.size();
  
  for(int i = 0; i < l - 1 / 2; i++){
    for(int j = 0; j < l - 2 * i - 2; j++){
      if(s[j] == 'A' && s[i + j + 1] == 'B' && s[2 * (i + 1) + j] == 'C') n++;
    }
  }
  cout << n << endl;
}
