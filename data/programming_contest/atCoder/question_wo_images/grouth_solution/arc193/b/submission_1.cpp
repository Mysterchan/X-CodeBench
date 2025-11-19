#include <bits/stdc++.h>
#define rep(i, a, b) for (int i = (a), i##ABRACADABRA = (b); i <= i##ABRACADABRA; i++)
#define drep(i, a, b) for (int i = (a), i##ABRACADABRA = (b); i >= i##ABRACADABRA; i--)
using namespace std;
using ll = long long;
constexpr int mod=998244353;

int n,a[2][2][2][2][2],res;
char s[1000010];

void ad(int&x,int y){x+=y,x-=x>=mod?mod:0;}

int main() {
  scanf("%d%s",&n,s+1);
  auto f=a[0],g=a[1];
  if (s[1]=='0'){
    f[0][0][0][1]=1;
    f[0][1][1][0]=1;
    f[1][0][0][0]=1;
  }else{
    f[0][0][0][1]=1;
    f[0][1][1][1]=1;
    f[1][1][1][0]=1;
    f[1][0][0][0]=1;
  }
  rep(i,2,n){
    swap(f,g);
    rep(j00,0,1)rep(j01,0,1)rep(j10,0,1)rep(j11,0,1)
      f[j00][j01][j10][j11]=0;
    rep(i00,0,1)rep(i01,0,1)rep(i10,0,1)rep(i11,0,1)
      if (s[i]=='0'){
        {
          int j00=0,j01=0,j10=0,j11=0;
          j00|=i01;
          j10|=i11;
          ad(f[j00][j01][j10][j11],g[i00][i01][i10][i11]);
        }
        {
          int j00=0,j01=0,j10=0,j11=0;
          j00|=i00,j01|=i01;
          j10|=i10,j11|=i11;
          ad(f[j00][j01][j10][j11],g[i00][i01][i10][i11]);
        }
        {
          int j00=0,j01=0,j10=0,j11=0;
          j01|=i00;
          j11|=i10;
          ad(f[j00][j01][j10][j11],g[i00][i01][i10][i11]);
        }
      }else{
        {
          int j00=0,j01=0,j10=0,j11=0;
          j00|=i01;
          j10|=i11;
          ad(f[j00][j01][j10][j11],g[i00][i01][i10][i11]);
        }
        {
          int j00=0,j01=0,j10=0,j11=0;
          j00|=i01;
          j10|=i11;
          j00|=i00,j01|=i01;
          j10|=i10,j11|=i11;
          ad(f[j00][j01][j10][j11],g[i00][i01][i10][i11]);
        }
        {
          int j00=0,j01=0,j10=0,j11=0;
          j00|=i00,j01|=i01;
          j10|=i10,j11|=i11;
          j01|=i00;
          j11|=i10;
          ad(f[j00][j01][j10][j11],g[i00][i01][i10][i11]);
        }
        {
          int j00=0,j01=0,j10=0,j11=0;
          j01|=i00;
          j11|=i10;
          ad(f[j00][j01][j10][j11],g[i00][i01][i10][i11]);
        }
      }
  }
  rep(i00,0,1)rep(i01,0,1)rep(i10,0,1)rep(i11,0,1)
    if (i01||i10)ad(res,f[i00][i01][i10][i11]);
  printf("%d\n",res);
  return 0;
}