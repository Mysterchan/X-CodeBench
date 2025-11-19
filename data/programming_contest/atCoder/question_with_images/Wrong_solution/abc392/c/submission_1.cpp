#include<iostream>
#include<algorithm>

int main()
{
	int n;
	std::cin >> n;
	int P[n + 1];
	int Q[n + 1];
	
	int invP[n + 1];
	int invQ[n + 1];
	
	for (int i = 1; i <= n; ++i) {
		std::cin >> P[i];
		invP[P[i]] = i;
	}
	for (int i = 1; i <= n; ++i) {
		std::cin >> Q[i];
		
		invQ[Q[i]] = i;
	}
	
	for (int i = 1; i <= n; ++i) {
		std::cout << Q[invP[invQ[i]]] << " ";
	}
}