#include <iostream>
#include <string>
#include <vector>
using namespace std;


using VE = vector<int>;
using VVE = vector<VE>;


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
    int m = s.size();
    VVE obs(2*m + 1, VE(2*m + 1, false));
    while (n--) {
      int x, y;
      cin >> x >> y;
      if (abs(x) <= m and abs(y) <= m) obs[x+m][y+m] = true;
    }

    int x = 0;
    int y = 0;
    for (char c : s) {
      int x2, y2;
      mou(x, y, c, x2, y2);
      if (not obs[x2+m][y2+m]) {
        x = x2;
        y = y2;
      }
    }
    cout << "(" << x << ", " << y << ")" << endl;
  }
}

