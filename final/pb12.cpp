#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
  int c, n;
  while (cin >> c >> n) {
    vector<int> V(n);
    for (int& x : V) cin >> x;
    V.push_back(0);
    V.push_back(c + 1);
    sort(V.begin(), V.end());
    int mx = 0;
    for (int i = 0; i <= n; ++i) mx = max(mx, V[i+1] - V[i]);
    cout << c + 1 - mx << endl;
  }
}
