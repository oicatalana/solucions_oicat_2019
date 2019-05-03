#include <iostream>
using namespace std;


bool zu(int n, int b) {
  if (n == 0) return true;
  if (n%b > 1) return false;
  return zu(n/b, b);
}


bool ok(int n) {
  return zu(n, 2) and zu(n, 3) and zu(n, 4) and zu(n, 5);
}


int main() {
  int n = 2;
  while (not ok(n)) ++n;
  cout << n << endl;
}
