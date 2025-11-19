#include <iostream>
#include<vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int n;
    cin >> n;
    vector<int> arrp(n + 1);  
    vector<int> arrq(n + 1);  
    for(int i = 1; i <= n; i++){  
        cin >> arrp[i];
    }
    for(int i = 1; i <= n; i++){  
        cin >> arrq[i];
    }
    
    int find = 1;
    for(int j = 1; j <= n; j++){
        for(int i = 1; i <= n; i++){
            if(arrq[i] == find){
                cout << arrq[arrp[i]];
                if(find < n) cout << " ";  
                find++;
                break;  
            }
        }
    }
    
    return 0;
}