#include <iostream>
#include <vector>
#include <set>
using namespace std;


const string SEP = string(10, '-');
const vector<string> talla = { "S", "M", "L", "XL", "XXL", "XXXL" };


using VE = vector<int>;
using SE = set<int>;


VE D(6), Q(6);


void llegeix(VE& V) {
  for (int i = 0; i < 6; ++i) {
    string s;
    int n;
    cin >> s >> n;
    int j = -1;
    while (talla[++j] != s) ;
    V[j] = n;
  }
}


int mcd(int a, int b) {
  return (b ? mcd(b, a%b) : a);
}


SE divisors(int n) {
  SE div;
  for (int d = 1; d*d <= n; ++d)
    if (n%d == 0) {
      div.insert(d);
      div.insert(n/d);
    }
  return div;
}


bool ok(int y) {
  for (int i = 0; i < 6; ++i)
    if (Q[i]/y > D[i] - Q[i]) return false;
  return true;
}


void solu() {
  int mx = 0;
  for (int q : Q) mx = mcd(mx, q);

  SE S = divisors(mx);

  cout << SEP << endl;
  for (int y : S) {
    if (ok(y)) {
      cout << y << endl;
      for (int i = 0; i < 6; ++i)
        cout << talla[i] << ' ' << D[i] - Q[i] - Q[i]/y << endl;
      return;
    }
  }
  cout << "NO" << endl;
}


int main() {
  string s;
  while (cin >> s) {
    llegeix(D);
    llegeix(Q);
    solu();
  }
}
