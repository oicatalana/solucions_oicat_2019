#include <iostream>
using namespace std;


int main() {
  int res = 0;
  for (int x = 20; x <= 60; ++x) {
    int d = x%10;
    if (d and x%d == 0) ++res;
  }
  cout << res << endl;
}
