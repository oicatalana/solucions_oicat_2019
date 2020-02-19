#include <iostream>
#include <vector>
using namespace std;


using VE = vector<int>;


int n, d;
VE V;
VE usat;


void f(int i) {
  if (i == n) {
    for (int x : V) cout << char('A' + x);
    cout << endl;
    return;
  }

  for (int x = 0; x < n; ++x)
    if ((x <= i - d or x >= i + d) and not usat[x]) {
      usat[x] = true;
      V[i] = x;
      f(i + 1);
      usat[x] = false;
    }
}


int main() {
  cin >> n >> d;
  V = VE(n);
  usat = VE(n, false);
  f(0);
}
