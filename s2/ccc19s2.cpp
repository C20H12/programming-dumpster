#include <bits/stdc++.h>
using namespace std;

// bool isPrime(int n){ //next slowest, O(N/2)
//     if (n==2 || n==3 || n==5 || n==7) return true;
//     else if (n <= 1 || n % 2 == 0 || n % 3 == 0) return false;
//     else{
//         for (int i=3; 2*i<n; i+=2){
//             if (n%i == 0 || n%(i+2) == 0) return false;
//         }
//     }
//     return true;
// }
bool isPrime(int n){ //fastest with 6k+1, O(sqrt(N))
    if (n == 2 || n == 3) return true;
    else if (n <= 1 || n % 2 == 0 || n % 3 == 0) return false;
    else{    
        for (int i=5; i*i <= n; i+=6){
            if (n%i == 0 || n%(i+2) == 0) return false;
        }
    }
    return true;
}
// bool isPrime(int n){ //slowest, O(N)
    
//     if (n <= 1)  return false;
//     else{
//         for (int i=2; i<n; i++){
//             if (n%i == 0){
//                 return false;
//             }
//         }
//     }
//     return true;
// }

int main(){
    int t;
    cin >> t;
    while (t--){
        int input;
        cin >> input;
        int output, output1;
        for (int i=2; i<input*2; i++){
            output = input*2 - i;
            if (isPrime(output) && isPrime(i)){
                output1 = i;
                break;
            }
        }
        cout << output << ' ' << output1 << endl;
    }
}