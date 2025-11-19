#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
    int n; cin >> n;
    for(int k = 0; k < n; k++){
        int size; cin >> size;
        vector<long long> temp(size);
        vector<int> arr(size);
        for(int i = 0; i < size; i++){
            cin >> temp[i];
            arr[i] = i;
        }
        int max = 0;
        do{
            vector<long long> tower = temp;
            for(int i = 0; i < arr.size(); i++){
                int temp = arr[i];
                for(int j = temp + 1; j < temp + tower[temp] + 1; j++){
                    if(j >= tower.size()) break;
                    tower[j]++;
                }
                tower[temp] = 0;
            }
            int mex = 0;
            for(int i = 0; i < tower.size(); i++){
                if(tower[i] == mex + 1) mex++;
                else if(tower[i] > mex || tower[i] < mex) break;
            }
            if(mex == tower[size - 1]) mex++;
            else mex = 0;
            if(max < mex) max = mex;
        }while(next_permutation(arr.begin(), arr.end()));
        cout << max << endl;
    }
    return 0;
}