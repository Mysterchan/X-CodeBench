#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 1000005,mod = 998244353;
string s[N];
int n,m;

int fa[N*4];
int find(int x){return fa[x]?fa[x]=find(fa[x]):x;}
void merge(int x,int y){
    x = find(x),y = find(y);
    if(x==y)
        return;
    fa[x] = y;
}

int w;
int id(int x,int y){return x*m+y;}

void sam(int x,int y){
    merge(x<<1,y<<1);
    merge(x<<1|1,y<<1|1);
}
void dif(int x,int y){
    merge(x<<1,y<<1|1);
    merge(x<<1|1,y<<1);
}



int main(){
    int t;
    cin >> t;
    while(t--){
        cin >> n >> m;
        memset(fa,0,sizeof(int)*(2*n*m*2));
        for(int k=0;k<n;k++)
            cin >> s[k];
        
        for(int k=0;k<n;k++)
            for(int j=0;j<m;j++){
                int U = id(k*2,j),D = id((k*2+2)%(n*2),j),L = id(k*2+1,j),R = id(k*2+1,(j+1)%m);
                if(s[k][j]=='A'){
                    dif(U,D);
                    dif(L,R);
                }
                else{
                    sam(U,D);
                    sam(L,R);
                    dif(U,L);
                }
            }

        for(int k=0;k<2*n*m;k++)
            if(find(k<<1)==find(k<<1|1))
                goto yohane;
    
        goto yoshiko;
        yohane:;
        puts("0");
        continue;
        yoshiko:;

        int ans = 1;
        for(int k=0;k<2*n*m;k++)
            if(find(k<<1)==(k<<1))
                ans = ans*2%mod;
        cout << ans << endl;
    }
}