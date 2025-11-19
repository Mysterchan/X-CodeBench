#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ll H,W;
    cin>>H>>W;
    vector<string> S(H);
    for(ll i=0;i<H;i++){
      cin>>S[i];
    }
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};
    
    vector<pair<ll,ll>> T;
    for(ll x=0;x<H;x++){
      for(ll y=0;y<W;y++){
        if(S[x][y]=='.'){
          ll cnt = 0;
          for(int k=0;k<4;k++){
            ll nx = x+dx[k];
            ll ny = y+dy[k];
            if(nx>=0 && nx<H && ny>=0 && ny<W && S[nx][ny]=='#'){
              cnt++;
            }
          }
          if(cnt==1){
            T.push_back({x,y});
          }
        }
      }
    }
    
    for(ll i=0;i<H*W;i++){
      if(T.empty()){
        break;
      }
      for(auto [x,y]:T){
        S[x][y] = '#';
      }
      
      vector<pair<ll,ll>> nT;
      for(auto [x,y]:T){
        for(int k=0;k<4;k++){
          ll nx = x+dx[k];
          ll ny = y+dy[k];
          if(nx>=0 && nx<H && ny>=0 && ny<W && S[nx][ny]=='.'){
            int cnt=0;
            for(int p=0;p<4;p++){
              ll cx = nx+dx[p];
              ll cy = ny+dy[p];
              if(cx>=0 && cx<H && cy>=0 && cy<W && S[cx][cy]=='#'){
                cnt++;
              }
            }
            if(cnt==1){
              nT.push_back({nx,ny});
            }
          }
        }
      }
      T = move(nT);
    }
    
    ll ans = 0;
    for(ll i=0;i<H;i++){
      for(ll j=0;j<W;j++){
        if(S[i][j] == '#'){
          ans++;
        }
      }
    }
    cout<<ans<<endl;
}
