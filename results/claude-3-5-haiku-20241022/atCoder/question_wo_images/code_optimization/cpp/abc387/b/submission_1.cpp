#include<bits/stdc++.h> 
using namespace std;
int main()
{
	int x;
	cin>>x;
	
	int total = 2025; // Sum of all 81 integers in 9x9 multiplication table = (1+2+...+9)^2
	
	// Count occurrences of x in the multiplication table
	int count = 0;
	for(int i=1; i<=9; i++) {
		if(x % i == 0 && x / i <= 9) {
			count++;
		}
	}
	
	cout << total - count * x << endl;
	return 0;
}