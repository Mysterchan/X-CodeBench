#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(void){
    string s;
    ll l,r;
    cin >> l >> r;
    ll result = 0;
    int flag = 1;
    for(ll i = l; i <= r;i++){
        s = to_string(i);
        for(int j = 1;j < s.size();j++){
            if(s.at(0) <= s.at(j)){
                flag = 0;
                break;
            }
        }
        if(flag == 1){
            result++;
        }
        flag = 1;

    }

    cout << result << endl;
    return 0;
}