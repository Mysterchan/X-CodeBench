#include<bits/stdc++.h>
#define int long long
using namespace std;
const int N = 2e5 + 5;
int T , n , px , py , qx , qy;
double dis(int a , int b , int x , int y){
	return sqrt((a - x) * (a - x) + (b - y) * (b - y));
}
double a[N];
signed main(){
	cin >> T;
	while(T--){
		cin >> n >> px >> py >> qx >> qy;
		for(int i = 1;i <= n;i++)cin >> a[i];
		if(n == 1){
			if(dis(px , py , qx , qy) == a[1])cout << "Yes\n";
			else cout << "No\n";
			continue;
		}
		a[n + 1] = dis(px , py , qx , qy);
		sort(a + 1 , a + n + 2);
		double sum = 0;
		for(int i = 1;i <= n;i++)sum += a[i];
		if(sum >= a[n + 1])cout << "Yes\n";
		else cout << "No\n";
	}
	return 0;
}
