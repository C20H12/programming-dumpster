#include <bits/stdc++.h>
using namespace std;

int main(){

  string test, cyclic;
  cin >> test >> cyclic;

  for (int i = 0; i < cyclic.size() - 1; i++) {
    if (test.find(cyclic) != string::npos) {
      cout << "yes" << endl;
      return 0;
    } else {
      char firstLetter = cyclic[0];
      cyclic.erase(0, 1);
      cyclic.push_back(firstLetter);
    }
    // cout << cyclic << endl;
  }

  cout << "no" << endl;
}