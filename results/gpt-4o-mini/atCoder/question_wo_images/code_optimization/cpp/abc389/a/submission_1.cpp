#include <iostream>
using namespace std;

int main() {
    string S;
    cin >> S;
    
    int a = S[0] - '0'; // Convert char to int
    int b = S[2] - '0'; // Convert char to int
    
    cout << a * b; // Print the product
    return 0;
}