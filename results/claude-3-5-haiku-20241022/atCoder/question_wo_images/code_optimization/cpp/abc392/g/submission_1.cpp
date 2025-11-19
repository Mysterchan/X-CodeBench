#include <bits/stdc++.h>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  
  int N;
  cin >> N;
  
  vector<int> S(N);
  unordered_set<int> S_set;
  
  for(int i=0; i<N; i++){
    cin >> S[i];
    S_set.insert(S[i]);
  }
  
  long long count = 0;
  
  for(int i=0; i<N; i++){
    for(int j=i+1; j<N; j++){
      int A = S[i];
      int B = S[j];
      int C = 2*B - A;
      
      if(C > B && S_set.count(C)){
        count++;
      }
    }
  }
  
  cout << count << endl;
  
  return 0;
}