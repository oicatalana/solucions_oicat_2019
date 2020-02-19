#include <iostream>
#include <map>
using namespace std;


using MES = map<int, string>;


MES U = { {0, "zero"}, {1, "u"}, {2, "dos"}, {3, "tres"}, {4, "quatre"}, {5, "cinc"}, {6, "sis"}, {7, "set"}, {8, "vuit"}, {9, "nou"} };

MES D = { {2, "vint"}, {3, "trenta"}, {4, "quaranta"}, {5, "cinquanta"}, {6, "seixanta"}, {7, "setanta"}, {8, "vuitanta"}, {9, "noranta"}, {10, "cent"} };

MES X = { {10, "deu"}, {12, "dotze"}, {14, "catorze"}, {15, "quinze"}, {16, "setze"}, {18, "divuit"} };


string f(int x) {
  if (x < 10) return U[x];
  if (x < 20) return X[x];
  int u = x%10;
  int d = x/10;
  if (u == 0) return D[d];
  return D[d] + (d == 2 ? "-i-" : "-") + U[u];
}


int main() {
  int n;
  cin >> n;
  for (int i = 0; i <= 10; ++i)
    cout << f(n) << " x " << f(i) << " = " << f(n*i) << endl;
}
