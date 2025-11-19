#include<iostream>
#include<vector>
#include<algorithm>
int h,w,hh,ww;
std::vector<std::vector<char>> V1;
std::vector<int> V2,V3;
int main(){
  std::cin >> h >> w;
  V1.resize(h);
  for (int i=0;i<h;i++){
    V1[i].resize(w);
    for (int j=0;j<w;j++){
      std::cin >> V1[i][j];
      if (V1[i][j]=='#'){
        V2.push_back(i);
        V3.push_back(j);
      }
    }
  }
  for (int i=*std::min_element(V2.begin(),V2.end());i<=*std::max_element(V2.begin(),V2.end());i++){
    for (int j=*std::min_element(V3.begin(),V3.end());j<=*std::max_element(V3.begin(),V3.end());j++){
      if (V1[i][j]=='.'){
        std::cout << "No";
        return 0;
      }
    }
  }
  std::cout << "Yes";
}
