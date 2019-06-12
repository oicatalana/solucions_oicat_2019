#include <iostream>
#include <vector>
using namespace std;


const vector<string> talla = { "S", "M", "L", "XL", "XXL", "XXXL" };


using VE = vector<int>;


VE llegeix() {
  vector<int> V(6);
  for (int i = 0; i < 6; ++i) {
    string s;
    int n;
    cin >> s >> n;
    int j = -1;
    while (talla[++j] != s) ;
    V[j] = n;
  }
  return V;
}


int main() {
  VE D = llegeix();
  VE Q = llegeix();
  for (int i = 0; i < 6; ++i) cout << talla[i] << ' ' << D[i] - 2*Q[i] << endl;
}