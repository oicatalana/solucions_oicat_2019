#include <iostream>
#include <string>
#include <set>
using namespace std;


using P = pair<int, int>;


void mou(int x, int y, char c, int& x2, int& y2) {
  x2 = x;
  y2 = y;
  if (c == 'N') ++y2;
  else if (c == 'S') --y2;
  else if (c == 'E') ++x2;
  else --x2; // 'O'
}


int main() {
  string s;
  int n;
  while (cin >> s >> n) {
    set<P> S;
    while (n--) {
      int x, y;
      cin >> x >> y;
      S.insert(P(x, y));
    }

    int x = 0;
    int y = 0;
    for (char c : s) {
      int x2, y2;
      mou(x, y, c, x2, y2);
      if (S.find(P(x2, y2)) == S.end()) {
        x = x2;
        y = y2;
      }
    }
    cout << "(" << x << ", " << y << ")" << endl;
  }
}

