#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main() {
    int t;cin >>t;
    while (t--){
    int c=0;
        int n;cin >>n;
        while (n>=2){
            if (n%2==0){
            c++;
            }
        }
        if (n%2==0){
            cout <<n<<endl;
        }
        else {
            cout <<n+1<<endl;
        }
    }
}