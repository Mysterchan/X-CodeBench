#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> A(5);

    for (int i = 0; i < 5; i++) {
        cin >> A.at(i);
    }

    vector<vector<int>> CHECK = {
        {2, 1, 3, 4, 5},
        {1, 3, 2, 4, 5},
        {1, 2, 4, 3, 5},
        {1, 2, 3, 5, 4},
    };

    bool flag = false;
    for (int i = 0; i < 4; i++){
        if (A == CHECK.at(i)) {
            flag = true;
            break;
        }
    }
    
    if(flag) cout << "Yes" << endl;
    else cout << "No" << endl;
    
}