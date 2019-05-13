#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


bool es_primer(int x) {
  if (x < 2) return false;
  for (int d = 2; d*d <= x; ++d)
    if (x%d == 0) return false;
  return true;
}


int main() {
  vector<int> V = { -9, -8, -7, -6, -5, -3, -2, -1 };
  int n = V.size();
  int x;
  do {
    x = 0;
    for (int i = 0; i < n; ++i) x = 10*x - V[i];
    if (es_primer(x)) break;
  } while (next_permutation(V.begin(), V.end()));
  cout << x << endl;
}
