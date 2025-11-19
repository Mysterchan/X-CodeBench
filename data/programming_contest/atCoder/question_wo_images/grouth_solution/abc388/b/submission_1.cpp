#include <bits/stdc++.h>
using namespace std;

int main() {

    int n,d;
    cin>>n>>d;
    vector<int>t(n),s(n);
    for(int i=0;i<n;i++) {
        int a,b;
        cin>>a>>b;
        t[i]=a;
        s[i]=a*b;
    }


    for(int j=0;j<d;j++) {
    for(int i=0;i<n;i++) {
            s[i]+=t[i];
        }
        int ans=*max_element(s.begin(),s.end());
        cout<<ans<<endl;
    }
    return 0;
}
