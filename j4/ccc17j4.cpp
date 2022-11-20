#include <bits/stdc++.h>
using namespace std;

int calcTime(int start, int minutes) {
  int hr = floor(start / 100);
  int min = start % 100;
  min += minutes;
  while (min >= 60) {
    min -= 60;
    hr++;
  }
  if (hr != 12) {
    hr %= 12;
  }
  return hr * 100 + min;
}

int main(){

  int min;
  cin >> min;

  vector<int> arthmicTimes;
  for (int i = 1; i <= min; i++) {
    int time = calcTime(1200, i);
    if (time > 999) {
      int dig1 = time % 10;
      int dig2 = (time / 10) % 10;
      int dig3 = (time / 100) % 10;
      int dig4 = (time / 1000) % 10;
      if (dig1 - dig2 == dig2 - dig3 && dig2 - dig3 == dig3 - dig4) {
        arthmicTimes.push_back(time);
      }
    } else if (time > 99) {
      int dig1 = time % 10;
      int dig2 = (time / 10) % 10;
      int dig3 = (time / 100) % 10;
      if (dig1 - dig2 == dig2 - dig3) {
        arthmicTimes.push_back(time);
      }
    }
  }

  cout << floor(arthmicTimes.size() * min / 720) + arthmicTimes.size() << endl;
}