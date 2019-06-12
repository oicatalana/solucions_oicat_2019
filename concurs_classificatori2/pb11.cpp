#include <iostream>
#include <vector>
using namespace std;


using ll = long long;
using VE = vector<ll>;


int n;
VE V;
VE parell, senar;


ll maxim(ll x, ll y) {
  if (x > y) return x;
  return y;
}


ll s(int i);


ll p(int i) {
  ll& res = parell[i];
  if (res != -1) return res;
  if (i == n) return res = 0;
  if (V[i]%2) return res = p(i + 1);
  return res = maxim(p(i + 1), V[i] + s(i + 1));
}


ll s(int i) {
  ll& res = senar[i];
  if (res != -1) return res;
  if (i == n) return res = 0;
  if (V[i]%2 == 0) return res = s(i + 1);
  return res = maxim(s(i + 1), V[i] + p(i + 1));
}


int main() {
  while (cin >> n) {
    V = VE(n);
    for (ll& x : V) cin >> x;
    parell = senar = VE(n + 1, -1);
    cout << maxim(p(0), s(0)) << endl;
  }
}