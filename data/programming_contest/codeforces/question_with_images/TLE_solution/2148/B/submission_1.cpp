#include<bits/stdc++.h>
using namespace std;

int main(){
    int T;
    cin>>T;
    while(T--){
        int n1,n2,x,y;
        cin>>n1>>n2>>x>>y;
        unordered_set<int > horizontal;
        unordered_set<int > vertical;
        while(n1--){
            int k;
            cin>>k;
            horizontal.insert(k);
        }
         while(n2--){
            int k;
            cin>>k;
             vertical.insert(k);
        }
        int count=0;
        
        for(int i=0;i<=x;i++){
            if(vertical.find(i)!=vertical.end()){
                count++;
            }
        }
        for(int i=0;i<=y;i++){
            if(horizontal.find(i)!=horizontal.end()){
                count++;
            }
        }
        cout<<count<<endl;
        
        
    }
    return 0;
}