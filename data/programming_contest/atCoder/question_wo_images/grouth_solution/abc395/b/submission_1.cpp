#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    vector<string>ans(n, string(n, '\0'));

    char even=(((n+1)/2)%2==0 ? '.' : '#');
    char odd= (((n+1)/2)%2==1 ? '.' : '#');
    pair<int, int>mid;
    if(n%2==0){
        mid=make_pair(n/2, n/2-1);
    }else{
        mid=make_pair(n/2, n/2);
    }

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            int x=min(abs(i-mid.first), abs(i-mid.second));
            int y=min(abs(j-mid.first), abs(j-mid.second));
            int dis=max(x, y);

            if(dis%2==0)ans[i][j]=even;
            else ans[i][j]=odd;
        }
    }

    for(auto a:ans){
        cout<<a<<endl;
    }
}