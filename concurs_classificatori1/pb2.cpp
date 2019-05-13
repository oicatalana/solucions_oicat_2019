#include <iostream>
#include <map>
#include <cmath>
using namespace std;


bool arrel(int n) {
  int a = sqrt(n);
  return a*a == n;
}


int main() {
  map<int, int> M;
  for (int a = 1; a < 100; ++a)
    for (int b = a + 1; b < 100; ++b) {
      int q = a*a + b*b;
      if (arrel(q)) {
        int c = sqrt(q);
        if (++M[c] >= 4) cout << "REPE!!! " << c << ' ' << M[c] << endl;
      }
    }
}
