#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;

    int first = S[0] - '0'; 
    int second = S[2] - '0'; 
    
    int result = first * second;
    cout << result << endl;
    return 0;
}