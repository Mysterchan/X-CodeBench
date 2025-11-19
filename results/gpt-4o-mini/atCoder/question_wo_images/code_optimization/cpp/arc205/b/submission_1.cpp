#include<bits/stdc++.h>
using namespace std;
long long n, m;

int main() {
    cin >> n >> m;
    // The maximum number of edges in a complete graph with n vertices
    long long totalEdges = n * (n - 1) / 2;
    
    // If there are M black edges, we utilize the operations to repaint edges
    // Each operation can convert 3 white edges into black
    // If the number of black edges is even, we won't lose any
    // If it's odd, we lose one black edge after maximally repainting
    long long maxBlackEdges = totalEdges - (m % 2);
    
    cout << maxBlackEdges << endl;
}
