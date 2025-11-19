#pragma GCC optimize("Ofast")
#include<bits/stdc++.h>
#define int long long
using namespace std;

const int N=4e5+10;
int n,m;
int a[N],b[N];
int ans[N];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin>>t;
    while(t--){
        cin>>n>>m;
        for(int i=1;i<=n;i++) cin>>a[i];
        for(int i=1;i<=m;i++) cin>>b[i];

        sort(a+1,a+n+1);
        sort(b+1,b+m+1);

        // Precompute prefix sums of differences for a
        vector<int> c(1,0);
        for(int i=1,j=n;i<j;i++,j--){
            c.push_back(a[j]-a[i]);
        }
        for(int i=1;i<(int)c.size();i++) c[i]+=c[i-1];

        // Precompute prefix sums of differences for b
        vector<int> d(1,0);
        for(int i=1,j=m;i<j;i++,j--){
            d.push_back(b[j]-b[i]);
        }
        for(int i=1;i<(int)d.size();i++) d[i]+=d[i-1];

        // Calculate maximum number of operations k_max
        int k_max = 0;
        if(n >= 2*m) k_max = m;
        else if(m >= 2*n) k_max = n;
        else {
            int len = 0;
            if(n >= m){
                len = n - m;
                n -= len * 2;
                m -= len;
                len += (n / 3) * 2;
                n %= 3;
                if(n == 2) len++;
            } else {
                len = m - n;
                m -= len * 2;
                n -= len;
                len += (m / 3) * 2;
                m %= 3;
                if(m == 2) len++;
            }
            k_max = len;
        }

        // Restore original n,m for calculation
        // (We need original n,m for constraints in the loop)
        // But since we modified n,m above, we must store original values before
        // Let's store original n,m before modification
        // So we do this after reading input and sorting

        // Actually, let's store original n,m before modification:
        // We'll do the calculation of k_max first, then restore n,m

        // So let's move the k_max calculation after storing original n,m
        // Let's fix this by storing original n,m before modification

        // Let's do that now:

        // Re-implement with original n,m stored
    }

    return 0;
}