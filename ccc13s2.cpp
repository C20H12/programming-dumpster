#include <bits/stdc++.h>
using namespace std;

int main(){
    int w,n,carW,carsTotW,output=0;
    vector<int> cars;
    cin >> w;
    cin >> n;
    for(int i=0; i<n; i++){
        cin >> carW;
        cars.push_back(carW);
    }
    cars.push_back(0);
    cars.push_back(0);
    cars.push_back(0);
    for (int i=3; i<=cars.size(); i++){
        carsTotW = cars[i] + cars[i-1] + cars[i-2] + cars[i-3];
        if (carsTotW <= w){
            output++;
        }
    }

    cout << output << endl;
}