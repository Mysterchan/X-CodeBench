#include <bits/stdc++.h>
using namespace std;

int G (char x) {
  if(x == 'N')x = 'S';
  if(x == 'S')x = 'N';
  if(x == 'W')x = 'E';
  if(x == 'E')x = 'W';
}
int G (string y) {
  if(y == "NE")y = "SW";
  if(y == "NW")y = "SE";
  if(y == "SE")y = "NW";
  if(y == "SW")y = "NE";
}
int main() {
  string S;
  cin >> S;
  
  cout << G (S) << endl;
}