#include <bits/stdc++.h>
using namespace std;

class Section {
  public:
    int large;
    int mid;
    int small;
    Section() {
      large = 0;
      mid = 0;
      small = 0;
    }

    void addBook(char book) {
      if (book == 'L') {
        large++;
      } else if (book == 'M') {
        mid++;
      } else {
        small++;
      }
    }
};


int main(){
  string allBooks;
  cin >> allBooks;

  Section shelve;

  for (char book : allBooks) {
    shelve.addBook(book);
  }

  Section l;
  Section m;
  // Section s;

  for (int i = 0; i < shelve.large; i++) {
    l.addBook(allBooks[i]);
  }
  for (int i = shelve.large; i < shelve.large + shelve.mid; i++) {
    m.addBook(allBooks[i]);
  }
  // for (int i = shelve.large + shelve.mid; i < shelve.large + shelve.mid + shelve.small; i++) {
  //   s.addBook(allBooks[i]);
  // }

  int missPlacedInL = l.mid + l.small;
  int missPlacedInM = m.large + m.small;
  int shouldSwap = min(l.mid, m.large);

  cout <<  missPlacedInL + missPlacedInM - shouldSwap << endl;
}