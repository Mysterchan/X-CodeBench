#include<bits/stdc++.h>
using namespace std;
int main(){
    int N;
    cin>>N;
    
    for(int i=1;i<=N;i++){
        for(int j=1;j<=N;j++){
            int k = min({i, j, N+1-i, N+1-j});
            if(k % 2 == 1){
                cout<<"#";
            }else{
                cout<<".";
            }
        }
        cout<<endl;
    }
    
    return 0;
}