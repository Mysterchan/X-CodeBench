#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    long long sum_parity = 0;
    int ones = 0;
    for(int i = 0; i < N; i++){
        long long a;
        cin >> a;
        if(a == 1) {
            ones++;
        }
        sum_parity ^= (a & 1LL);
    }

    // If there is at least one pile of size 1,
    // winner is determined by parity of N.
    if(ones > 0){
        if(N % 2 == 1) 
            cout << "Fennec\n";
        else 
            cout << "Snuke\n";
    }
    else {
        // Otherwise, winner is determined by parity of total sum of A_i.
        if(sum_parity % 2 == 1)
            cout << "Fennec\n";
        else
            cout << "Snuke\n";
    }
    return 0;
}