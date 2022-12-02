#include <iostream>
#include <vector>

using namespace std;

struct dimension {
  int a, b, c;
};

const int INF = int(1e9);

int n, m;
vector<dimension> boxes;

void sort(int &a, int &b, int &c) {
  if(a < b) swap(a, b);
  if(a < c) swap(a, c);
  if(b < c) swap(b, c);
}

int find_min_vol(int a, int b, int c) {
  sort(a, b, c);
  int min_vol = INF;
  for(auto box : boxes) {
    int a2 = box.a, b2 = box.b, c2 = box.c;
    sort(a2, b2, c2);
    if(a <= a2 && b <= b2 && c <= c2) {
      min_vol = min(min_vol, a2*b2*c2);
    }
  }
  return min_vol;
}

int main() {
  cin >> n;
  for(int i=0; i<n; i++){
    int a, b, c;
    cin >> a >> b >> c;
    boxes.push_back({a, b, c});
  }
  cin >> m;
  for(int i=0; i<m; i++){
    int a, b, c;
    cin >> a >> b >> c;
    int min_vol = find_min_vol(a, b, c);
    if (min_vol == INF) {
      cout << "Item does not fit." << endl;
    }
    else {
      cout << min_vol << endl;
    }
  }
}