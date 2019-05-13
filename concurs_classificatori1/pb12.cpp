#include <iostream>
#include <vector>
#include <set>
using namespace std;


using VE = vector<int>;
using VVE = vector<VE>;
using SE = set<int>;
using VSE = vector<SE>;


VVE G; // graf original
VVE I; // graf invers
VE vist;   // vist[x] diu si el vertex x ja s'ha vist durant el primer recorregut
VE vertex; // vertex[c] indica a quin vertex li toca el numero c per al segon recorregut
VE repre;  // repre[x] es el representant d'x al mateix component fortament connex
int q;  // nombre de components fortament connexos
VE Q;   // Q[r] es la quantitat de vertexs originals dins del component fortament connex d'r
VSE C;  // graf compactat
VSE R1; // primer resultat de la PD: R1[r] son els representants accessibles des d'r
VE R2;  // segon resultat de la PD: R2[r] es el nombre de vertexs originals accessibles des d'r


void prof1(int x) {
  if (vist[x]) return;
  vist[x] = true;
  for (int y : I[x]) prof1(y);
  vertex[q++] = x;
}


void prof2(int x, int r) {
  if (repre[x] != -1) return;
  repre[x] = r;
  for (int y : G[x]) prof2(y, r);
}


int f(int r) {
  int& res = R2[r];
  if (res != -1) return res;

  R1[r].insert(r);
  for (int u : C[r]) {
    f(u);
    for (int v : R1[u]) R1[r].insert(v);
  }

  res = 0;
  for (int u : R1[r]) res += Q[u];
  return res;
}


int main() {
  int n, m;
  while (cin >> n >> m) {
    G = I = VVE(n);
    while (m--) {
      int x, y;
      cin >> x >> y;
      G[x].push_back(y);
      I[y].push_back(x);
    }

    vist = VE(n, false);
    vertex = VE(n, -1);
    q = 0;
    for (int x = 0; x < n; ++x) prof1(x);

    repre = VE(n, -1);
    VE comp(n);
    int s = 0;
    for (int c = n - 1; c >= 0; --c) {
      int x = vertex[c];
      if (repre[x] == -1) {
        prof2(x, x);
        comp[x] = s++; // x sera un representant, pero compactat al numero s
      }
    }

    Q = VE(s, 0);
    C = VSE(s);
    for (int x = 0; x < n; ++x) {
      int r1 = comp[repre[x]];
      ++Q[r1];
      for (int y : I[x]) {
        int r2 = comp[repre[y]];
        if (r1 != r2) C[r1].insert(r2);
      }
    }

    R1 = VSE(s);
    R2 = VE(s, -1);
    int res = 0;
    for (int r = 0; r < s; ++r) res = max(res, f(r));
    cout << res << endl;
  }
}
