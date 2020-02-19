#include <iostream>
using namespace std;


int x1, y1, x2, y2;


bool parell(int s) {
  return (s + int(1e9))%2 == 0;
}


int solu() {
  int x = abs(x1 - x2);
  int y = abs(y1 - y2);
  if (x >= y) return x + y;
  int canvi = (y1 < y2);
  int res = 2*y;
  if (parell(x1 + y1 + canvi)) ++res;
  if (parell(x2 + y2 + canvi)) --res;
  return res;
}


int main() {
  while (cin >> x1 >> y1 >> x2 >> y2) cout << solu() << endl;
}
