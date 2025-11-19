#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<long long> a(n+1);
    
    for(int i = 1; i <= n; i++){
        cin >> a[i];
    }
    
    // Process each alien becoming adult
    for(int i = 1; i <= n; i++){
        // Count how many adults before i have stones
        int adults_with_stones = 0;
        for(int j = 1; j < i; j++){
            if(a[j] > 0) adults_with_stones++;
        }
        
        // Alien i receives stones from adults
        a[i] += adults_with_stones;
        
        // Alien i gives stones to future aliens
        int stones_to_give = min((long long)(n - i), a[i]);
        a[i] -= stones_to_give;
    }
    
    for(int i = 1; i <= n; i++){
        cout << a[i];
        if(i < n) cout << ' ';
    }
    
    return 0;
}