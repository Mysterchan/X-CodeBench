#include<bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    vector<int> a(n);
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    
    set<vector<int>> unique_sequences;
    
    for(int L = 0; L < n; ++L) {
        vector<int> seq = a;
        for(int R = L; R < n; ++R) {
            seq[R] = a[L];
            unique_sequences.insert(seq);
        }
    }
    
    cout << unique_sequences.size() << endl;
    return 0;
}