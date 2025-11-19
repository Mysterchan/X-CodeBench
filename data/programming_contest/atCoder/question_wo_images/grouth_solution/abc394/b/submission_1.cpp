#include <bits/stdc++.h>

using namespace std;

int main(){
  int N;
  cin >> N;
  vector<string> S(N);
  for(int i=50;i>=1;i++){
    for(int j=0;j<N;j++){
      if(S[j].length()==i){
        cout << S[j];
        break;
      }
    }
  }
}