#include<bits/stdc++.h>

using namespace std;

int main(){
    int n, m;
    cin >> n >> m;
    
    vector<bool> present(n + 1, false);
    
    for(int i = 0; i < m; i++){
        int a;
        cin >> a;
        present[a] = true;
    }
    
    vector<int> missing;
    for(int i = 1; i <= n; i++){
        if(!present[i]){
            missing.push_back(i);
        }
    }
    
    cout << missing.size() << "\n";
    for(int i = 0; i < missing.size(); i++){
        if(i > 0) cout << " ";
        cout << missing[i];
    }
    if(!missing.empty()) cout << "\n";
    
    return 0;
}