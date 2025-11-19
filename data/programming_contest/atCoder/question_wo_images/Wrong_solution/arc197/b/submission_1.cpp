#include<bits/stdc++.h>
#define C getchar()
#define LL long long
using namespace std;

inline int read() {
	int num = 0 , f = 0;
	char c = C;
	for(;c < '0' || c > '9';c = C) if (c == '-') f = 1;
	for(;c >= '0' && c <= '9';c = C) num = (num << 1) + (num << 3) + c - 48;
	return f ? -num : num;
}

int a[201000];

int main() {
	
	int T = read();
	while (T --) {
		int n = read();
		for(int i = 1;i <= n;++ i) a[i] = read();
		sort(a + 1 , a + n + 1);
		LL now = a[1];
		int Max = 0;
		for (int i = 2;i <= n;++ i) {
			double tmp = now + a[i];
			tmp /= i;
			int l = 1 , r = i;
			while (l < r - 1) {
				int mid = l + r >> 1;
				if (a[mid] > tmp) r = mid;
				 else l = mid;
			}
			int len = 0;
			if (a[l] > tmp) len = i - l + 1;
			 else if (a[r] > tmp) len = i - r + 1;
			if (len < Max) break;
			Max = len;
			now += a[i];
		}
		printf("%d\n",Max);
	}
	
	return 0;
}