#include<bits/stdc++.h>
using namespace std;
int a[500000];
int main(){
	int n;
	cin >> n;
	for(int i = 0 ; i < n ; i++) cin >> a[i];
	sort(a , a + n);
	int i = n / 2 - 1 , j = n - 1;
	int cnt = 0;
	while(i >= 0 && j >= n/2-1){
		if(a[i] * 2 <= a[j]){
			cnt++;
			i--;
			j--;
		}
		else{
			j--;
		}
	}
	cout << cnt;
}