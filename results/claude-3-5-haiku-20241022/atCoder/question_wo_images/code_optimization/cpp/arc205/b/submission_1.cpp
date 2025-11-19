#include<bits/stdc++.h>
using namespace std;

int main(){
    long long n, m;
    cin >> n >> m;
    
    long long total_edges = n * (n - 1) / 2;
    long long max_black = total_edges;
    
    // Check if parity matches
    if (total_edges % 2 != m % 2) {
        max_black = total_edges - 1;
    }
    
    cout << max_black << endl;
    
    return 0;
}