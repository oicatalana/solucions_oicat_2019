#include <iostream>
using namespace std;


int x1, y1, y2, x2;


int solu() {
  int sx = x1 + x2;
  int sy = y1 + y2;
  if (sx > sy) return 1;
  if (sy > sx) return 2;
  if (x2 > y1) return 1;
  if (y1 > x2) return 2;
  return 0;
}


int main() {
  cin >> x1 >> y1 >> y2 >> x2;
  int r = solu();
  cout << (r ? (r == 1 ? 'X' : 'Y') : 'P') << endl;
}

