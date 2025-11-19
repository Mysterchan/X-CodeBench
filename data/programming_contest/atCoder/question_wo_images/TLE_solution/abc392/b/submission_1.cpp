#include<bits/stdc++.h>

using namespace std;

int n, m, aa;
int a[1005];

int main(){
	cin >> n >> m;
	if (n == m){
		cout << 0;
		return 0;
	}
	for(int i = 0; i < n; i ++){
		cin >> a[i];
	}
	sort(a, a+n);
	for(int i = 1; i <= n; i ++){
		if(i = a[aa]){
			aa ++;
		}
		else{
			cout << i << " ";
		}
	}
	return 0;
}