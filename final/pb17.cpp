#include <iostream>
#include <queue>
#include <vector>
using namespace std;


using VE = vector<int>;
using VVE = vector<VE>;


const VE inc_x = { 1,  1, -1, -1 , 2,  2, -2, -2 };
const VE inc_y = { 2, -2,  2, -2 , 1, -1,  1, -1 };


int f, c;
VVE T;
int n;
VVE G;


void veins(int x, int y) {
  if (T[x][y]) return;
  int v = c*x + y;
  for (int k = 0; k < 8; ++k) {
    int x2 = x + inc_x[k];
    int y2 = y + inc_y[k];
    if (x2 >= 0 and x2 < f and y2 >= 0 and y2 < c and not T[x2][y2])
      G[v].push_back(c*x2 + y2);
  }
}


int amplada(int v) {
  VE dist(n, -1);
  queue<int> Q;
  dist[v] = 0;
  Q.push(v);
  int res = -33;
  while (not Q.empty()) {
    int u = Q.front(); Q.pop();
    for (int z : G[u])
      if (dist[z] == -1) {
        res = dist[z] = dist[u] + 1;
        Q.push(z);
      }
  }
  return res;
}


int main() {
  int p;
  while (cin >> f >> c >> p) {
    T = VVE(f, VE(c, false));
    while (p--) {
      int x, y;
      cin >> x >> y;
      T[x-1][y-1] = true;
    }

    n = f*c;
    G = VVE(n);
    for (int x = 0; x < f; ++x)
      for (int y = 0; y < c; ++y) veins(x, y);

    int res = 0;
    for (int v = 0; v < n; ++v) res = max(res, amplada(v));
    cout << res << endl;
  }
}
