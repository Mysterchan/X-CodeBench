#include <bits/stdc++.h>
using namespace std;
const long long MOD=1e9+7;
#define ll long long
#define int ll
bool compare(vector<int>& arr,vector<int>& brr)
{
    int n1=arr.size();
    int n2=brr.size();
    int t=min(n1,n2);
    for(int i=0;i<t;i++)
    {
        if(arr[i]!=brr[i]) return arr[i]<brr[i];
    }
    return n1<n2;
}
void solve()
{  
    int n;
    cin>>n;
    vector<vector<int>> arr(n);
    for(int i=0;i<n;i++)
    {
        int k;
        cin>>k;
        int x;
        for(int j=0;j<k;j++)
        {
            cin>>x;
            arr[i].push_back(x);
        }
    }
    sort(arr.begin(),arr.end(),compare);
    int len=0;
    int i=0;
    while(i<n)
    {
        while(len<arr[i].size())
        {
            cout<<arr[i][len]<<" ";
            len++;
        }
        i++;
    }
    cout<<"\n";
}
signed main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t=1;
    cin>>t;
    while(t--) solve();
} 

