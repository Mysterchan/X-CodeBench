#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

const int N = 510;

int a[N][N],pre[N][N];

int main()
{
    int n,q;
    
    cin>>n>>q;
    for(int i=1;i<=n;i++){
        string s;
        cin>>s;
        for(int j=0;j<n;j++){
            if(s[j]=='.') a[i][j+1]=1;
        }
    }
    
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            if(a[i][j]==1&&a[i+1][j]==1&&a[i][j+1]==1&&a[i+1][j+1]==1){
                a[i][j]=0;
                pre[i][j]=1;
            }
        }
    }
    
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            pre[i][j]+=pre[i-1][j]+pre[i][j-1]-pre[i-1][j-1];
        }
    }
    
    while(q--){
        int x,y,x1,y1;
        cin>>x>>x1>>y>>y1;
        if(abs(x-x1)==0 || abs(y-y1)==0){
            cout<<0<<"\n";
            continue;
        }
        x1--,y1--;
        cout<<(pre[x1][y1]-pre[x1][y-1]-pre[x-1][y1]+pre[x-1][y-1])<<"\n";
    }

}