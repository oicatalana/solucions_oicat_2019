#include <iostream>
#include <vector>
using namespace std;


using VE = vector<int>;
using VVE = vector<VE>;
using VVVE = vector<VVE>;


int n;
VE V;
VVVE R;


int f(int i, int x, int s) {
  if (x < 0 or s < 0) return false;
  int& res = R[i][x][s];
  if (res != -1) return res;
  if (s == 0) return res = (x == 0);
  if (x == 0) return res = false;
  if (i == 0) return res = false;
  return res = f(i - 1, x - 1, s - V[i-1]) or f(i - 1, x, s);
}


int main() {
  while (cin >> n) {
    V = VE(n);
    int sum = 0;
    for (int& x : V) {
      cin >> x;
      sum += x;
    }

    if (n%2 or sum%2) cerr << "pifia!!!" << endl;

    R = VVVE(n + 1, VVE(n/2 + 1, VE(sum/2 + 1, -1)));
    cout << (f(n, n/2, sum/2) ? "si" : "no") << endl;
  }
}
