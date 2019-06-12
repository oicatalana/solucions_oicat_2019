#include <iostream>
using namespace std;

bool pal(int x) {
  int c = x;
  int i = 0;
  while (c) {
    i = 10*i + c%10;
    c /= 10;
  }
  return i == x;
}


int main() {
  for (int x = 1; x < 1e9; ++x)
    if (pal(x) and pal(x + 1111)) cout << x << ' ' << x + 1111 << endl;
}