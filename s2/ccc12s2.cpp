#include <bits/stdc++.h>
using namespace std;

int main(){
  map<char,int> m = {{'I',1}, {'V',1}, {'X',1}, {'L',1}, {'C',1}, {'D',1}, {'M',1}};
  string s;
  cin >> s;
  int total=0;

  for (int i=0; i<s.length(); i+=2){
    int d = s[i] - '0';
    char r = s[i+1];
    int si = 1;
    if (i+3 < s.length()){
      char r2 = s[i+3];
      if (m[r] < m[r2]) si = -1;
    }
    total += d * m[r] * si;
  }
  cout << total << endl;
}

