#include <bits/stdc++.h>
using namespace std;

int main() {
    int T,n,a,b;
    scanf("%d",&T);
    while (T--) {
        scanf("%d %d %d",&n,&a,&b);
        if (b>=a) {
            puts(n%2==b%2?"YES":"NO");
        } else {
            puts(n%2==b%2&&n%2==a%2?"YES":"NO");
        }
    }
    return 0;
} 