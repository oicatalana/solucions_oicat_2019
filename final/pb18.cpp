#include <iostream>
#include <vector>
using namespace std;


using VE = vector<int>;
using VC = vector<char>;
using VVC = vector<VC>;


int f(const VE& V) {
  int m = V.size();
  VE pila;
  VE E(m), D(m);
  for (int i = 0; i < m; ++i) {
    while (not pila.empty() and V[pila.back()] >= V[i]) pila.pop_back();
    E[i] = (pila.empty() ? -1 : pila.back());
    pila.push_back(i);
  }

  pila.clear();
  for (int i = m - 1; i >= 0; --i) {
    while (not pila.empty() and V[pila.back()] >= V[i]) pila.pop_back();
    D[i] = (pila.empty() ? m : pila.back());
    pila.push_back(i);
  }

  int res = 0;
  for (int i = 0; i < m; ++i) res = max(res, (D[i] - E[i] - 1)*V[i]);
  return res;
}


int main() {
  int n, m;
  while (cin >> n >> m) {
    VVC M(n, VC(m));
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < m; ++j) cin >> M[i][j];

    int res = 0;
    VE V(m, 0);
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j)
        if (M[i][j] == 'X') V[j] = 0;
        else ++V[j];
      res = max(res, f(V));
    }
    cout << res << endl;
  }
}
