#include<bits/stdc++.h>
using namespace std;
void coY(){cout<<"Yes"<<endl;}
void coN(){cout<<"No"<<endl;}
int main(){
  int n,x,z=0,j;
  cin>>n;
  for(j=0;j<n;j++){
    cin>>x;
    if(x==0) z++;
  }
  if(n%4==0) coY();
  else if(n%2==1){
    if(z==n) coN();
    else coY();
  }
  else if(n%4==2){
    if(z>=n-1) coN();
    else coY();
  }
}