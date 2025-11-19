#include<bits/stdc++.h>
using namespace std;
const int N=1e6+10;
int main()
{
  int n,a[N],cnt=0;
  long long ans=0;
  cin>>n;
  map<int,int>mm;
  ans=(n-1)*n/2;
 
  for(int i=0;i<n;i++)
{
cin>>a[i];
mm[a[i]]++;
if(i)
{
  if(a[i]==a[i-1])ans-=(n-i-1),cnt++;
  
}
}
cout<<ans-(n-mm.size())+cnt;
}