#include <bits/stdc++.h>
using namespace std;

int main() {
  
  int N;
  cin >> N;
  
  vector<int> S(N);
  
  for(int i=0; i<N; i++){
    cin >> S.at(i);
  }
  sort(S.begin(), S.end());
  
  int A, B, C;
  int X = 0;
  
  for(int a=0; a<N; a++){
    A = S.at(a);
    
    for(int b=a+1; b<N; b++){
      B = S.at(b);
      
      for(int c=b+1; c<N; c++){
        C = S.at(c);
        
        if(B-A==C-B){
          X += 1;
        }
      }
    }
  
  }  
   

 cout << X;  

    

  }