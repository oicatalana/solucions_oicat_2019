#include <iostream>
#include <set>
using namespace std;


using SE = set<int>;


int main() {
  int c, n;
  while (cin >> c >> n) {
    set<int> S;
    S.insert(0);
    S.insert(c + 1);
    int res = 0;
    while (n--) {
      int x;
      cin >> x;
      auto e = S.lower_bound(x);
      auto d = e--;
      res += min(x - *e, *d - x);
      S.insert(x);
    }
    cout << res << endl;
  }
}