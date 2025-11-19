#include <bits/stdc++.h>
using namespace std;



int main() {
  
 int N;
 cin >> N;
 
 vector<int> A(N);

 for(int i=0; i<N; i++){
   cin >> A.at(i);
 }
 
 int a, x;
 int64_t X = 0LL;
 
 for(int i=0; i<N; i++){
   a = A.at(i);
   
   if(A.at(N-1) < 2*a){
     break;
   }
   
   for(int j=i+1; j<N; j++){
     if(A.at(j) >= 2*a){
       X += N-j;
       break;
     }
   }
   
 }
   
  cout << X; 

} 