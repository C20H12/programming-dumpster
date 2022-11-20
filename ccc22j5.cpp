#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, t;
    cin >> n >> t;

    vector<pair<int,int>> trees;
    vector <int> rows;
    rows.push_back(-1);

    for (int i=0; i<t; i++){
        int r, c;
        cin >> r >> c;
        trees.push_back({c-1,r-1});
        rows.push_back(r-1);
    } 

    rows.push_back(n);
    sort(rows.begin(), rows.end());

    vector<tuple<int,int,int>> itv;

    for (int i=0; i<t+2; i++){
        int r1 = rows[i];
        for (int j=i+1; j<t+2; j++){
            int r2 = rows[j];
            itv.push_back({r2-r1-1, r1, r2});
        }
    }

    sort(itv.begin(), itv.end());
    reverse(itv.begin(), itv.end());
    sort(trees.begin(), trees.end());

    int sqr, pool=0;

    for (auto i: itv){
        if (get<0>(i) <= 0) break;
        int up = get<1>(i), lo = get<2>(i);
        
    }
}