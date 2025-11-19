#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int n,s;
        cin>>n>>s;
        int p=0;
        for(int i=0;i<n;i++){
            int d1,d2,x,y;
            cin>>d1>>d2>>x>>y;
            int l=1;
            int r=s-1;
            for(int j=0;j<s;j++){
                if(x==l && y==r){
                   p++;
                   break;
                }
                else{
                    l++;
                    r--;
                }
            }
        }
        cout<<p<<endl;
    }
}