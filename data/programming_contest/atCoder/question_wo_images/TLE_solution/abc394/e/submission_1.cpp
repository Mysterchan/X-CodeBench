#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <cmath>
#include <iomanip>
#include <stack>
#include <queue>
#include <numeric>
#include <map>
#include <unordered_map>
#include <set>
#include <fstream>
#include <chrono>
#include <random>
#include <bitset>
#define rep(i,n) for(int i=0;i<(n);i++)
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define sz(x) ((int)(x).size())
#define pb push_back
using ll = long long;
using namespace std;
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T>bool chmin(T &a, const T &b) { if (b<a) { a=b; return 1; } return 0; }
ll gcd(ll a, ll b) {return b?gcd(b,a%b):a;}
ll lcm(ll a, ll b) {return a/gcd(a,b)*b;}

int main(){
  int N; cin >> N;
  vector<string> A(N);
  rep(i,N) cin >> A[i];
  int inf = 1<<20;
  vector G(N,vector<int>(N,inf));
  rep(i,N) G[i][i] = 0;
  rep(i,N) rep(j,N){
    if(A[i][j]!='-') chmin(G[i][j],1);
  }
  int cont=1;
  while(cont){
    cont = 0;
    rep(k,N) rep(l,N) rep(i,N){
      if(A[i][k]=='-') continue;
      rep(j,N){
        if(A[i][k]!='-' && A[i][k]==A[l][j]){
          if(chmin(G[i][j], G[k][l]+2)) cont=1;
        }
      }
    }
  }
  rep(i,N){
    rep(j,N){
      cout << (G[i][j]>=inf?-1:G[i][j]) << ' ';
    }
    cout << endl;
  }
  return 0;
}

