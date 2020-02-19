#include <iostream>
#include <map>
using namespace std;


using ll = long long;


int main() {
  int n;
  while (cin >> n) {
    map<ll, ll> M;
    M[0] = 0;
    M[2e9] = 1e15;
    while (n--) {
      ll x;
      cin >> x;
      auto p = M.lower_bound(x);
      if (p->first == x) p->second += x;
      else {
        --p;
        M[x] = p->second + x;
        ++p;
      }
      auto q = p; ++q;
      while (q->second <= p->second) M.erase(q++);
    }
    auto p = M.end(); --p; --p;
    cout << p->second << endl;
  }
}
