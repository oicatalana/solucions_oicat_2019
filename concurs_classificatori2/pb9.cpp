#include <iostream>
using namespace std;


using ll = long long;


bool f(ll n, ll p) {
  if (n == 0) return false;
  p /= 2;
  return (n >= p ? not f(n - p, p) : f(n, p));
}


int main() {
  ll n;
  while (cin >> n) {
    --n;
    ll p = 1;
    while (p <= n) p *= 2;
    cout << n + 1 << " : " << f(n, p) << endl;
  }
}