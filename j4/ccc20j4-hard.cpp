#include <bits/stdc++.h>
using namespace std;

// vector<int> getZArray(string str) {
  
//   size_t len = str.length();
  
//   vector<int> z(len);

//   int l = 0, r = 0;

//   for (int i = 1; i < len; i++) {
//     if (i > r) {
//       l = r = i;
//       while (r < len && str[r] == str[r - l]) {
//         r++;
//       }
//       z[i] = r - l;
//       r--;
//     } else { // inside the current z-box
//       int k = i - l;
      
//       if (z[k] < r - i + 1) { // if value does not stretch to right bound
//         z[i] = z[k];
//       } else { // if value touches right bound
//         l = i;
//         while (r < len && str[r] == str[r - l]) {
//           r++;
//         }
//         z[i] = r - l;
//         r--;
//       }
//     }
//   }
//   return z;
// }

// bool match(string str, string pattern) {
//   string newStr = pattern + "$" + str;
//   vector<int> zArray = getZArray(newStr);

//   for (int i = 0; i < zArray.size(); i++) {
//     cout << zArray[i] << " ";
//     if (zArray[i] == pattern.size()) {
//       return true;
//     }
//   }

//   return false;
// }





void getZarr(string str, int Z[])
{
	int n = str.length();
	int L, R, k;

	L = R = 0;
	for (int i = 1; i < n; ++i)
	{
		if (i > R)
		{
			L = R = i;

			while (R<n && str[R-L] == str[R])
				R++;
			Z[i] = R-L;
			R--;
		}
		else
		{
			k = i-L;

			if (Z[k] < R-i+1)
				Z[i] = Z[k];

			else
			{
				L = i;
				while (R<n && str[R-L] == str[R])
					R++;
				Z[i] = R-L;
				R--;
			}
		}
	}
}


bool match(string text, string pattern)
{
	string concat = pattern + "$" + text;
	int l = concat.length();

	int Z[l];
	getZarr(concat, Z);

	for (int i = 0; i < l; ++i)
	{
    // cout << Z[i] << endl;
		if (Z[i] == pattern.length()) return true;
	}
  return false;
}

int main(){

  string test, cyclic;
  cin >> test >> cyclic;

  for (int i = 0; i < cyclic.size() - 1; i++) {
    if (match(test, cyclic)) {
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