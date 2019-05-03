#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;


using P = pair<int, int>;


int main() {
  int n;
  while (cin >> n) {
    vector<P> V(n);
    for (int i = 0; i < n; ++i) {
      int x;
      cin >> x;
      V[i] = P(x, i);
    }

    sort(V.begin(), V.end());
    int res = 0;
    for (int i = 0; i < n; ++i)
      if (V[i].second != -1) {
        int q = 0;
        int j = i;
        while (V[j].second != -1) {
          int k = V[j].second;
          V[j].second = -1;
          j = k;
          ++q;
        }
        res += q - 1;
      }
    cout << res << endl;
  }
}
