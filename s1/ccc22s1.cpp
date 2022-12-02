#include <bits/stdc++.h>
using namespace std;

int main(){

    int ip,op=0;
    cin >> ip;

    // if ((ip%4)%5 == 0 || (ip%5)%4 == 0){
    //     op++;
    //     if (ip >= 20){
    //         op += round(ip/20);
    //     }
    // }

    // if (ip==0) op=0;

    for (int i=0; i<=ip/5; i++){
        if ((ip-i*5)%4==0) op++;
    }

    cout << op << endl;
}