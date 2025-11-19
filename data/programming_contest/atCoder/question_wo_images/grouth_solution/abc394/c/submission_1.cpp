#include <bits/stdc++.h>
using namespace std;

int main(){
    string S;
    cin >> S;
    vector<char> s((int)S.size() + 1);
    for(int i = 0; i < (int)S.size(); i++) {
        s.at(i) = S.at(i);
    }
    while(true) {
        bool wa = false;
        for(int i = 0; i < (int)S.size(); i++) {
            if(s.at(i) == 'W' && s.at(i + 1) == 'A') {
                wa = true;
                s.at(i) = 'A';
                s.at(i + 1) = 'C';
            }
        }
        if(wa == false) {
            break;
        }
    }
    
    for(int i = 0; i < (int)S.size(); i++) {
        cout << s.at(i);
    }
    cout << endl;
    
    return 0;
}
