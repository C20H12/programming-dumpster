#include <bits/stdc++.h>
using namespace std;

// ccc22j3:
int main(){
    string input;
    cin >> input;

    string op;

    for (int i=0; i<input.length(); i++){
        if (input[i]>='A' && input[i]<='Z'){
             op += input[i];
        }

        else if (input[i]=='+' || input[i]=='-'){
            if (input[i]=='+') op += " tighten ";
            else op += " loosen ";
        }

        else{
            if (!(input[i+1]>='A')) op += input[i];
            else{
                op += input[i];
                op += '\n';
            }
        } 
    }

    cout << op << endl;
}


