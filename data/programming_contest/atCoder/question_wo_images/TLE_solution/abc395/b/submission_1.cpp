#include<bits/stdc++.h>
using namespace std;
int main(){
    int N;
    cin>>N;

    for(int i=1;i<=N;i++){
     for(int k=1;k<=N;k++){
        int j=N+1-i;
     while(j>0){
        
            if(i<=j&&j%2==1){
                cout<<"#";
            }else if(i<=j&&j%2==0){
                cout<<".";
            }
      }
      cout<<endl;
     }
     
}
}


