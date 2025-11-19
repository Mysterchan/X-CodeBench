#include<bits/stdc++.h>
using namespace std;
using ll = long long;


int n;
const int maxn = 5e5 +5;
ll a[maxn];
ll b[maxn];


#define lowbit(x) ( (x) & -(x) )
ll c[maxn];


inline void add ( int x, ll y ) {

    if ( x <= 0 ) return ;
    
    
    for (  ; x <= 500000 ; x += lowbit(x) ) {

        c[x] += y;
    }

    return ;
}


inline ll getsum ( int x ) {

    if ( x <= 0 ) return 0;
    
    
    ll res = 0;
    for (  ; x >= 1 ; x -= lowbit(x) ) {

        res += c[x];
    }

    return res;
}


int main (  ) {
    cin.tie(0)->sync_with_stdio(0);

    cin >> n;
    for ( int i = 1 ; i <= n ; i++ ) {

        cin >> a[i];
    }


    for ( int i = 1 ; i <= n ; i++ ) {

        ll sum = getsum( 500000 ) - getsum( i - 1 );

        add( a[i] + sum + i, 1 );

        b[i] = max( 0LL, a[i] + sum - ( n - i ) );
    } 


    for ( int i = 1 ; i <= n ; i++ ) {

        cout << b[i] << " ";
    }
    cout << "\n";
    

    return 0;
}