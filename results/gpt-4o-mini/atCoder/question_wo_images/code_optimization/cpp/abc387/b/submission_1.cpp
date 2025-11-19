#include<bits/stdc++.h> 
using namespace std;
int main()
{
    int x;
    cin >> x;
    int totalSum = 0;
    int excludedSum = 0;

    // Calculate the total sum of the multiplication table and the sum of excluded value.
    for(int i = 1; i <= 9; i++) {
        for(int j = 1; j <= 9; j++) {
            int value = i * j;
            totalSum += value;
            if (value == x) {
                excludedSum += value;
            }
        }
    }
    
    // The result is the total sum minus the sum of excluded values
    cout << totalSum - excludedSum << endl;
    return 0;
}