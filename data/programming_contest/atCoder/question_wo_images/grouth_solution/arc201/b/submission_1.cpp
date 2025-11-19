#include <vector>
#include <iostream>
#include <algorithm>

#define ll long long

using namespace std;

const int N = 2e5 + 10;

int n;
ll w;
vector <ll> y[62];
ll f[62][2];

void work () {
    for (int i = 0; i <= 60; i ++) y[i].clear ();
    scanf ("%d%lld", &n, &w);
    for (int i = 1; i <= n; i ++) {
        int u; ll v; scanf ("%d%lld", &u, &v);
        y[u].push_back (v);
    }

    int i = 0; ll ans = 0;
    for (i = 0; i <= 60; i ++) {
        if ((1ll << i) > w) break ;
        sort (y[i].begin (), y[i].end ());
        if ((w >> i & 1) && !y[i].empty ()) ans += y[i].back (), y[i].pop_back ();
        while (y[i].size () > 1) y[i + 1].push_back (y[i].back () + y[i][y[i].size () - 2]), y[i].pop_back (), y[i].pop_back (); 
        if (y[i].size ()) y[i + 1].push_back (y[i].back ());
    }

    printf ("%lld\n", ans);
}

int main (void) {

    int t; scanf ("%d", &t);
    while (t --) work ();

    return 0;
}