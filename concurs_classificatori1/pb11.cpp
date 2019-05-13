#include <iostream>
#include <vector>
using namespace std;


using VE = vector<int>;
using VVE = vector<VE>;


int n;
VE V;
VVE R;


int f(int i, int s) {
  if (s < 0) return false;
  int& res = R[i][s];
  if (res != -1) return res;
  if (s == 0) return res = true;
  if (i == 0) return res = false;
  return res = f(i - 1, s - V[i-1]) or f(i - 1, s);
}


int main() {
  while (cin >> n) {
    V = VE(n);
    int sum = 0;
    for (int& x : V) {
      cin >> x;
      sum += x;
    }

    sum /= 2;
    R = VVE(n + 1, VE(sum + 1, -1));
    int k = sum;
    while (not f(n, k)) --k;
    cout << 2*(sum - k) << endl;
  }
}
