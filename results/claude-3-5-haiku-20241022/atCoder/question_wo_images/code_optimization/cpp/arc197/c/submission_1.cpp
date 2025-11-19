#include<bits/stdc++.h>
using namespace std;

int main(){
    int q;
    scanf("%d", &q);
    
    vector<long long> divisors;
    vector<int> queries(q);
    
    for(int i = 0; i < q; i++){
        long long a;
        int b;
        scanf("%lld%d", &a, &b);
        divisors.push_back(a);
        queries[i] = b;
    }
    
    auto is_valid = [&](long long x, int up_to) {
        for(int i = 0; i <= up_to; i++){
            if(x % divisors[i] == 0) return false;
        }
        return true;
    };
    
    for(int i = 0; i < q; i++){
        int needed = queries[i];
        int count = 0;
        long long num = 0;
        
        while(count < needed){
            num++;
            if(is_valid(num, i)){
                count++;
            }
        }
        
        printf("%lld\n", num);
    }
    
    return 0;
}