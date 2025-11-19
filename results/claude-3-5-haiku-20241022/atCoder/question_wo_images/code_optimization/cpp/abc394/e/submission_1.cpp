#include <iostream>
#include <string>
#include <vector>
#include <queue>
#define rep(i,n) for(int i=0;i<(n);i++)
using namespace std;

int main(){
  int N; 
  cin >> N;
  vector<string> A(N);
  rep(i,N) cin >> A[i];
  
  int inf = 1<<20;
  vector<vector<int>> G(N, vector<int>(N, inf));
  
  // Initialize: distance 0 for same vertex
  rep(i,N) G[i][i] = 0;
  
  // BFS approach: process by length
  queue<tuple<int,int,int>> q; // (from, to, length)
  
  // Length 1: single edges
  rep(i,N) rep(j,N){
    if(A[i][j] != '-' && G[i][j] > 1){
      G[i][j] = 1;
      q.push({i, j, 1});
    }
  }
  
  while(!q.empty()){
    auto [i, j, len] = q.front();
    q.pop();
    
    if(G[i][j] < len) continue;
    
    // Try to extend: find k where edge (i,k) exists and l where edge (l,j) exists
    // and the labels match
    rep(k,N){
      if(A[i][k] == '-') continue;
      char c1 = A[i][k];
      
      rep(l,N){
        if(A[l][j] == '-') continue;
        if(A[l][j] != c1) continue;
        
        int new_len = G[k][l] + 2;
        if(new_len < G[i][j]){
          G[i][j] = new_len;
          q.push({i, j, new_len});
        }
      }
    }
  }
  
  rep(i,N){
    rep(j,N){
      cout << (G[i][j] >= inf ? -1 : G[i][j]);
      if(j < N-1) cout << ' ';
    }
    cout << '\n';
  }
  
  return 0;
}